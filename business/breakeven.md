# Breakeven Analysis – **stock-oracle**

## 1. Cost per Active User (USD / month)

| Cost Component | Assumption | Monthly Cost |
|----------------|------------|--------------|
| Compute (t3.medium EC2‑equivalent, 2 vCPU, 4 GB RAM) | $0.0416 / hr → $30 / mo | **$30.00** |
| Storage (SSD, 10 GB per user for SKU master data & forecasts) | $0.10 / GB‑mo | **$1.00** |
| Bandwidth (API & UI traffic, 100 GB per user) | $0.09 / GB | **$9.00** |
| Managed Services (pgvector, logging, monitoring) | 20 % of compute | **$6.00** |
| **Total Variable Cost / Active User** | | **$46.00** |

*Note: Fixed overhead (core dev, DevSecOps, QA) is treated separately in the break‑even calculation.*

---

## 2. Pricing Tiers

| Tier | Price / month | SKU Limit | Core Features |
|------|---------------|-----------|----------------|
| **Basic** | **$49** | ≤ 5 k SKUs | Demand forecast (7‑day), single‑FC replenishment suggestions, email alerts, CSV export |
| **Pro** | **$149** | ≤ 20 k SKUs | Multi‑FC & vendor optimization, safety‑stock modeling, API access, Slack/Teams alerts, 90‑day forecast horizon |
| **Enterprise** | **$499** | Unlimited | Dedicated instance, SLA 99.9 %, custom ML model tuning, priority support, role‑based access, white‑label portal |

*Assumed gross margin = 80 % (variable cost subtracted from price).*

---

## 3. Customer Acquisition Cost (CAC)

| Channel | Typical CAC (USD) | Rationale |
|---------|-------------------|-----------|
| Inbound content + SEO | $200 | Low‑touch self‑serve trial → conversion |
| Outbound SDR + LinkedIn ads | $350 | Mid‑market outreach, 2‑touch demo |
| Agency / partnership referral | $500 | Higher‑touch enterprise sales cycle |

**CAC Range:** **$200 – $500** per paying customer.

---

## 4. Lifetime Value (LTV) Estimate

Assumptions  
- Monthly churn = 5 % (typical for SaaS inventory tools) → average customer lifespan = 1 / 0.05 = **20 months**.  
- Gross margin = 80 %.  

| Tier | ARPU ($/mo) | Gross Margin ($/mo) | LTV = Gross Margin × Lifespan |
|------|-------------|---------------------|------------------------------|
| Basic | 49 | 39.20 | **$784** |
| Pro   | 149 | 119.20 | **$2,384** |
| Enterprise | 499 | 399.20 | **$7,984** |

---

## 5. Break‑Even Users Count

**Fixed Monthly Overhead** (core team, DevSecOps, QA, office): **$12,000**  
*(2 senior engineers @ $6k each, 1 DevSecOps @ $4k, 1 QA/Product @ $2k)*  

Contribution margin per user = Price – Variable Cost.

| Tier | Price | Variable Cost | Contribution / user |
|------|-------|---------------|----------------------|
| Basic | $49 | $46 | **$3** |
| Pro   | $149 | $46 | **$103** |
| Enterprise | $499 | $46 | **$453** |

Break‑even users (assuming a mix) = Fixed Overhead / Avg. Contribution.

- **If all users are Basic:** 12,000 / 3 ≈ **4,000** users.  
- **If all users are Pro:** 12,000 / 103 ≈ **117** users.  
- **If all users are Enterprise:** 12,000 / 453 ≈ **27** users.  

A realistic early‑stage mix (70 % Basic, 20 % Pro, 10 % Enterprise) yields:

- Avg. Contribution = 0.7×3 + 0.2×103 + 0.1×453 ≈ **$71**  
- Break‑even ≈ 12,000 / 71 ≈ **169** paying users.

---

## 6. Path to $10K MRR

Target MRR = $10,000.

| Scenario | Users Needed (by tier) | MRR Contribution |
|----------|------------------------|------------------|
| **Only Basic** | 10,000 / 49 ≈ **204** users | 204 × $49 = $9,996 |
| **Only Pro** | 10,000 / 149 ≈ **68** users | 68 × $149 = $10,132 |
| **Only Enterprise** | 10,000 / 499 ≈ **21** users | 21 × $499 = $10,479 |
| **Mixed (70 % Basic / 20 % Pro / 10 % Enterprise)** | Solve: 0.7x·49 + 0.2x·149 + 0.1x·499 = 10,000 → x ≈ **115** total users → Basic ≈ 81, Pro ≈ 23, Enterprise ≈ 12 | 81×49 + 23×149 + 12×499 ≈ $10,018 |

**Recommended early‑stage path:** acquire **≈ 115 paying users** with the above tier split (≈ 81 Basic, 23 Pro, 12 Enterprise) to reach $10K MRR while keeping CAC within the $200‑$500 band and maintaining healthy LTV:CAC ratios (> 3× for Pro/Enterprise, ≈ 2.5× for Basic, improvable via upsell).