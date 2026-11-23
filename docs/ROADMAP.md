# In X Evolution — Delivery Roadmap

**Version:** 0.3  
**Date:** 23 November 2026  
**Status:** Proposed sequence — no delivery dates or budgets committed

## Delivery approach

Use stage gates and evidence. The portfolio must not launch every proposed business line simultaneously by default. Select one priority pilot based on validated demand, capability, legal risk and affordable delivery cost.

## Phase 0 — Repository foundation

**Status:** Documentation baseline created on `docs/in-x-evolution-foundation`; draft PR #3 is open.

Deliverables:
- Project charter, requirements and technology-neutral architecture.
- Security, privacy and quality baseline.
- Business strategy and portfolio hypotheses.
- Stakeholder/user map.
- Financial and technical constraints.
- Longevity strategy and stewardship principles.
- Wiki, risk register, KPI catalogue, roadmap and open decisions.

Exit criteria:
- Documentation reviewed.
- Facts distinguished from hypotheses.
- Project owner identified for approval.

## Phase 1 — Business and product discovery

Deliverables:
- Approve purpose, mission, vision, values and strategic objectives.
- Confirm brand ownership, legal entity and portfolio structure.
- Select one first business line and target user segment.
- Validate user problems and workflows.
- Approve an initial product/service offer and exclusions.
- Identify applicable legal, tax, consumer, privacy and sector regulation.
- Define stakeholder roles and decision authority.
- Prepare budget ceiling, resource plan and commercial hypotheses.
- Define success metrics, succession owners for critical roles and a pilot decision.

Exit criteria:
- Project owner signs off the charter and strategy.
- First customer segment, problem and offer have evidence.
- Product owner and technical owner appointed.
- Legal/financial boundaries for the selected offer reviewed.
- Affordable pilot envelope approved.

## Phase 2 — Requirements and solution design

Deliverables:
- Prioritised enterprise requirements baseline.
- Business-line workflows and responsibility matrix.
- Data classification, source-of-truth and data-flow model.
- C4 context and container architecture views.
- Threat model and privacy assessment where required.
- Technology selection and ADRs.
- Integration contracts and provider review.
- Costed hosting, security, backup and support model.
- Data export, archival and provider-exit requirements for critical information.

Exit criteria:
- Must requirements are testable.
- Architecture and vendors are approved.
- Major risks have owners and treatments.
- Operating and cost model is viable.

## Phase 3 — Foundation implementation

Deliverables, subject to the approved stack:
- Reproducible development environment.
- Repository conventions and CI quality gates.
- Identity and access foundation.
- Initial data and interface boundaries.
- Unit and integration testing.
- Development and test environments.
- Initial observability, secret management and backup controls.
- Data inventory and cryptographic inventory for systems that process sensitive or long-lived information.

Exit criteria:
- A minimal technical slice works end-to-end.
- Build and tests are repeatable.
- Security and configuration checks pass.
- No production data or credentials are exposed in development.

## Phase 4 — Pilot product delivery

Deliverables:
- One approved business-line capability.
- E2E tests for critical user journeys.
- User and operator documentation.
- Support, feedback and issue workflow.
- Cost and performance measurement.
- Pilot acceptance evidence.

Exit criteria:
- User outcome is demonstrated.
- Delivery and support costs are measured.
- Risks and user feedback are reviewed.
- Owner decides whether to launch, revise or stop.

## Phase 5 — Production readiness and launch

Deliverables:
- Production deployment and release approval.
- Backup, recovery and incident runbooks.
- Security/privacy and legal review.
- Performance and accessibility checks where relevant.
- Monitoring and support processes.
- Accurate customer terms, pricing and disclosures.
- Verified succession and transfer procedures for critical accounts and roles.

Exit criteria:
- Release checklist signed by accountable owners.
- Recovery and rollback rehearsed where applicable.
- Residual risks documented and accepted.
- Support and finance operations ready.

## Phase 6 — Portfolio expansion and continuous improvement

Expand to other business lines only when the first operating model is stable and expansion has a separate business case.

Measure:
- Customer value, conversion and retention.
- Revenue, gross margin and contribution by line.
- Reliability, incidents and support demand.
- Security, privacy and compliance findings.
- Cost, delivery capacity and provider dependency.
- Test health, succession readiness and documentation drift.

## Phase 7 — Long-term stewardship and renewal

This is a recurring governance responsibility, not a single project phase or a promise of 100-year survival.

| Horizon | Stewardship focus |
|---|---|
| 0–1 year | Approve purpose, pilot, owners, risk controls and record custody |
| 1–5 years | Prove value, financial sustainability, support and recovery |
| 5–15 years | Renew providers, platforms, formats and business models |
| 15–30 years | Review legal structure, governance, archives and succession |
| 30–50 years | Prepare generational leadership and knowledge transfer |
| 50–100 years | Reassess relevance; continue, transform, transfer or close responsibly |

### Recurring review controls

- Annual strategy, risk, succession and continuity review.
- Periodic technology, vendor and dependency inventory.
- Tested data restoration and archival readability for critical records.
- Architecture and portability review at least annually; deeper exit/migration review every three years.
- Revisit century-scale assumptions at least every five years and after material change.
- Define lawful retention and deletion; do not preserve personal information indefinitely by default.

Detailed controls are in [LONGEVITY_STRATEGY.md](LONGEVITY_STRATEGY.md).

## Roadmap governance

Every phase has an owner, deliverables, cost envelope, risks, dependencies and exit evidence. Dates and estimates remain open until discovery and capacity planning are complete.
