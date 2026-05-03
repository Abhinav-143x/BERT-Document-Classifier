import os
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from typing import Tuple, List

class DocumentDataLoader:
    """
    Handles loading the 20 Newsgroups dataset directly from the file system.
    Provides progress tracking and avoids external library hangs.
    """

    def __init__(self, data_path: str = "./data/20news_home", categories: List[str] = None):
        self.data_path = data_path
        self.categories = categories

    def load_20newsgroups(self, test_size: float = 0.2) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Loads data from 20news-bydate-train and 20news-bydate-test folders.
        """
        all_data = []
        subsets = ['20news-bydate-train', '20news-bydate-test']
        
        print(f"🔍 Searching for data in {self.data_path}...")
        
        train_path = os.path.join(self.data_path, '20news-bydate-train')
        if not os.path.exists(train_path):
            raise FileNotFoundError(
                f"Could not find data at {self.data_path}. "
                "Ensure the dataset is downloaded and extracted correctly."
            )
            
        available_categories = sorted(os.listdir(train_path))
        target_categories = [c for c in available_categories if c in self.categories] if self.categories else available_categories
            
        print(f"📂 Found {len(target_categories)} target categories.")
        cat_to_id = {cat: i for i, cat in enumerate(target_categories)}

        for subset in subsets:
            subset_path = os.path.join(self.data_path, subset)
            print(f"📥 Loading subset: {subset}...")
            
            for cat in tqdm(target_categories, desc=f"Loading {subset}"):
                cat_path = os.path.join(subset_path, cat)
                if not os.path.exists(cat_path):
                    continue
                    
                for filename in os.listdir(cat_path):
                    file_path = os.path.join(cat_path, filename)
                    try:
                        with open(file_path, 'r', encoding='latin1') as f:
                            text = f.read()
                        all_data.append({
                            'text': text,
                            'label': cat_to_id[cat],
                            'category_name': cat
                        })
                    except Exception as e:
                        print(f"⚠️ Error reading {file_path}: {e}")

        df = pd.DataFrame(all_data)
        df = df[df['text'].str.strip().str.len() > 10].reset_index(drop=True)
        
        print(f"✅ Successfully loaded {len(df)} documents.")
        
        train_df, test_df = train_test_split(
            df, 
            test_size=test_size, 
            random_state=42, 
            stratify=df['label']
        )
        
        print(f"📊 Final split -> Train: {len(train_df)} | Test: {len(test_df)}")
        return train_df, test_df

if __name__ == "__main__":
    demo_categories = ['sci.med', 'sci.space', 'comp.graphics']
    loader = DocumentDataLoader(categories=demo_categories)
    try:
        train, test = loader.load_20newsgroups()
        print("\nSample Data Point:")
        print(f"Label: {train.iloc[0]['category_name']} (ID: {train.iloc[0]['label']})")
        print(f"Text Preview: {train.iloc[0]['text'][:100]}...")
    except Exception as e:
        print(f"❌ Error: {e}")
