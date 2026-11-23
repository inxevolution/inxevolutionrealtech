# In X Evolution — Open Decisions Register

**Version:** 0.1  
**Date:** 23 November 2026

This register prevents unknowns from silently becoming architectural or business assumptions. Each decision should be assigned an owner, supported by evidence and closed through approval or an Architecture Decision Record (ADR) when appropriate.

| ID | Decision / question | Why it matters | Suggested owner | Status |
|---|---|---|---|---|
| DEC-001 | What exact problem does In X Evolution solve? | Defines project purpose and scope | Project owner | Open |
| DEC-002 | Who are the primary users and stakeholders? | Determines workflows and access model | Product owner | Open |
| DEC-003 | What products, services or capabilities are in scope? | Prevents scope ambiguity | Project owner | Open |
| DEC-004 | What are the measurable business outcomes? | Establishes acceptance and success measures | Project owner | Open |
| DEC-005 | Which legal entity, jurisdictions and markets apply? | Determines legal and regulatory assessment | Project owner / legal adviser | Open |
| DEC-006 | What data will be processed and how sensitive is it? | Drives privacy, security and data architecture | Data / privacy owner | Open |
| DEC-007 | What channels are required (web, mobile, API, other)? | Shapes experience and deployment architecture | Product owner | Open |
| DEC-008 | Which programming language and framework are justified? | Determines delivery skills and engineering model | Technical lead | Open |
| DEC-009 | What persistence, search and reporting needs exist? | Drives data-store selection | Technical lead | Open |
| DEC-010 | Is cloud, self-hosting or hybrid operation required? | Affects cost, resilience and data residency | Technical lead / project owner | Open |
| DEC-011 | Which external integrations are essential? | Adds dependency, security and vendor risks | Product owner | Open |
| DEC-012 | What are the budget, team capacity and target dates? | Sets realistic delivery scope | Project owner | Open |
| DEC-013 | What availability, performance and recovery targets are required? | Determines operational design | Technical lead / operations | Open |
| DEC-014 | Who owns production support and incident response? | Ensures operational accountability | Project owner | Open |
| DEC-015 | Should this repository contain one application or multiple bounded components? | Avoids premature service decomposition | Technical lead | Open |

## Decision record template

For each significant decision, create a file under `docs/DECISIONS/`:

1. ID, title, date and status.
2. Context and evidence.
3. Decision drivers and constraints.
4. Options considered.
5. Decision and rationale.
6. Consequences, risks and reversibility.
7. Approver and review date.

## Closure rule

An item is closed only when the answer, evidence, owner and approval are recorded. A preference without rationale is not a completed architecture decision.
