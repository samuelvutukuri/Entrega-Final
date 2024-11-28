# Preprocessing Module: Handles text preprocessing
def preprocess(input_text):
    """
    Tokenizes and cleans input text by removing punctuation 
    and converting to lowercase.
    """
    tokenized_text = input_text.split()
    cleaned_text = [word.strip(".,!?") for word in tokenized_text]
    return [word.lower() for word in cleaned_text]
