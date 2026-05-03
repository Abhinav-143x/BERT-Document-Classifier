import re
import string
from typing import List

class TextPreprocessor:
    """Utility class for cleaning and normalizing text for BERT."""
    
    def __init__(self, lowercase: bool = True):
        self.lowercase = lowercase

    def clean(self, text: str) -> str:
        """
        Performs basic cleaning on a single string.
        - Removes URLs
        - Removes extra whitespace
        - Optionally lowercases
        """
        if not text:
            return ""
            
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        if self.lowercase:
            text = text.lower()
            
        return text

    def clean_batch(self, texts: List[str]) -> List[str]:
        """Cleans a list of strings."""
        return [self.clean(t) for t in texts]

if __name__ == "__main__":
    # Quick test
    preprocessor = TextPreprocessor()
    sample = "Check out this link: https://google.com   It has   too many spaces!"
    cleaned = preprocessor.clean(sample)
    print(f"Original: {sample}")
    print(f"Cleaned:  {cleaned}")
