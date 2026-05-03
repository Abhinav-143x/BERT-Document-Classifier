# Architectural Decision Log (Reference)

This document serves as a chronological record of the technical and architectural choices made during the development of the BERT Document Classifier. Each entry provides the context, reasoning, and current status of the decision.

## Status Key
- **[ACCEPTED]**: The decision is currently in effect.
- **[DEPRECATED]**: The decision is no longer relevant but kept for historical context.
- **[SUPERSEDED]**: This decision has been replaced by a newer one.

---

## 2026-05-03: Multi-tier Documentation Strategy
- **Decision**: Adopt the Diátaxis framework across all markdown documentation (README, DEV_README, DECISIONS, Tutorials, How-tos).
- **Reason**: To ensure that the documentation scales with the project's complexity and remains user-centric, distinguishing between learning, doing, understanding, and reference.
- **Status**: [ACCEPTED]

## 2026-05-03: Initial Model Selection (BERT)
- **Decision**: Use `bert-base-uncased` from HuggingFace.
- **Reason**: It provides an optimal balance between accuracy and computational requirements (parameters vs performance), making it suitable for deployment on standard cloud instances.
- **Status**: [ACCEPTED]

## 2026-05-03: Web Framework Selection (FastAPI)
- **Decision**: Utilize FastAPI for the inference layer.
- **Reason**: FastAPI provides high performance (via Starlette and Pydantic) and automatic OpenAPI/Swagger documentation, which aligns with our API-first philosophy.
- **Status**: [ACCEPTED]

## 2026-05-03: Dataset Selection (20 Newsgroups)
- **Decision**: Use the `20 Newsgroups` dataset via `scikit-learn` for initial development and verification.
- **Reason**: It is a well-benchmarked, diverse, and programmatically accessible dataset that allows us to verify the BERT pipeline without manual data collection.
- **Status**: [ACCEPTED]

## 2026-05-03: Port Configuration (8081)
- **Decision**: Default the API service to port `8081`.
- **Reason**: Port `8000` and `8080` are frequently used by local development servers (like React or Jenkins); using `8081` minimizes local environment collisions.
- **Status**: [ACCEPTED]
