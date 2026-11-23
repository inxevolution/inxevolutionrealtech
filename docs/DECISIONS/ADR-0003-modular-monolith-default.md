# ADR-0003: Modular Monolith as the Initial Architecture Candidate

- **Status:** Proposed
- **Date:** 2026-11-23
- **Decision owner:** Technical owner (to be assigned)
- **Scope:** In X Evolution pilot only

## Context

The repository defines a multi-area digital business ecosystem, but no pilot, team structure, workload, technology stack or operating budget has been approved. A distributed architecture would introduce deployment, network, observability, security and operational complexity before there is evidence that it is needed.

## Decision

Use a modular monolith as the default candidate for the first application, subject to confirmation during solution design. Organise code around explicit business capabilities and enforce module boundaries. Keep integration adapters and data ownership explicit.

## Options considered

1. **Modular monolith:** one deployable application with cohesive modules and explicit interfaces.
2. **Microservices:** independently deployed services and distributed data/operations.
3. **Low-code / SaaS composition:** assemble capabilities from managed platforms and integrations.

## Rationale

The modular monolith is likely to minimise initial operational cost while preserving a path to later separation. SaaS/low-code may be appropriate for selected workflows after data, access, portability and cost review. Microservices should be chosen only when justified by independent scaling, team autonomy, fault isolation or regulatory boundaries.

## Consequences

### Positive
- Lower deployment and operational complexity for an early pilot.
- Easier local development and end-to-end testing.
- Clear module boundaries can preserve future extraction options.
- Fewer distributed failure modes.

### Negative
- Requires discipline to prevent module coupling.
- A single deployment can create a shared release and failure boundary.
- Scaling modules independently is limited until extraction.

## Revisit when

- A module needs independent scaling or release cadence.
- Availability or fault-isolation requirements cannot be met within one deployment.
- Separate teams need independent ownership.
- Regulatory or security isolation requires a separate boundary.
- Measured operational evidence justifies the additional cost.

## Approval

This ADR is proposed, not approved. Record the approver and date before treating it as a binding technical decision.
