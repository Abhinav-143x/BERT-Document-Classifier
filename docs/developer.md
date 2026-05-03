# Developer README (DEV_README.md)

## 🛠️ Environment Setup

### Prerequisites
- Python 3.11 or higher
- `pip` and `venv`
- Docker (optional, for containerization)

### Local Development
1. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
2. **Install Dependencies**:
   ```bash
   pip install transformers torch fastapi uvicorn scikit-learn
   ```

## 🏗️ Project Structure
```text
BERT-Document-Classifier/
├── src/                # Source code
├── data/               # Datasets (gitignored)
├── models/             # Local model checkpoints
├── tests/              # Unit and integration tests
├── AGENT.md            # AI Agent guidelines
├── DECISIONS.md        # Architectural decisions
└── CHANGELOG.md        # Semantic versioning log
```

## 🧪 Testing
Run tests using pytest:
```bash
pytest
```

## 📦 Deployment
Build the Docker image:
```bash
docker build -t bert-classifier .
```
