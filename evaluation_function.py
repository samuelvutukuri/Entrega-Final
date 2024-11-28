# Evaluation Function: Calculates progress based on grammar and vocabulary metrics
def evaluate_progress(grammar_errors, vocabulary_feedback):
    """
    Evaluates the learner's progress by calculating weighted scores 
    for grammar accuracy, vocabulary retention, and fluency.
    """
    # Grammar score
    total_sentences = 10  # Example total
    grammar_score = 1 - (len(grammar_errors) / total_sentences)

    # Vocabulary score
    target_vocab_size = 100  # Example target size
    missing_vocab = len(vocabulary_feedback["missing"])
    vocab_score = 1 - (missing_vocab / target_vocab_size)

    # Fluency score (mock example)
    coherent_sentences = 8  # Example
    fluency_score = coherent_sentences / total_sentences

    # Weighted evaluation
    evaluation_score = (0.5 * grammar_score) + (0.3 * vocab_score) + (0.2 * fluency_score)
    return evaluation_score
