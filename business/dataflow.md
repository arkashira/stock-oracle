# dataflow.md  

## 1. Overview  

The **Stock‑Oracle** platform ingests real‑time and batch signals from a DTC retailer’s ecosystem, transforms them into demand‑aware replenishment recommendations, stores both raw and enriched artefacts, and serves the results to planners, ERP systems, and BI tools. All data movement is secured with zero‑trust boundaries (OAuth2/JWT + mTLS) and audited via centralized logging.

---

## 2. ASCII System Diagram  

```
+-------------------+        +-------------------+        +-------------------+
|   External Data   |        |   Ingestion Layer |        |   Processing &   |
|   Sources         |        |   (Kafka / S3)    |        |   Transform Tier |
+-------------------+        +-------------------+        +-------------------+
| • POS sales API   |  --->  | • API Gateway     |  --->  | • Spark / Flink   |
| • Vendor catalog  |        | • Kinesis / Kafka |        |   (stream + batch)|
|   (REST, SFTP)    |        | • S3 Landing Zone |        | • Feature Store   |
| • Fulfillment FC  |        | • Auth Proxy (mTLS|        |   (pgvector)      |
|   inventory API   |        |   + JWT)          |        | • Model Service   |
| • Market demand   |        +-------------------+        |   (TF‑Serving)    |
|   (3rd‑party)     |                                      +-------------------+
+-------------------+                                                |
        |                                                            |
        |                                                            v
        |                                                   +-------------------+
        |                                                   |   Storage Tier    |
        |                                                   +-------------------+
        |                                                   | • Raw Lake (S3)   |
        |                                                   | • Curated DW (Redshift) |
        |                                                   | • Time‑Series DB (InfluxDB) |
        |                                                   | • Vector Store (pgvector) |
        |                                                   +-------------------+
        |                                                            |
        |                                                            v
        |                                                   +-------------------+
        |                                                   | Query / Serving   |
        |                                                   +-------------------+
        |                                                   | • GraphQL API (Apollo) |
        |                                                   | • REST Endpoints (FastAPI) |
        |                                                   | • BI Connector (SQL/ODBC) |
        |                                                   | • Cache (Redis) |
        |                                                   +-------------------+
        |                                                            |
        |                                                            v
        |                                                   +-------------------+
        |                                                   |   Egress to User  |
        |                                                   +-------------------+
        |                                                   | • Web UI (React) |
        |                                                   | • Slack / Email Alerts |
        |                                                   | • ERP Push (SFTP/REST) |
        |                                                   | • PDF/CSV Export |
        |                                                   +-------------------+
```

---

## 3. Tier‑by‑Tier Component Breakdown  

### 3.1 External Data Sources  

| Source | Type | Access Method | Frequency | Security |
|--------|------|---------------|-----------|----------|
| POS Transaction Feed | JSON/CSV | HTTPS REST (OAuth2) | Near‑real‑time (push) | API‑Key + JWT |
| Vendor Catalogs | XML/CSV | SFTP / HTTPS | Daily batch | SSH key / TLS |
| Fulfillment Center Inventory | REST | HTTPS (OAuth2) | Every 5 min (poll) | mTLS |
| Market Demand / Trend APIs (e.g., Google Trends, NPD) | JSON | HTTPS (API‑Key) | Hourly | API‑Key |
| ERP Purchase Orders | SOAP / CSV | VPN‑protected endpoint | On‑demand | Mutual TLS |
| Historical Sales DB (legacy) | SQL | JDBC | Nightly batch | IAM role |

### 3.2 Ingestion Layer  

- **API Gateway (Kong / AWS API GW)** – validates JWT, rate‑limits, routes to Kafka topics.  
- **Auth Proxy** – mTLS termination, injects service‑principal identity.  
- **Message Bus** – **Apache Kafka** (3 partitions per source, replication factor = 3) for streaming; **AWS Kinesis** fallback for burst traffic.  
- **Landing Zone** – **Amazon S3** bucket (`s3://stock-oracle/raw/`) with **Object Lock** (WORM) for audit compliance.  
- **Schema Registry** – **Confluent Schema Registry** (Avro) to enforce contract versioning.  

*Auth Boundary*: All inbound traffic must present a valid JWT signed by the corporate IdP; the gateway enforces scope `stock-oracle.ingest`.

### 3.3 Processing / Transform Layer  

| Sub‑tier | Tech | Purpose | Scaling |
|----------|------|---------|---------|
| **Stream Processor** | **Apache Flink** (Docker‑Swarm) | Real‑time demand signal enrichment, out‑of‑stock detection | 4‑node cluster, autoscale on event‑rate |
| **Batch ETL** | **Apache Spark** (EMR) | Nightly reconciliation, feature generation for ML | 8‑node Spark with spot instances |
| **Feature Store** | **pgvector** (PostgreSQL) | Store embeddings of SKU demand patterns | 2‑node HA PostgreSQL |
| **Model Inference Service** | **TensorFlow Serving** (GPU‑enabled) | Run replenishment optimizer (seq2seq + RL) | 2 x NVIDIA T4, horizontal pod autoscaling |
| **Orchestration** | **Airflow** (Celery Executor) | DAG scheduling for batch jobs, model retraining | 3 workers, 1 scheduler |

*Auth Boundary*: Internal services authenticate via **service‑to‑service JWT** signed by internal CA; mTLS enforced on all inter‑process RPC (gRPC, HTTP).

### 3.4 Storage Tier  

| Store | Type | Data | Retention | Security |
|-------|------|------|-----------|----------|
| Raw Lake | Object (S3) | Unprocessed feeds | 365 days | Bucket policy + KMS‑CMK |
| Curated DW | Columnar (Amazon Redshift) | Joined, cleaned tables (`sales_fact`, `inventory_dim`) | 5 years | IAM roles, column‑level encryption |
| Time‑Series DB | InfluxDB | Inventory level time‑series per SKU | 2 years | Token auth, TLS |
| Vector Store | pgvector (PostgreSQL) | SKU demand embeddings | 3 years | Row‑level security, audit logs |
| Model Artifacts | S3 (`model/`) | Serialized TensorFlow checkpoints | Indefinite | Versioned bucket, MFA delete |

*Auth Boundary*: Access to storage is gated by **IAM roles** (least‑privilege). All data at rest encrypted with **AWS KMS** CMK `alias/stock-oracle-data`.

### 3.5 Query / Serving Layer  

- **GraphQL API (Apollo Server)** – single endpoint for UI & external apps; resolves to Redshift or InfluxDB depending on query.  
- **REST Endpoints (FastAPI)** – legacy integration (ERP push).  
- **BI Connector** – ODBC/JDBC driver exposing Redshift schema for Tableau/PowerBI.  
- **Cache Layer** – **Redis (cluster mode)** for hot SKU recommendation look‑ups (TTL = 5 min).  

*Auth Boundary*: Clients must present **OAuth2 access token** with scope `stock-oracle.read`. Tokens are introspected by **OPA** (Open Policy Agent) for fine‑grained row‑level access (e.g., region‑based).

### 3.6 Egress to User  

| Channel | Tech | Format | Frequency |
|---------|------|--------|-----------|
| Web UI | React + Apollo | Interactive dashboards, drill‑down tables | Real‑time (via GraphQL subscription) |
| Slack / Email Alerts | AWS SNS → Lambda → Slack webhook / SES | JSON payload → markdown | Event‑driven (stock‑out, over‑stock) |
| ERP Push | SFTP (AES‑256) / REST (JSON) | PO recommendation file (`recommendations_YYYYMMDD.csv`) | Daily batch (09:00 UTC) |
| Export | CSV / PDF (via Lambda + wkhtmltopdf) | User‑initiated download | On‑demand |
| Mobile App (future) | GraphQL over HTTPS | JSON | Real‑time |

*Auth Boundary*: UI uses **SSO (SAML2) → JWT**; Slack/Email use signed webhook tokens; ERP SFTP uses **SSH key**; REST pushes require **mutual TLS** and API‑Key.

---

## 4. Security & Compliance Summary  

| Layer | Controls |
|-------|----------|
| **Ingress** | API‑Gateway rate limiting, JWT validation, IP allow‑list |
| **Transport** | mTLS everywhere (Kafka, gRPC, REST) |
| **At Rest** | AES‑256 (S3, Redshift, PostgreSQL) with KMS CMK |
| **Identity** | Central IdP (Okta) → OIDC for users, service‑principal JWT for services |
| **Auditing** | CloudTrail + Kafka audit logs → ElasticSearch + Kibana dashboard |
| **Data Governance** | Schema Registry versioning, data‑lineage tracked in **Amundsen** |
| **Disaster Recovery** | Cross‑region S3 replication, Redshift snapshot (daily), Redis replication (3‑zone) |

---

## 5. Key Metrics (for Ops monitoring)  

| Metric | Target |
|--------|--------|
| Ingestion latency (raw → Kafka) | ≤ 30 s |
| Stream processing end‑to‑end latency | ≤ 2 min |
| Model inference latency (per SKU) | ≤ 150 ms |
| Query response (GraphQL) | 95th pct ≤ 300 ms |
| Data freshness in UI | ≤ 5 min |
| SLA for ERP push | 99.5 % on‑time delivery |

---  

*End of dataflow.md*  