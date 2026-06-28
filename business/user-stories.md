# User Stories – Stock‑Oracle

## Epic 1: Data Integration & Normalization
**As a** Supply‑Chain Analyst, **I want** to connect our ERP and multiple 3PL fulfillment centers to Stock‑Oracle via secure APIs, **so that** inventory levels and inbound shipments are reflected in real time.  
- Acceptance Criteria  
  - OAuth2 token exchange works for each connected system (ERP, 3PL A, 3PL B).  
  - Stock‑Oracle pulls SKU, quantity, location, and ETA fields nightly and on‑demand.  
  - Data is stored in a normalized schema with SKU as primary key and timestamps for each source.  
  - Validation logs flag any mismatched SKUs or missing required fields.  
  - Dashboard shows a “Data Health” indicator (≥95% completeness) for each source.  
- Estimated Complexity: **M**

**As a** Vendor Manager, **I want** to upload vendor catalogs (CSV/Excel) containing lead times, MOQs, and cost tiers, **so that** the replenishment engine can factor vendor constraints.  
- Acceptance Criteria  
  - Upload UI accepts .csv/.xlsx up to 50 MB and validates required columns.  
  - System parses and stores vendor‑SKU mapping with versioning.  
  - Duplicate SKUs trigger a warning and allow manual resolution.  
  - Uploaded data is available for recommendation runs within 2 minutes.  
  - Audit log records user, timestamp, and file hash.  
- Estimated Complexity: **S**

## Epic 2: AI‑Powered Replenishment Planning
**As a** Inventory Planner, **I want** Stock‑Oracle to generate AI‑driven purchase recommendations for each SKU, **so that** I can minimize stock‑outs while keeping excess inventory low.  
- Acceptance Criteria  
  - Recommendation model outputs suggested order quantity, preferred vendor, and expected arrival date.  
  - Model uses historical sales (last 90 days), current on‑hand, lead time variability, and service level target (default 95%).  
  - Users can adjust service level slider and see impact on suggested qty in real time.  
  - Recommendations are exportable as CSV and pushable to ERP via API.  
  - Back‑test report shows ≥10% reduction in stock‑out incidents vs. baseline on a 4‑week holdout.  
- Estimated Complexity: **L**

**As a** Finance Lead, **I want** to see the projected cost impact of each recommendation (purchase cost, carrying cost, stock‑out cost), **so that** I can approve budgets with confidence.  
- Acceptance Criteria  
  - Cost model includes unit price, inbound freight, warehousing per‑unit‑per‑day, and penalty cost per stock‑out unit.  
  - Totals are displayed per SKU and aggregated by product line.  
  - Users can toggle cost components on/off to see sensitivity.  
  - Export includes a summary table with total projected spend and savings vs. current plan.  
  - Model recalculates instantly when lead time or unit price inputs change.  
- Estimated Complexity: **M**

**As a** Operations Manager, **I want** to simulate “what‑if” scenarios (e.g., supplier delay, demand spike) on the recommended plan, **so that** I can assess risk before executing orders.  
- Acceptance Criteria  
  - Scenario builder lets user adjust lead time (+/- days), demand forecast multiplier, or vendor availability.  
  - System re‑runs the recommendation engine and shows delta vs. baseline plan.  
  - Visual highlights SKUs where stock‑out probability changes >5%.  
  - Scenario can be saved, named, and compared side‑by‑side with other scenarios.  
  - Export includes scenario parameters and resulting order quantities.  
- Estimated Complexity: **L**

## Epic 3: Execution & Vendor Collaboration
**As a** Procurement Officer, **I want** to approve or modify AI‑generated purchase orders directly in Stock‑Oracle, **so that** I maintain control while reducing manual entry errors.  
- Acceptance Criteria  
  - Each recommendation appears as a draft PO with editable fields (qty, vendor, ship‑to).  
  - One‑click “Approve & Send” transmits PO to vendor via EDI or email API.  
  - System logs approval user, timestamp, and any modifications made.  
  - Rejected POs require a comment and move to a “Review” queue.  
  - Sent POs update inventory on‑hand status to “On Order” immediately.  
- Estimated Complexity: **M**

**As a** Vendor Relations Lead, **I want** vendors to receive PO acknowledgments and ASN updates through Stock‑Oracle, **so that** I can track fulfillment performance and reduce manual follow‑ups.  
- Acceptance Criteria  
  - Vendor portal shows PO status (Sent, Acknowledged, Shipped, Received).  
  - ASN upload (EDI 856 or CSV) automatically matches to PO and updates expected receipt date.  
  - Discrepancies >10% in quantity trigger an alert to the planner.  
  - Performance metrics (OTIF, lead time variance) are calculated per vendor and displayed on a dashboard.  
  - Data export available for quarterly vendor reviews.  
- Estimated Complexity: **M**

## Epic 4: Reporting, Alerts & Continuous Improvement
**As a** Director of Supply Chain, **I want** a real‑time dashboard showing inventory health, service level, and turnover metrics, **so that** I can make strategic decisions quickly.  
- Acceptance Criteria  
  - Dashboard widgets: current stock‑out risk (% SKUs < safety stock), weeks of supply, GMROI, and pending PO value.  
  - Data refreshes every 15 minutes from the underlying inventory tables.  
  - Drill‑down from any widget to SKU‑level detail view.  
  - Date range selector (last 7/30/90 days, custom).  
  - Dashboard is role‑based; planners see operational view, executives see financial view.  
- Estimated Complexity: **L**

**As a** System Administrator, **I want** to set up automated alerts (email/Slack) when any SKU’s projected stock‑out probability exceeds a threshold, **so that** the team can act before a disruption occurs.  
- Acceptance Criteria  
  - Alert rule creator allows selection of SKU filter, probability threshold (≥20%), and notification channel.  
  - System evaluates rules after each recommendation run and sends alerts within 5 minutes.  
  - Alert includes SKU, current on‑hand, recommended order, and link to detail view.  
  - Alert history is searchable and exportable for audit.  
  - Duplicate alerts for same SKU within 1 hour are suppressed.  
- Estimated Complexity: **S**