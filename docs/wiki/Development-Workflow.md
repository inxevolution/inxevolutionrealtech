# Development Workflow

**Status:** Proposed engineering workflow.

## Branching

- Keep main as the reviewed baseline.
- Create a short-lived branch for each coherent change.
- Use descriptive branch names such as feature/customer-onboarding, docs/architecture-baseline or fix/permission-check.
- Avoid force-pushing shared branches or bypassing review.

## Pull requests

Every pull request should include purpose, related requirement, summary of changes, risk/security/privacy impact, tests and results, migration/recovery notes and documentation changes.

## Commit messages

Use imperative messages with prefixes such as docs, feat, fix, test, refactor, build and security.

## Quality gates

- Review diff and project scope.
- Run formatters and static analysis when a stack exists.
- Run unit, integration and E2E tests as appropriate.
- Scan for secrets and vulnerable dependencies.
- Update requirements and documentation.
- Obtain owner approval.

## Repository protection

Branch-protection settings have not yet been verified. Before production development, evaluate required reviews, status checks and restrictions on direct pushes.

## Releases

Document version, changelog, limitations, migration notes and recovery plan. Never claim tests passed unless executed.
