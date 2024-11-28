# Audio Output Module: Reads feedback aloud
import pyttsx3

def speak_feedback(feedback_text):
    """
    Converts feedback text into spoken audio output.
    """
    engine = pyttsx3.init()
    engine.say(feedback_text)
    engine.runAndWait()
