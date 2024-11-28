# Vocabulary Analysis Module: Checks vocabulary usage against a target lexicon
def check_vocabulary(preprocessed_text):
    """
    Compares learner input with a predefined vocabulary set 
    and returns missing or extra words.
    """
    target_vocab = {"beginner": ["go", "eat", "see"], "advanced": ["analyze", "explore"]}
    feedback = {"missing": [], "extra": []}
    for word in preprocessed_text:
        if word not in target_vocab["beginner"]:
            feedback["missing"].append(word)
    return feedback
