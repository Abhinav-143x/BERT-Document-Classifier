# Developer README (DEV_README.md)

## 🛠️ Environment Setup

### Prerequisites
- Python 3.11 or higher
- `pip` and `venv`
- Docker (optional, for containerization)

### Local Development
1. **Create Virtual Environment**:
   ```bash
   python -m venv bert-classifier-env
   source bert-classifier-env/bin/activate  # Windows: bert-classifier-env\Scripts\activate
   ```
2. **Install Dependencies**:
   ```bash
   pip install transformers torch fastapi uvicorn scikit-learn pandas
   ```

## 🏗️ Project Structure
```text
BERT-Document-Classifier/
├── src/                    # Source code
├── data/                   # Datasets (gitignored)
├── models/                 # Local model checkpoints
├── tests/                  # Unit and integration tests
├── bert-classifier-env/    # Project-specific virtual environment
├── AGENT.md                # AI Agent guidelines
├── DECISIONS.md            # Architectural decisions
└── CHANGELOG.md            # Semantic versioning log
```

## 🚀 Running the API
The API defaults to port `8081` to avoid conflicts with other projects.
```bash
python src/main.py
```
To use a custom port:
```bash
$env:PORT=9000; python src/main.py
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
