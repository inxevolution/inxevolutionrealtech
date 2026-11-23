# In X Evolution — Stakeholders and Users

**Version:** 0.2  
**Date:** 23 November 2026  
**Status:** Initial stakeholder hypotheses — validation required

## 1. Purpose

This document identifies the people and organisations who may influence, operate, use, supply, regulate or be affected by In X Evolution. Roles are defined as functions; actual names and assignments remain to be confirmed.

## 2. Stakeholder map

| Stakeholder | Interest / responsibility | Required engagement |
|---|---|---|
| Founder / project owner | Purpose, ownership, strategy, scope, budget and risk acceptance | Approves charter, priorities, commitments and major changes |
| Executive / portfolio management | Coordination across business lines and shared services | Reviews performance, costs, risk and resource allocation |
| Product / business-line owners | Offer definition, user value, backlog and lifecycle | Own requirements, acceptance and business KPIs |
| Technical lead / developers | Architecture, engineering, delivery and maintenance | Own design decisions, code quality, testing and technical risks |
| Security / privacy lead | Security controls and personal-data governance | Reviews data flows, access, incidents and privacy measures |
| Finance / accounting adviser | Cost control, invoicing, tax records and financial reporting | Reviews legal accounting setup, tax, margins and financial controls |
| Legal / regulatory adviser | Entity, contract, consumer and regulated-activity assessment | Reviews terms, advertising, partnerships and activity boundaries |
| Operations / support | Daily execution, records, customer requests and incidents | Maintains workflows, service quality and escalation |
| Marketing / community managers | Brand, content, acquisition and community moderation | Ensure transparent claims, disclosures and responsible moderation |
| Customers and end users | Receive products, services, information or support | Validate needs, test usability and provide feedback |
| Suppliers / technology providers | Hosting, SaaS, payment, identity, data and technical services | Due diligence, contracts, access and service reviews |
| Commercial / affiliate partners | Referrals, distribution, products or co-marketing | Written terms, disclosure, attribution and performance reviews |
| Financial platform providers | External investment, exchange, wallet or mining services | Provider verification, terms, risks and dependency review |
| Regulators / public authorities | Oversight where activities fall within their remit | Applicability review and compliant operation |

## 3. Candidate user segments

These are discovery personas, not confirmed customer profiles.

### U-01 — Business technology customer
- **Likely need:** website, software, integrations or business automation.
- **Desired outcome:** reduce manual work, improve service or gain reliable digital capability.
- **Validation questions:** what process is painful, what does it cost today, what systems are used, who approves purchase?

### U-02 — Digital finance information user
- **Likely need:** understandable information about platforms, tools, fees, risks and digital asset activities.
- **Desired outcome:** make better-informed independent decisions.
- **Validation questions:** what information is missing, which jurisdictions apply, does the user expect education, comparison or regulated advice?
- **Guardrail:** do not imply personalised recommendations or guaranteed returns.

### U-03 — SHOP visitor / buyer
- **Likely need:** discover and purchase clearly described products.
- **Desired outcome:** a transparent and reliable purchase.
- **Validation questions:** what product category, who is the seller, how are fulfilment, payment, returns and support handled?

### U-04 — Community member
- **Likely need:** updates, learning, discussion and help.
- **Desired outcome:** relevant, safe and useful participation.
- **Validation questions:** which channel, content cadence, moderation rules and support expectations?

### U-05 — Internal operator
- **Likely need:** manage leads, customers, tasks, products, suppliers, financial references and operational records.
- **Desired outcome:** accurate, controlled and auditable operations.
- **Validation questions:** which records are authoritative, what needs approval, what access is required?

### U-06 — Partner / supplier user
- **Likely need:** clear onboarding, integration, referral or delivery processes.
- **Desired outcome:** predictable collaboration and measurable results.
- **Validation questions:** what data is exchanged, who owns the relationship, how are disputes and service failures handled?

## 4. Roles and access model — proposed

| Role | Typical permissions | Restrictions |
|---|---|---|
| Owner / super-admin | Approve policy and manage access | Use privileged access only when needed; protect with MFA |
| Portfolio manager | View consolidated business metrics and approve assigned changes | No unrestricted access to credentials or private customer data |
| Business-line manager | Manage that line's products, customers and operations | No access to unrelated business-line records by default |
| Finance | Manage approved financial records and reports | No secret-key or technical-admin access unless separately authorised |
| Technical administrator | Manage infrastructure and technical configuration | No routine access to financial/customer content |
| Sales / support | Access assigned leads, customers and support cases | No access to restricted finance, investment credentials or other teams' records |
| Marketing / community | Manage approved content, campaigns and community | Use consented data; no unauthorised financial or customer record access |
| External partner | Access only specific approved shared information | Time-limited, least-privilege access |
| Auditor / read-only reviewer | Read assigned evidence and reports | No write or administrative access |

Implement least privilege and segregation of duties. A role title alone must not grant access to sensitive records.

## 5. Stakeholder engagement plan

| Activity | Participants | Output |
|---|---|---|
| Project-owner workshop | Owner and proposed portfolio leads | Purpose, mission, vision, scope and priority |
| Customer discovery | Representative users from the selected segment | Validated problems and workflows |
| Service feasibility review | Product owner and technical lead | Capability, dependencies, delivery cost and limits |
| Invest activity review | Owner, legal/regulatory adviser and relevant operators | Activity classification, provider checks and approved boundaries |
| Commerce review | Owner, operations, finance and legal adviser | Seller model, terms, tax, payment, fulfilment and returns |
| Technical architecture review | Technical lead, security/privacy and operations | Approved architecture, risks and technology choices |
| Financial planning | Owner and accounting/finance adviser | Budget, cash-flow, pricing and unit-economics assumptions |

## 6. Discovery evidence to collect

- Interview notes with consent and no unnecessary personal data.
- User journey and process maps.
- Existing support questions and recurring problems.
- Competitor and alternative-solution analysis.
- Purchase intent, willingness-to-pay signals and objections.
- Operational capacity and skills assessment.
- Partner terms, licences and regulatory status checks.

## 7. Approval and maintenance

The project owner must confirm actual stakeholders, appoint accountable role holders and select the first target segment. Revisit the map when a new business line, regulated activity, data processor or external partner is introduced.
