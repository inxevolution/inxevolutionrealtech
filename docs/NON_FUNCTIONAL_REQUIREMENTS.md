# In X Evolution — Non-Functional Requirements

**Status:** Draft targets for pilot sizing; approve and adjust before implementation.

These are proposed acceptance targets, not claims about an existing system. Final values depend on the selected pilot, risk, user volume and budget.

| ID | Quality attribute | Proposed requirement | Verification |
|---|---|---|---|
| NFR-001 | Security | Enforce server-side authorisation for every protected operation | Automated permission tests and review |
| NFR-002 | Authentication | Require strong authentication for privileged roles | Configuration inspection and access tests |
| NFR-003 | Secrets | No credentials, tokens or private keys in source control or logs | Secret scanning and log review |
| NFR-004 | Privacy | Collect only fields required for documented purposes | Data inventory and privacy review |
| NFR-005 | Availability | Define a pilot service objective after hosting and business-hours decisions | Monitoring over agreed measurement window |
| NFR-006 | Performance | Establish baseline; target p95 API response under 500 ms for ordinary non-reporting operations under agreed pilot load | Repeatable load test |
| NFR-007 | Reliability | External calls use timeouts, bounded retries and safe duplicate handling | Integration fault-injection tests |
| NFR-008 | Recoverability | Define RPO/RTO based on business impact; perform a restore rehearsal before production | Restore exercise and evidence |
| NFR-009 | Maintainability | Business rules are modular, documented and covered by automated tests | Code review and coverage of critical rules |
| NFR-010 | Portability | Critical business data can be exported in documented, machine-readable formats | Periodic export and import test |
| NFR-011 | Accessibility | Target WCAG 2.2 AA for customer-facing web journeys where applicable | Automated and manual accessibility review |
| NFR-012 | Observability | Record service health, errors and security events without sensitive payloads | Dashboard and alert test |
| NFR-013 | Scalability | Pilot load and growth assumptions documented; avoid premature distributed architecture | Load test and capacity review |
| NFR-014 | Auditability | Record actor, action, timestamp and target for material privileged changes | Audit trail test |
| NFR-015 | Compatibility | Supported browsers/devices and API version policy documented | Compatibility test matrix |
| NFR-016 | Cost control | Monitor recurring infrastructure and provider spend against approved ceiling | Monthly cost review |

## Measurement rules

- Define the workload, sample size, environment and measurement period before testing.
- Report p50/p95/p99 latency where meaningful, not averages alone.
- Distinguish availability objective from observed availability.
- Set RPO (maximum tolerable data loss) and RTO (target recovery time) with the business owner.
- Do not claim WCAG conformance based only on automated tools.
- Treat all thresholds as pilot proposals until approved.
