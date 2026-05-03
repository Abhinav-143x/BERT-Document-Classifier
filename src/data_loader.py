from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
import pandas as pd
from typing import Tuple, List

class DocumentDataLoader:
    """Handles fetching and splitting external datasets for classification."""

    def __init__(self, categories: List[str] = None):
        self.categories = categories

    def load_20newsgroups(self, test_size: float = 0.2) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Fetches the 20 Newsgroups dataset and returns train/test dataframes.
        """
        print("📡 Fetching 20 Newsgroups dataset (this may take a moment)...")
        data = fetch_20newsgroups(subset='all', categories=self.categories, remove=('headers', 'footers', 'quotes'))
        
        df = pd.DataFrame({
            'text': data.data,
            'label': data.target
        })

        # Remove empty or very short entries
        df = df[df['text'].str.strip().str.len() > 10].reset_index(drop=True)

        train_df, test_df = train_test_split(df, test_size=test_size, random_state=42, stratify=df['label'])
        
        print(f"✅ Loaded {len(df)} documents across {len(set(data.target))} categories.")
        print(f"📊 Training set: {len(train_df)} | Testing set: {len(test_df)}")
        
        return train_df, test_df

if __name__ == "__main__":
    # Test with a subset of categories for speed
    demo_categories = ['sci.med', 'sci.space', 'comp.graphics']
    loader = DocumentDataLoader(categories=demo_categories)
    train, test = loader.load_20newsgroups()
    print("\nSample Data Point:")
    print(f"Label ID: {train.iloc[0]['label']}")
    print(f"Text Preview: {train.iloc[0]['text'][:100]}...")
