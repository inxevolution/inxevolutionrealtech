# Contributing to In X Evolution

This repository is dedicated exclusively to the In X Evolution project.

## Before making a change

1. Read the project [README](README.md), [charter](docs/PROJECT_CHARTER.md) and relevant requirements.
2. Confirm that the change belongs to the In X Evolution scope.
3. Link the change to an approved requirement, defect or documented decision.
4. Check whether the change affects privacy, security, data, interfaces or operations.

## Branch and review approach

- Keep `main` as the reviewed baseline.
- Use a short-lived branch for each coherent change.
- Prefer small changes that can be reviewed independently.
- Open a pull request describing purpose, scope, risks and verification evidence.
- Do not merge high-impact changes without the required owner approval.

## Commit messages

Use clear, imperative messages with a consistent prefix where useful:

- `docs:` documentation
- `feat:` approved functionality
- `fix:` defect correction
- `test:` tests
- `refactor:` internal restructuring
- `build:` build and dependency changes
- `security:` security hardening

## Quality expectations

- Update documentation with relevant behaviour or interface changes.
- Add or update unit, integration and E2E tests as appropriate.
- Include failure, boundary and permission cases.
- Do not suppress warnings or weaken tests merely to obtain a passing build.
- Record important architectural trade-offs in an ADR.

## Security and privacy rules

- Never commit secrets, credentials, private keys or tokens.
- Never commit real customer or other personal data.
- Use synthetic test data.
- Report suspected vulnerabilities privately to the repository owner rather than publishing exploit details in an issue.
- Review dependencies and licences before introducing them.

## Scope discipline

Do not add unrelated projects, examples or experimental systems to this repository without explicit scope approval. A change that is technically interesting is not automatically in scope.
