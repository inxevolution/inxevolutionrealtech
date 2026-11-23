# In X Evolution — Initial Threat Model

**Status:** Initial, technology-neutral assessment. Revisit when the pilot and data flows are known.

## Scope

The model covers a proposed digital ecosystem with customer-facing channels, staff workflows, identity/access, business modules, data stores and external integrations. It is not a penetration test or certification.

## Assets to protect

- User and customer personal data.
- Authentication sessions and privileged accounts.
- Business plans, source code and intellectual property.
- Financial records and payment references.
- Invest operational and Mining records.
- SHOP orders and fulfilment data.
- Community moderation and support records.
- API credentials, signing keys, backups and audit logs.

## Trust boundaries

1. Public users to application edge.
2. Ordinary users to privileged administration.
3. One business line to another.
4. Application to data store.
5. Application to external provider.
6. Production to development/test environments.
7. Live systems to backups and archives.

## Initial threat register

| ID | Threat | Potential impact | Initial controls | Residual work |
|---|---|---|---|---|
| THR-001 | Account takeover / credential stuffing | Customer or admin account compromise | MFA for privileged users, rate limits, secure sessions, alerting | Select identity provider and test recovery |
| THR-002 | Broken access control / IDOR | Cross-customer or cross-business data disclosure | Server-side object-level authorisation, deny-by-default tests | Build access matrix and negative tests |
| THR-003 | Secret leakage | Provider compromise, financial loss | Secret manager, scanning, rotation, least privilege | Select secret storage and rotation owner |
| THR-004 | Injection / unsafe input | Data exposure or system compromise | Parameterised queries, validation, output encoding | Framework-specific secure coding review |
| THR-005 | Third-party/API compromise | Data leakage or service disruption | Provider due diligence, scoped tokens, timeouts, monitoring | Provider inventory and exit plan |
| THR-006 | Data loss / ransomware | Business interruption and irreversible loss | Isolated backups, least privilege, restore testing | Approve RPO/RTO and rehearse recovery |
| THR-007 | Sensitive data in logs | Privacy breach | Structured redacted logs, access restrictions | Define logging schema and retention |
| THR-008 | Supply-chain vulnerability | Malicious or vulnerable dependency | Lockfiles, dependency scanning, patch policy | Select language/toolchain and CI checks |
| THR-009 | Fraud / payment manipulation | Financial loss and disputes | Trusted provider callbacks, signature checks, reconciliation | Define commerce/payment model |
| THR-010 | Cross-business data mixing | Confidentiality and regulatory failures | Domain boundaries, tenant scoping, access tests | Validate entity and data ownership |
| THR-011 | Social engineering / insider misuse | Unauthorised changes or data export | Separation of duties, approvals, audit trails | Define privileged workflow |
| THR-012 | Long-term cryptographic obsolescence | Future confidentiality/integrity failure | Cryptographic inventory and crypto-agility plan | Define migration ownership and review cadence |

## Abuse cases to test

- A user attempts to access another customer's record by changing an identifier.
- A staff member attempts to access a business line outside their role.
- A revoked provider token is reused.
- A webhook is replayed or delivered more than once.
- An attacker submits malformed or oversized input.
- A backup is deleted using the same compromised credentials as production.
- A user requests deletion/correction of personal data that is also present in exports or archives.
- A public community post attempts to expose private customer information.

## Minimum security acceptance gates

- Threat model reviewed for the chosen pilot.
- Data-flow diagram and data classification approved.
- Authentication, authorisation and session tests pass.
- Secrets are not present in repository history or logs.
- Dependency and static checks run in CI.
- Backup restore is demonstrated.
- Incident contact and escalation route are documented.
- Critical/high findings are fixed or explicitly risk-accepted by an authorised owner.

## Standards and references

Use current versions of OWASP ASVS and OWASP Top 10 as engineering references, NIST Cybersecurity Framework 2.0 for risk governance, and applicable privacy/security law. Standards are references, not evidence of compliance.
