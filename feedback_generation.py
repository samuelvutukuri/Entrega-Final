# Updated Feedback Module
def generate_feedback(grammar_errors, vocabulary_feedback, evaluation_score, corrected_text):
    """
    Summarizes analysis results, including grammar issues, vocabulary feedback,
    and evaluation score. Also provides the corrected sentence.
    """
    # Deduplicate grammar errors and format them for clarity
    unique_errors = list(set(grammar_errors))
    feedback = f"Grammar Errors: {', '.join(unique_errors)}\n"
    feedback += f"Vocabulary Issues: {', '.join(vocabulary_feedback['missing'])}\n"
    feedback += f"Evaluation Score: {evaluation_score:.2f}\n"
    feedback += f"Suggested Correction: {corrected_text}"
    return feedback
