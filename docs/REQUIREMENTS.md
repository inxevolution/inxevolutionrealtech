# In X Evolution — Requirements Baseline

**Version:** 0.1  
**Date:** 23 November 2026  
**Status:** Draft — discovery required

## 1. Purpose

This document defines how requirements will be captured, prioritised, validated and traced. Because the business problem and user workflows are not yet documented in the repository, it deliberately does not invent product features.

## 2. Requirement status

Use these statuses:

- **Proposed:** a candidate requirement awaiting review.
- **Approved:** accepted by the authorised owner.
- **Implemented:** delivered in code or configuration.
- **Verified:** acceptance evidence exists.
- **Deferred:** intentionally moved to a later release.
- **Rejected:** considered and not accepted, with a reason recorded.

A requirement is not complete merely because code has been written.

## 3. Requirement categories

| Category | Meaning | Example of evidence |
|---|---|---|
| Business | Outcome or business rule | Approved objective or policy |
| User | User goal or workflow | Validated user scenario |
| Functional | System behaviour | Acceptance test |
| Data | Data entities, quality, lifecycle and retention | Data dictionary and tests |
| Integration | Interaction with external systems | Interface contract and integration test |
| Security | Protection against threats and misuse | Threat model and security tests |
| Privacy | Lawful and proportionate personal-data processing | Data-flow map and privacy assessment |
| Performance | Capacity, latency and throughput | Load-test results |
| Availability / resilience | Recovery and continuity expectations | Recovery test and operational metrics |
| Usability / accessibility | User experience and inclusive access | Usability and accessibility evaluation |
| Operations | Monitoring, support and maintenance | Runbooks and operational checks |

## 4. Initial requirements register

The entries below are **proposed project controls**, not approved product functionality.

| ID | Requirement | Priority | Status | Verification |
|---|---|---|---|---|
| GOV-001 | The project shall maintain an approved scope and named decision owners. | Must | Proposed | Charter review |
| GOV-002 | Major architecture choices shall have a documented rationale and consequences. | Must | Proposed | ADR review |
| ENG-001 | Each delivered change shall be reviewable and traceable to an approved requirement or defect. | Must | Proposed | Pull-request review |
| ENG-002 | Automated tests shall be selected according to component risk and behaviour. | Must | Proposed | Test reports |
| SEC-001 | Credentials and secrets shall not be stored in source control. | Must | Proposed | Secret scanning and review |
| SEC-002 | Access shall follow least-privilege principles. | Must | Proposed | Access review |
| PRIV-001 | Personal-data flows and purposes shall be identified before production processing. | Must | Proposed | Data-flow and privacy review |
| OPS-001 | A production release shall have documented monitoring and recovery procedures. | Should | Proposed | Release-readiness review |
| DOC-001 | User-facing and operator-facing documentation shall be maintained with relevant changes. | Should | Proposed | Documentation review |

## 5. Prioritisation

Use MoSCoW:

- **Must:** essential for legal, safety, core operation or release acceptance.
- **Should:** important, but a controlled release may proceed without it.
- **Could:** beneficial when capacity permits.
- **Won't (this release):** explicitly excluded from the current release.

Priority must include a rationale. “Must” should not be used merely because a stakeholder prefers a feature.

## 6. Requirement writing template

Each product requirement should use this structure:

| Field | Required content |
|---|---|
| ID | Stable identifier, e.g. FUN-001 |
| Name | Short, specific title |
| Statement | “The system shall…” |
| Rationale | User or business need |
| Actor | User, administrator, external system, or scheduled process |
| Preconditions | State required before execution |
| Trigger | User action or system event |
| Main flow | Expected behaviour |
| Alternate / failure flows | Expected handling of exceptions |
| Data | Inputs, outputs, sensitivity and retention |
| Priority | MoSCoW |
| Dependencies | Related requirements or systems |
| Acceptance criteria | Observable, testable outcomes |
| Verification | Inspection, analysis, demonstration or test |
| Owner / status | Accountable approver and current state |

## 7. Acceptance criteria

Acceptance criteria must be objective and testable. Prefer Given/When/Then:

- **Given** a documented initial condition,
- **When** an identified action or event occurs,
- **Then** the expected result is observable,
- and relevant failure, permission and boundary cases are specified.

Avoid vague terms such as “fast”, “secure”, “easy” or “robust” without measurable definitions.

## 8. Traceability

Maintain the following chain:

`Stakeholder need → Requirement → Design decision → Implementation → Test → Release evidence`

A requirement should not be marked Verified until the corresponding evidence is available.

## 9. Discovery inputs still required

- Validated problem statement and business outcomes.
- Target user groups and their workflows.
- Product or service capabilities.
- Data categories, sources, ownership and retention.
- Integration partners and interface requirements.
- Jurisdictions and applicable legal obligations.
- Expected usage, performance and availability.
- Budget, people, delivery constraints and support model.

## 10. Change control

Changes to approved requirements must record: the request, rationale, affected requirements, impact on schedule/cost/risk/architecture, approver, and verification changes.
