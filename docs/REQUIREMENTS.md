# In X Evolution — Enterprise Requirements Baseline

**Version:** 0.2  
**Date:** 23 November 2026  
**Status:** Proposed requirements — approval and prioritisation required

## 1. Purpose and status

This document defines enterprise-level requirements for the proposed In X Evolution digital business ecosystem. Requirements below are proposed project controls and capability needs; they are not evidence that corresponding software exists.

The requirements must be validated against the selected first business line, legal entity, user workflows, budget and operational capacity.

## 2. Requirement lifecycle

Statuses: Proposed, Approved, Implemented, Verified, Deferred, Rejected.

A requirement becomes Verified only when objective evidence demonstrates that its acceptance criteria have been met.

Priority uses MoSCoW:
- **Must:** essential for safe/legal/core operation or release acceptance.
- **Should:** important but may be deferred with explicit approval.
- **Could:** beneficial where capacity allows.
- **Won't (this release):** explicitly excluded from the current release.

## 3. Enterprise governance requirements

| ID | Requirement | Priority | Proposed acceptance evidence |
|---|---|---|---|
| ENT-GOV-001 | In X Evolution shall maintain an approved purpose, mission, vision, values and scope. | Must | Approved charter |
| ENT-GOV-002 | Each active business line shall have an accountable owner, defined scope and measurable objectives. | Must | Portfolio register |
| ENT-GOV-003 | Material decisions, risk acceptances and scope changes shall be recorded with an approver. | Must | Decision and risk logs |
| ENT-GOV-004 | Shared services and business-line responsibilities shall be explicitly separated. | Should | Operating model and RACI |
| ENT-GOV-005 | The portfolio shall support consolidated reporting without removing business-line accountability. | Should | Approved reporting model |

## 4. Customer, product and commercial requirements

| ID | Requirement | Priority | Proposed acceptance evidence |
|---|---|---|---|
| ENT-CRM-001 | The operating model shall define a controlled register of leads, customers and organisations. | Must | Data model and access test |
| ENT-CRM-002 | Customer records shall have ownership, source, status and a history of material interactions. | Should | Workflow demonstration |
| ENT-PROD-001 | Every product/service shall have an owner, business line, status, scope and lifecycle record. | Must | Product catalogue |
| ENT-PROD-002 | Every published offer shall have accurate description, price/terms and support responsibility. | Must | Offer approval checklist |
| ENT-SALES-001 | The system shall distinguish prospects, quotations, accepted orders/contracts and completed delivery. | Should | End-to-end sales workflow |
| ENT-SALES-002 | Refund, complaint, warranty and cancellation responsibilities shall be defined for each applicable offer. | Must | Published policy and case test |
| ENT-PART-001 | Suppliers, providers, commercial partners and affiliate relationships shall be recorded and reviewed. | Should | Partner register and due-diligence record |
| ENT-PART-002 | Sponsored, paid and affiliate relationships shall be disclosed where required and appropriate. | Must | Content and offer review |

## 5. Operational requirements

| ID | Requirement | Priority | Proposed acceptance evidence |
|---|---|---|---|
| ENT-OPS-001 | Work items shall have an owner, status, due date where relevant and completion evidence. | Should | Workflow report |
| ENT-OPS-002 | Critical workflows shall define approval, exception and escalation paths. | Must | Process test |
| ENT-OPS-003 | Operational records shall preserve timestamps and change history where auditability is required. | Should | Audit trail test |
| ENT-OPS-004 | Community moderation and customer support shall have rules, ownership and escalation. | Should | Operating procedure |
| ENT-OPS-005 | Business continuity and recovery responsibilities shall be documented before production. | Must | Approved runbook |

## 6. Financial management requirements

These are management-control requirements, not a replacement for a statutory accounting system.

| ID | Requirement | Priority | Proposed acceptance evidence |
|---|---|---|---|
| ENT-FIN-001 | Budgets, actual costs and commitments shall be tracked by business line. | Must | Cost report |
| ENT-FIN-002 | Revenue, refunds, fees and direct costs shall be attributable to an offer or business line. | Should | Reconciliation report |
| ENT-FIN-003 | Cash receipts shall be distinguished from invoices, estimates and unrealised valuations. | Must | Financial data definitions |
| ENT-FIN-004 | Spending commitments shall have an authorised owner and approval threshold. | Must | Approval workflow |
| ENT-FIN-005 | Financial exports and source records shall be reconcilable with the authoritative accounting/payment providers. | Must | Reconciliation test |
| ENT-FIN-006 | No customer funds, private keys or custody operations shall be introduced without separate legal and security approval. | Must | Design and compliance sign-off |

## 7. Data, privacy and security requirements

| ID | Requirement | Priority | Proposed acceptance evidence |
|---|---|---|---|
| ENT-DATA-001 | Every data domain shall have an owner, source of truth, classification and retention rule. | Must | Data inventory |
| ENT-DATA-002 | Business-line data access shall be restricted by role and purpose. | Must | Permission tests |
| ENT-DATA-003 | Personal data shall be processed only for defined and documented purposes with an assessed lawful basis. | Must | Privacy/data-flow review |
| ENT-DATA-004 | Data export, correction and deletion procedures shall be defined where applicable. | Must | Demonstrated procedure |
| ENT-SEC-001 | Privileged access shall use least privilege and strong authentication where supported. | Must | Access review |
| ENT-SEC-002 | Secrets shall never be committed to the repository or exposed in logs. | Must | Secret scanning and review |
| ENT-SEC-003 | Security-relevant actions shall be logged without unnecessarily recording sensitive values. | Must | Audit/log review |
| ENT-SEC-004 | Dependencies and deployment configuration shall be reviewed for vulnerabilities. | Should | Build/security report |

## 8. Integration and platform requirements

| ID | Requirement | Priority | Proposed acceptance evidence |
|---|---|---|---|
| ENT-INT-001 | Each integration shall have an owner, purpose, data contract and failure-handling design. | Must | Integration specification |
| ENT-INT-002 | API access shall use scoped credentials stored outside source control. | Must | Security review |
| ENT-INT-003 | Integration retries shall be bounded and safe against duplicate processing where relevant. | Should | Failure/retry test |
| ENT-INT-004 | The Invest workstream's Airtable integration shall have an agreed data model and source-of-truth rules. | Should | Approved mapping and test |
| ENT-INT-005 | The three Mining records identified by the project owner shall be preserved during the Airtable implementation. | Must for that workstream | Before/after record reconciliation |
| ENT-INT-006 | Destructive changes to existing business records shall require explicit approval. | Must | Change approval evidence |

## 9. Non-functional requirements

Specific numerical targets remain open until demand, risk and budget are understood.

| ID | Quality attribute | Requirement |
|---|---|---|
| NFR-001 | Availability | Define service availability targets based on user and business impact before production. |
| NFR-002 | Performance | Establish measurable response-time and workload targets for critical journeys. |
| NFR-003 | Scalability | Support growth without premature infrastructure complexity. |
| NFR-004 | Maintainability | Use modular design, code review, automated tests and current documentation. |
| NFR-005 | Portability | Document data export, provider dependencies and exit options. |
| NFR-006 | Accessibility | Evaluate relevant user interfaces against an agreed accessibility standard. |
| NFR-007 | Resilience | Define backup frequency, recovery point and recovery time objectives. |
| NFR-008 | Observability | Monitor critical application, integration and security events. |
| NFR-009 | Usability | Validate critical journeys with representative users. |
| NFR-010 | Compliance | Assess applicable privacy, consumer, tax, IP and sector-specific obligations. |

## 10. Proposed roles

- Owner / super-admin.
- Portfolio manager.
- Business-line manager.
- Product owner.
- Finance.
- Technical administrator.
- Sales / customer support.
- Marketing / community manager.
- External partner with restricted access.
- Auditor / read-only reviewer.

Role assignments and permissions require approval and must follow least privilege.

## 11. Testing and acceptance

- Unit tests for domain rules and validation.
- Integration tests for database, identity and external-service boundaries.
- E2E tests for the most important approved user journeys.
- Security tests for authentication, authorisation, input validation and secrets handling.
- Data reconciliation tests for financial records and integrations.
- Usability/accessibility checks for user-facing interfaces.
- Performance and recovery tests according to risk and approved targets.

## 12. Traceability

Maintain:

`Strategic objective → Stakeholder need → Requirement → ADR/design → Implementation → Test evidence → Release`

Every Must requirement needs an accountable owner and testable acceptance criteria before being baselined.

## 13. Discovery still required

- Approve the first business line and first release boundary.
- Validate the candidate user segments and priority workflows.
- Confirm legal entity, market, regulatory responsibilities and contracts.
- Define product/service offers, pricing and revenue model.
- Set the cost ceiling, operating reserve and delivery capacity.
- Define data ownership and the role of Airtable versus accounting and payment systems.
- Select technology through documented evaluation and ADRs.
