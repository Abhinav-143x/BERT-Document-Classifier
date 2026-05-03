from fastapi import FastAPI
from transformers import BertTokenizer
import torch

app = FastAPI(title="BERT Document Classifier", version="0.1.0")

# Initialize tokenizer at startup
# Note: We'll use 'bert-base-uncased' as per DECISIONS.md
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

@app.get("/")
def read_root():
    return {"status": "online", "model": "bert-base-uncased"}

@app.get("/test-tokenizer")
def test_tokenizer(text: str = "Hello, BERT!"):
    """Basic test endpoint to verify tokenizer works."""
    tokens = tokenizer.tokenize(text)
    ids = tokenizer.convert_tokens_to_ids(tokens)
    return {
        "text": text,
        "tokens": tokens,
        "token_ids": ids
    }

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8081))
    uvicorn.run(app, host="0.0.0.0", port=port)
