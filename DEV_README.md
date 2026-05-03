# Technical Reference: BERT Document Classifier

This document provides a technical specification of the project structure, dependencies, and configuration parameters. It is intended as a map for developers who are already familiar with the system.

## Project Structure

The repository is organized into the following functional directories:

| Path | Purpose |
| :--- | :--- |
| `src/` | Primary source code containing model logic, preprocessing, and API routes. |
| `docs/` | Diátaxis-compliant documentation site (MkDocs). |
| `tests/` | Unit and integration tests. |
| `data/` | Local storage for datasets (gitignored). |
| `models/` | Storage for pre-trained model weights and fine-tuned checkpoints. |
| `site/` | Generated documentation site (build output). |

## Core Source Files

- **`src/main.py`**: Entry point for the FastAPI application. Handles routing and initialization.
- **`src/preprocess.py`**: Contains the `TextPreprocessor` class for text normalization.
- **`src/data_loader.py`**: Utility for fetching and splitting the 20 Newsgroups dataset.

## Dependency Specification

The project requires **Python 3.11+**. Key dependencies include:

- `transformers`: HuggingFace library for BERT model loading.
- `torch`: Backend for tensor computations and model inference.
- `fastapi`: Web framework for the API layer.
- `uvicorn`: ASGI server for running the FastAPI application.
- `scikit-learn`: Used for dataset utilities and evaluation metrics.
- `pandas`: Data manipulation and tabular representation.

## Configuration Parameters

The application behavior can be modified through environment variables:

| Variable | Description | Default |
| :--- | :--- | :--- |
| `PORT` | The network port the API will listen on. | `8081` |
| `HOST` | The network host address. | `0.0.0.0` |

## Build Specifications

### Docker Configuration
The project is container-ready. 
- **Base Image**: `python:3.11-slim`
- **Exposed Port**: `8081` (default)
- **Entry Point**: `python src/main.py`

---
*Looking for instructions?*
*   **How-to**: [Environment Configuration](./docs/how-to-env-config.md)
*   **Tutorial**: [Getting Started](./docs/tutorial-getting-started.md)
