# Tutorial: Your First Steps with BERT and FastAPI

This tutorial will guide you through the process of setting up the project and running your first text-processing task using a BERT tokenizer. By the end of this lesson, you will have a live API service that can translate human language into the numerical tokens used by modern language models.

## Prerequisites

Before starting, ensure you have the following installed:
- Python 3.11 or higher
- A terminal/command prompt (PowerShell is recommended for Windows users)

## Step 1: Initialize the Environment

To keep this project's dependencies isolated and avoid conflicts with other Python projects on your machine, we use a project-specific virtual environment named `bert-classifier-env`.

1. Open your terminal in the project root directory.
2. Activate the environment:
   ```powershell
   # Windows
   .\bert-classifier-env\Scripts\activate
   ```
   You should now see `(bert-classifier-env)` at the beginning of your command prompt.

## Step 2: Launch the API Service

We use FastAPI to serve our model logic. The main entry point is located in `src/main.py`.

Run the following command:
```bash
python src/main.py
```

You should see output indicating that the server is running on `http://0.0.0.0:8081`.

## Step 3: Test the Tokenizer

Now that the service is live, we can verify that BERT is correctly processing text. The tokenizer breaks down sentences into "sub-words" and assigns each a unique ID from its pre-trained vocabulary.

1. Open your web browser.
2. Navigate to the following URL:
   [http://localhost:8081/test-tokenizer?text=I love engineering](http://localhost:8081/test-tokenizer?text=I%20love%20engineering)

## Results

You should receive a JSON response similar to this:
```json
{
  "text": "I love engineering",
  "tokens": ["i", "love", "engineering"],
  "token_ids": [1045, 2293, 5030]
}
```

This confirms that:
- The **FastAPI** server is correctly routing requests.
- The **BERT Tokenizer** is successfully loaded and operational.
- Your **Local Environment** is configured correctly.

## Next Steps
Congratulations! You have successfully deployed a basic NLP service. In the next tutorial, we will explore how to load and clean external datasets for model training.
