# In X Evolution — Implementation Standards

**Version:** 0.1 · **Status:** Proposed engineering standard.

## General
- Implement only approved requirements.
- Prefer readable, maintainable code.
- Keep modules cohesive and interfaces explicit.
- Use supported runtimes and maintained dependencies.
- Document configuration, interfaces and operational behaviour.
- Do not commit secrets, production data or unrelated build artefacts.

## Engineering workflow
1. Link work to an approved requirement or defect.
2. Create a short-lived branch.
3. Design for failure, security, privacy and observability.
4. Implement with automated tests.
5. Run formatters, static analysis and security checks.
6. Review the diff and documentation.
7. Open a pull request with test and risk evidence.
8. Merge after required approvals and checks.

## Testing
- Unit: domain rules, validation and calculations.
- Integration: persistence, authentication and external interfaces.
- E2E: priority user journeys.
- Security: permissions, input handling, secrets and dependencies.
- Data: uniqueness, integrity, migration and reconciliation.
- Performance, recovery and accessibility where required by risk.

## Error handling
Fail safely. Return clear, non-sensitive errors. Do not swallow exceptions. Use timeouts and bounded retries for remote dependencies. Make retried operations idempotent where possible. Avoid logging tokens, passwords, private keys or unnecessary personal data.

## Configuration
Separate environments. Keep secrets in an approved secret manager or protected environment configuration. Document variable names without publishing secret values.

## Documentation
Material features update requirements, architecture, operations and the Wiki. Significant architecture choices require an ADR.

## Release quality
A release requires approved scope, test evidence, security checks, migration/recovery plan, monitoring, support owner and documented residual risks.

Language-specific lint and format rules remain open until the stack is selected.
