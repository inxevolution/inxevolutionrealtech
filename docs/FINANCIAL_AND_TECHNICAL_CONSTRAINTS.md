# In X Evolution — Financial and Technical Constraints

**Version:** 0.2  
**Date:** 23 November 2026  
**Status:** Control baseline — budget and stack not yet approved

## 1. Purpose

This document records the constraints that should govern In X Evolution planning. No project budget, funding level, team capacity, approved hosting provider or technology stack has been supplied. Therefore, this document defines controls and decision criteria rather than inventing amounts or commitments.

## 2. Financial position — current evidence

| Item | Current status |
|---|---|
| Approved project budget | Not supplied |
| Available capital / funding | Not supplied |
| Monthly operating-cost ceiling | Not supplied |
| Team and contractor budget | Not supplied |
| Marketing budget | Not supplied |
| Legal, tax and compliance budget | Not supplied |
| Revenue to date | Not established in this repository |
| Profitability / cash runway | Cannot be calculated from available information |
| Currency and tax treatment | To be confirmed for the legal entity and markets |

**Planning rule:** no recurring subscription, cloud commitment, contractor engagement, advertising spend or third-party financial integration should be treated as approved until an accountable owner authorises its cost and purpose.

## 3. Financial controls

### 3.1 Stage-gated spending

1. Discovery: use existing tools and low-cost research; do not purchase a full production stack.
2. Prototype: approve a written cost cap and measurable test objective.
3. Pilot: approve delivery, support, legal and security costs.
4. Production: approve total cost of ownership, operating reserve and recovery costs.
5. Scale: expand only when customer demand, delivery capacity and unit economics support it.

### 3.2 Required cost categories

Track cost by business line and distinguish one-time from recurring costs:

- Legal, company, tax and accounting.
- Domain, hosting, storage, database and network.
- SaaS subscriptions, APIs and usage charges.
- Development, contractors and support.
- Security, backups, monitoring and incident response.
- Payment processing, refunds and chargebacks.
- Product acquisition, inventory, shipping and returns.
- Marketing, affiliate commissions and content production.
- Insurance, compliance and professional services.

### 3.3 Financial reporting

At minimum, separate:
- Cash balance and actual cash movements.
- Invoiced revenue from cash received.
- Direct cost of goods/services from overhead.
- Gross margin and contribution margin by business line.
- One-time setup cost from recurring operating cost.
- Budget from actual spend and committed future spend.
- Realised financial outcomes from estimates and unrealised valuations.

Do not treat token prices, projected mining rewards, unpaid invoices, referrals not yet paid or unrealised gains as cash.

### 3.4 Pricing and revenue validation

For each offer, calculate:
- Price and tax treatment.
- Direct delivery or product cost.
- Payment and platform fees.
- Support and fulfilment effort.
- Refund/return and warranty exposure.
- Gross margin and contribution margin.
- Customer acquisition cost where measurable.
- Break-even volume and cash conversion cycle.

No prices or revenue forecasts are approved in this baseline.

## 4. Financial risk controls for Invest

- Keep In X Evolution operating funds separate from any personal funds and customer funds.
- Do not accept or hold customer deposits or private keys under this project baseline.
- Do not promise returns, mining yield, token appreciation or capital protection.
- Verify platform identity, authorisation, fees, custody model, withdrawal terms and jurisdiction before referral or integration.
- Disclose commissions, affiliate links, sponsorships and conflicts.
- Record actual fees and realised cash flows separately from market valuations.
- Obtain specialist legal and accounting advice before offering investment, payment, custody, execution, asset-management or crypto-asset services.

The Banco de Portugal explains that payment and electronic-money institutions require appropriate authorisation and publishes information about authorised institutions. The CMVM investor portal provides checks for entities and professionals authorised or registered for relevant investment services in Portugal. These sources should be consulted for the specific proposed activity; this document does not determine legal classification.

References:
- [Banco de Portugal — Institutions and authorised activities](https://clientebancario.bportugal.pt/pt-pt/instituicoes)
- [CMVM — Authorised entities](https://investidor.cmvm.pt/PInvestidor/Content?Input=07D419590495176787CBC8290D95B30F1235C4ACE874EA8E408B180D23294F55&_ts=1720828800034)

## 5. Technical position — current evidence

| Area | Current status |
|---|---|
| Repository | Public GitHub repository |
| Default branch | main |
| Current work | Documentation-only branch and draft pull request |
| Application source code | Not present in initial repository |
| Programming language | Not selected |
| Framework | Not selected |
| Database | Not selected |
| Hosting / cloud | Not selected |
| CI/CD | Not established |
| Production environment | Not established |
| Identity provider | Not selected |
| Monitoring / backup | Not established |
| Airtable | Previously identified as the intended enterprise operations integration for In X Evolution Invest; detailed design and verification remain separate |

## 6. Repository and intellectual-property constraints

The repository is public and its existing `LICENSE` contains The Unlicense public-domain dedication. This is a material commercial decision: third parties may use, copy, modify and distribute material covered by that dedication.

Before proprietary source code, confidential business logic or commercially sensitive assets are added:
1. Decide whether the repository should remain public or become private.
2. Review the current licence and ownership of every contributed asset.
3. Select an appropriate licence with qualified legal advice if proprietary rights are intended.
4. Review visibility, history, forks and copies; making a repository private later does not retract copies already obtained.
5. Never commit passwords, API tokens, private keys, customer personal data or confidential operational records.

No licence or visibility change is made by this documentation update.

## 7. Proposed technical architecture constraints

- Start with a modular, well-separated application design; do not introduce microservices without a justified scaling or organisational need.
- Use clear business-line boundaries for Real Technology, Invest, SHOP and community operations.
- Keep authentication and authorisation centralised where appropriate, with role-based access and least privilege.
- Use documented APIs and explicit data contracts for integrations.
- Maintain separate development, test and production environments.
- Define backups, recovery and monitoring before production.
- Automate repeatable builds, quality checks and tests.
- Prefer maintained dependencies and documented migration paths.
- Design data exports and provider exit plans to limit lock-in.

These are architecture constraints, not a commitment to a specific vendor or programming language.

## 8. Airtable integration boundary

For the Invest workstream, Airtable has been identified as the intended enterprise operations platform. Its role must be defined before implementation:

- Appropriate candidate uses: operational registers, task workflows, research notes, non-secret asset metadata and internal reporting.
- Restricted uses: passwords, seed phrases, private keys, unrestricted authentication tokens or customer funds.
- Financial records: Airtable should not be assumed to replace certified accounting, regulated custody or authoritative banking/broker records.
- Data ownership: define the authoritative source for every field and how corrections are reconciled.
- Access: use role-appropriate access and separate sensitive business-line records.
- Migration: verify and preserve the three Mining records previously identified by the project owner before any schema or data operation.
- Destructive changes: request explicit owner confirmation before deleting, overwriting or materially restructuring existing records.

## 9. Personal data and legal constraints

Where personal data of people in the EU is processed, the project must assess the GDPR principles, including lawfulness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity/confidentiality and accountability.

Reference: [European Commission — Principles of the GDPR](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en).

Also assess, according to actual activities and markets:
- Consumer, e-commerce, distance-selling and returns requirements.
- Marketing, cookies, electronic communications and consent.
- Tax, invoicing and accounting requirements.
- Intellectual property and software licence obligations.
- Sector-specific financial, payment, crypto-asset or investment-service rules.

This is a project control checklist, not legal or tax advice.

## 10. Minimum approvals before implementation

- [ ] Project owner approves budget ceiling and spending authority.
- [ ] First business line and pilot scope selected.
- [ ] Legal entity, ownership and applicable jurisdictions confirmed.
- [ ] Public/private repository and licence strategy reviewed.
- [ ] Data classification and privacy responsibilities agreed.
- [ ] Technology stack selected through documented ADRs.
- [ ] Hosting, backup and operating costs estimated.
- [ ] Third-party vendors and integrations assessed.
- [ ] Financial and regulatory boundaries for Invest confirmed.
