# Architectural Decisions (DECISIONS.md)

All significant architectural and technical decisions are logged here.

## 2026-05-03: Initial Project Structure
- **Decision**: Adopt a multi-file documentation strategy (README, DEV_README, DECISIONS, AGENT, CHANGELOG, FINAL).
- **Reason**: User preference for heavy documentation and clear separation of concerns between user-facing docs, developer docs, and AI context.
- **Status**: Accepted.

## 2026-05-03: Base Model Selection
- **Decision**: Use `bert-base-uncased` from HuggingFace.
- **Reason**: Industry standard for general-purpose document classification with a good balance between performance and resource consumption.
- **Status**: Proposed.
