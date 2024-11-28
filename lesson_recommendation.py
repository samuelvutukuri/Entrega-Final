# Lesson Recommendation Module: Suggests lessons based on weaknesses
def recommend_lesson(grammar_errors, vocabulary_feedback):
    """
    Recommends the next lesson based on the learner's weaknesses.
    """
    if len(grammar_errors) > 0:
        return {"lesson_type": "grammar", "details": grammar_errors}
    elif len(vocabulary_feedback["missing"]) > 0:
        return {"lesson_type": "vocabulary", "details": vocabulary_feedback["missing"]}
    else:
        return {"lesson_type": "fluency", "details": "General speaking practice"}
