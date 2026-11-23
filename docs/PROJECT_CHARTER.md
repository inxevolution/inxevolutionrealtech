# In X Evolution — Project Charter

**Version:** 0.1  
**Date:** 23 November 2026  
**Status:** Draft — requires project-owner approval

## 1. Purpose of this charter

This charter establishes a controlled starting point for the In X Evolution project. It records what is confirmed, defines the current repository boundary, and identifies decisions that must be made before implementation.

It is not a claim that a particular product, service, company structure, or software platform has already been approved.

## 2. Project identity

| Field | Current value |
|---|---|
| Project name | In X Evolution |
| Repository | inxevolution/inxevolutionrealtech |
| Default branch | main |
| Current phase | Initiation and discovery |
| Project owner | To be formally confirmed |
| Business sponsor | To be confirmed |
| Product owner | To be confirmed |
| Delivery team | To be confirmed |
| Target users | To be confirmed |
| Business domain | To be confirmed |
| Delivery date | Not set |

## 3. Problem statement

**Not yet baselined.** The repository does not currently describe the business or user problem that In X Evolution is intended to solve.

Before implementation, the project owner should approve a concise statement in this form:

> For [identified users or stakeholders] who experience [validated problem], In X Evolution will provide [defined outcome]. Success will be measured by [observable measures], within [known constraints].

No solution architecture should be treated as final until this statement is approved.

## 4. Proposed project outcomes

The following are project-management outcomes, not claims about existing product functionality:

1. Establish an approved problem statement, target users and measurable objectives.
2. Document functional and non-functional requirements.
3. Select an architecture and technology stack using explicit criteria.
4. Deliver implementation in small, verifiable increments.
5. Maintain security, privacy, quality and operational controls throughout delivery.
6. Keep decisions, risks, tests and changes traceable.

## 5. Scope

### Included in this repository

- Project definition and governance for In X Evolution.
- Requirements, architecture and technical decision records.
- Source code and tests that are subsequently approved for this project.
- Build, deployment, security and operational documentation once the relevant technologies and environments are selected.

### Excluded unless explicitly approved

- Unrelated projects, prototypes or experiments.
- Separate products or business initiatives that have not been formally placed inside the In X Evolution scope.
- Production integrations, infrastructure purchases or external account changes.
- Real personal, financial, medical or customer data in development fixtures or documentation.

## 6. Constraints and assumptions

### Confirmed from the repository inspection

- The repository is public.
- The default branch is `main`.
- The repository initially contained `README.md` and `LICENSE`.
- The initial commit is dated 16 November 2026.
- The existing licence file contains The Unlicense dedication.

### Not confirmed

- Business model, geographic scope or legal entity.
- User groups, workflows and service catalogue.
- Applicable legal and regulatory obligations.
- Budget, staffing, delivery dates and service-level objectives.
- Preferred programming language, database, cloud or hosting provider.
- Required third-party platforms and integrations.

## 7. Stakeholders and responsibilities

| Role | Responsibility | Assignment |
|---|---|---|
| Project owner | Approves scope, objectives and major decisions | To be named |
| Product owner | Prioritises user and business requirements | To be named |
| Technical lead | Owns technical design and engineering standards | To be named |
| Security/privacy owner | Reviews security and privacy risks | To be named |
| Contributors | Implement and test approved work | To be assigned |
| Users / representatives | Validate needs and acceptance criteria | To be identified |

One person may hold multiple roles in a small project, but accountability should remain explicit.

## 8. Governance

- Scope changes must be recorded and approved by the project owner.
- Architecture decisions must be documented in an ADR.
- Requirements must have unique identifiers and acceptance criteria.
- Changes should be submitted through reviewable branches and pull requests.
- No secrets or production personal data may be committed.
- Releases must have test evidence and a rollback or recovery plan appropriate to their risk.

## 9. Initial success measures

Targets must be set after discovery. Proposed measures include:

- Percentage of high-priority requirements with approved acceptance criteria.
- Requirement-to-test traceability coverage.
- Automated test pass rate on the release pipeline.
- Number and severity of unresolved security findings.
- Deployment success and recovery performance, once a service exists.
- User acceptance against agreed scenarios.

Do not set numerical targets until a baseline and operating context are known.

## 10. Approval checklist

- [ ] Problem statement approved.
- [ ] Target users and stakeholders identified.
- [ ] Business outcomes and measures approved.
- [ ] Scope and exclusions approved.
- [ ] Budget, constraints and delivery expectations recorded.
- [ ] Product owner and technical lead assigned.
- [ ] Legal, privacy and regulatory applicability reviewed.

## 11. Change history

| Version | Date | Change |
|---|---|---|
| 0.1 | 23 November 2026 | Initial project charter draft |
