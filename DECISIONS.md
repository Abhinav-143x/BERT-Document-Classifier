# Architectural Decisions (DECISIONS.md)

All significant architectural and technical decisions are logged here.

## 2026-05-03: Initial Project Structure
- **Decision**: Adopt a multi-file documentation strategy (README, DEV_README, DECISIONS, AGENT, CHANGELOG, FINAL).
- **Reason**: User preference for heavy documentation and clear separation of concerns between user-facing docs, developer docs, and AI context.
- **Status**: Accepted.

## 2026-05-03: Dataset Selection
- **Decision**: Use the `20 Newsgroups` dataset via `scikit-learn` for initial development and verification.
- **Reason**: It is a well-benchmarked, diverse, and programmatically accessible dataset that allows us to verify the BERT pipeline without manual data collection.
- **Status**: Accepted.
