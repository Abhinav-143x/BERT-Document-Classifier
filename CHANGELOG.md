# Changelog (CHANGELOG.md)

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2026-05-03

### Added
- Robust custom `DocumentDataLoader` that reads directly from the file system.
- Explicit progress tracking using `tqdm` for data loading and extraction.
- Manual dataset download utility to bypass scikit-learn's silent hangs.

### Changed
- Replaced scikit-learn's `fetch_20newsgroups` with local file-based loading in `src/data_loader.py`.
- Improved error handling and status reporting during the data preparation phase.

## [0.3.0] - 2026-05-03

### Changed
- Refactored entire documentation suite (README, DEV_README, DECISIONS, AGENT) to follow the Diátaxis framework.
- Restructured README as an Explanation/Vision document.
- Restructured DEV_README as a Technical Reference document.
- Formalized DECISIONS as an Architectural Decision Log (Reference).

## [0.2.0] - 2026-05-03

### Added
- GitHub repository initialization and remote sync.
- Documentation website setup using `MkDocs` and `material` theme.
- `mkdocs.yml` configuration for dark/light themes and technical highlighting.
- `src/preprocess.py`: New utility class for text normalization (URL removal, whitespace cleaning, lowercasing).
- `src/data_loader.py`: Integrated 20 Newsgroups dataset for model training and verification.

### Changed
- Refined project-specific environment and port configuration to avoid system conflicts.

## [0.1.0] - 2026-05-03

### Added
- Initial project directory structure.
- Core documentation suite (README, DEV_README, DECISIONS, CHANGELOG, FINAL).
- Project subdirectories (`src`, `tests`, `data`, `models`).
- Python virtual environment and core dependencies (`transformers`, `torch`, `fastapi`, `uvicorn`).
- Initial boilerplate in `src/main.py` with FastAPI and BERT tokenizer integration.
