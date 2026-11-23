# Requirements and Acceptance

**Status:** Requirements baseline is proposed.

Requirement categories include business, user, functional, data, integration, security, privacy, non-functional and operational requirements.

## Requirement quality

Every requirement needs a stable ID, rationale, owner, priority, dependencies, status and testable acceptance criteria.

Use MoSCoW: Must, Should, Could and Won't this release.

## Acceptance criteria

Prefer Given / When / Then statements. Define preconditions, trigger, expected result, failure conditions, authorisation and data effects.

## Requirement template

- ID and name.
- Requirement statement.
- Business rationale and actor.
- Preconditions and trigger.
- Main and alternate flows.
- Data and security implications.
- Priority and owner.
- Acceptance criteria.
- Verification method and status.

## Traceability

Business objective → stakeholder need → requirement → design/ADR → implementation → test evidence → release.

Use unit tests for isolated rules, integration tests for system boundaries, E2E tests for critical journeys, plus security, data reconciliation, performance and accessibility checks according to risk.

See [Requirements Baseline](../REQUIREMENTS.md).
