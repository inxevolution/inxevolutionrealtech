# In X Evolution — Phase 2 Solution Design

**Version:** 0.1  
**Status:** Proposed baseline — owner and technical approval required  
**Scope:** In X Evolution only

## Purpose

Translate the approved business direction and discovery evidence into a testable, technology-neutral solution design. This document does not claim that an application, infrastructure, integration or production service exists.

## Design outcomes

1. A bounded context and capability map for the selected pilot.
2. C4 context and container-level views.
3. Data ownership, classification and lifecycle rules.
4. Functional and non-functional requirements with acceptance criteria.
5. Initial threat model and security controls.
6. Technology and provider evaluation criteria.
7. Cost, operations, recovery and exit requirements.
8. Architecture decisions recorded as ADRs.

## Current assumptions and gates

- The portfolio labels Real Technology, Invest, SHOP and Real Telegram/Community are proposed pending owner confirmation.
- One business line must be selected for the first pilot; do not implement the entire portfolio at once.
- A modular monolith is the default candidate until evidence justifies distribution.
- Airtable is a candidate operational tool for an Invest workstream, not a presumed system of record for finance, regulated custody or secrets.
- No programming language, framework, database, cloud provider, payment provider or identity provider is selected.
- Applicable legal, privacy, tax, consumer and sector requirements must be assessed for the selected service and jurisdiction.

## Design sequence

| Step | Activity | Required evidence |
|---|---|---|
| 1 | Confirm pilot, users and workflows | Approved scope and validated user journeys |
| 2 | Map business capabilities and boundaries | Context map and accountable owners |
| 3 | Define information architecture | Data catalogue, classification and source-of-truth matrix |
| 4 | Define solution structure | C4 context/container views and interface boundaries |
| 5 | Assess security and privacy | Threat model, data-flow review and risk treatments |
| 6 | Compare technology options | Weighted evaluation and cost assumptions |
| 7 | Define operating model | Hosting, monitoring, backup, support and incident requirements |
| 8 | Approve design | ADRs, residual risks, budget and sign-off |

## Stage gates

### Gate A — Business input ready
- One pilot business line and target user are confirmed.
- The problem, value proposition and excluded scope are documented.
- Legal and financial boundaries are identified.
- An accountable product owner is named.

### Gate B — Design ready
- Requirements are testable and prioritised.
- Data ownership and access boundaries are explicit.
- Architecture, threat model and integration contracts are reviewed.
- Technology options and total cost assumptions are compared.
- Major risks have owners and treatments.

### Gate C — Build authorised
- The owner approves the pilot scope and budget.
- Technical owner and operational support owner are named.
- Required legal/privacy/security reviews are complete for the planned processing.
- No unresolved critical risk is silently accepted.

## Traceability

Every implementation item must link to:
- A business objective or validated user need.
- A requirement ID.
- A design decision or interface specification where relevant.
- Unit, integration, security or E2E test evidence.
- A release and operational owner.

## Explicit non-goals

This phase does not authorise:
- Launching all portfolio areas.
- Providing regulated investment, payment, custody or crypto-asset services.
- Moving production or sensitive personal data into unapproved tools.
- Destructive changes to Airtable or existing Mining records.
- Purchasing infrastructure or paid services.
- Publishing secrets, credentials or private customer information.

## Approval record

| Role | Name | Decision | Date |
|---|---|---|---|
| Project owner | To be assigned | Pending | — |
| Product owner | To be assigned | Pending | — |
| Technical owner | To be assigned | Pending | — |
| Privacy/legal adviser (as applicable) | To be assigned | Pending | — |
