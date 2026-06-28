# partner-targets.md

## Partner Integration Roadmap  

| # | Partner (API / SaaS) | Free‑tier Limits* | Integration Effort | Value‑Add (User Job Solved) | Affiliate / Revenue‑Share |
|---|----------------------|-------------------|--------------------|-----------------------------|---------------------------|
| 1 | **Shopify** (REST Admin API + Webhooks) | Unlimited API calls on paid plans; 1 000 + webhook events free on dev store | **S** – straightforward REST + webhook subscription | Syncs DTC orders → inventory, enabling automatic replenishment triggers | **Yes** – Shopify Affiliate Program (referral revenue) |
| 2 | **Amazon Marketplace Web Services (SP‑API)** | 1 000 requests/day free (sandbox); no hard quota on production | **L** – complex OAuth, pagination, and high‑volume data handling | Pulls Amazon sales velocity → feeds replenishment engine for FBA & vendor‑fulfilled SKUs | **Yes** – Amazon Partner Network (referral fees) |
| 3 | **Stripe** (Payments & Connect API) | No request caps; pay‑as‑you‑go (no free tier needed) | **S** – simple JSON endpoints, webhook support | Reconciles purchase‑order payments → ensures cash‑flow visibility for replenishment decisions | **Yes** – Stripe Affiliate Program (referral revenue) |
| 4 | **ShipStation** (Shipping & Order Management API) | 50 shipments/month on free plan; unlimited API calls | **M** – requires mapping order statuses & shipping carriers | Aligns fulfillment‑center shipping schedules with replenishment forecasts | **Yes** – ShipStation Affiliate Program (referral) |
| 5 | **TradeGecko (QuickBooks Commerce)** | 100 orders/month on free tier; API rate limit 10 req/s | **M** – REST API with inventory‑level endpoints | Centralizes multi‑channel inventory → prevents stock‑outs across vendors | **Yes** – TradeGecko Partner Program (revenue share) |
| 6 | **Cin7** (Inventory Management API) | 500 SKUs & 1 000 orders/month on trial; API limits 5 req/s | **L** – enterprise‑grade data model, requires custom sync logic | Provides a single source of truth for high‑SKU DTC catalogs | **Yes** – Cin7 Referral Partnership (commission) |
| 7 | **Alibaba Supplier Center API** | 10 000 calls/month free (sandbox) | **L** – SOAP/REST hybrid, requires vendor onboarding | Enables direct purchase‑order creation with suppliers → automates replenishment triggers | **No** (no public affiliate program) |
| 8 | **NetSuite** (SuiteTalk / REST) | 1 000 transactions/month free on trial | **L** – heavy enterprise integration, requires middleware | Syncs enterprise‑level financials & inventory → validates purchase‑order profitability | **Yes** – NetSuite Partner Program (referral) |

\*Free‑tier limits reflect the most generous tier offered at the time of writing; actual limits may vary with plan upgrades.

### Prioritization Logic
1. **Affiliate/Revenue‑Share** – Partners 1, 2, 3, 4, 5, 6, 8 all provide a partner program that can generate recurring revenue for Axentx, making them high‑priority integration targets.  
2. **Strategic Fit** – Shopify, Amazon, and Stripe directly feed order‑flow and payment data that are core to inventory replenishment decisions.  
3. **Implementation Complexity** – We start with **S**‑effort partners (Shopify, Stripe) to quickly deliver value, then move to **M** (ShipStation, TradeGecko, Cin7) and finally **L** (Amazon SP‑API, NetSuite, Alibaba) for deeper, higher‑impact integrations.  

### Next Steps
- **Sprint 1 (2 weeks):** Build Shopify & Stripe connectors (S effort) → launch pilot with 2‑3 DTC brands; capture affiliate referrals.  
- **Sprint 2 (3 weeks):** Extend to ShipStation & TradeGecko (M effort) → enable multi‑fulfillment center syncing.  
- **Sprint 3 (4 weeks):** Develop Amazon SP‑API and NetSuite integrations (L effort) → target high‑volume DTC retailers using FBA and ERP systems.  

This roadmap delivers a phased, revenue‑generating partner ecosystem while solving the core user job of **“real‑time inventory visibility & automated purchase ordering”** across the DTC stack.