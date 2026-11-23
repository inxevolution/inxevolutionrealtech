# Architecture Principles

**Status:** Technology-neutral proposal; no production architecture is implemented.

## Principles

1. Requirements and user outcomes before tools.
2. Modular design with clear business-line boundaries.
3. Start with the simplest architecture that meets validated needs.
4. Do not introduce microservices without scale or operational justification.
5. Keep authoritative data sources explicit.
6. Secure identity, permissions and trust boundaries.
7. Document interfaces and integration failure behaviour.
8. Design for testability, observability and recovery.
9. Measure total cost of ownership and vendor exit cost.
10. Maintain data export and migration options.

## Proposed logical areas

- Experience and channel layer.
- Identity and access.
- Business workflows and domain capabilities.
- Data and reporting.
- Integration boundary.
- Audit, monitoring and operations.

Programming language, framework, database, cloud, identity provider, CI/CD and analytics tools remain open decisions.

## Airtable boundary

Airtable is the intended operations platform for the Invest workstream, subject to design approval. Do not store passwords, seed phrases, private keys or unrestricted tokens there. Preserve the three identified Mining records and require explicit approval for destructive changes.

See [Architecture Baseline](../ARCHITECTURE.md) and ADR files in the decisions directory.
