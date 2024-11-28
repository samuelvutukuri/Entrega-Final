from grammar_analysis import GrammarCorrectionWithBart  # Updated import for BART
from preprocessing import preprocess
from vocabulary_analysis import check_vocabulary
from evaluation_function import evaluate_progress
from feedback_generation import generate_feedback
from lesson_recommendation import recommend_lesson
import speech_recognition as sr
from audio_output import speak_feedback

def read_audio_input():
    """
    Captures speech input and converts it to text using Google Speech API.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Speak now:")

        try:
            # Listen for audio input with a longer timeout and a larger phrase_time_limit
            audio = recognizer.listen(source, timeout=15, phrase_time_limit=15)  # Increased timeout and phrase time limit

            # Recognize speech using Google API
            recognized_text = recognizer.recognize_google(audio)

            # Confirm the recognized text
            print(f"Recognized: {recognized_text}")
            confirmation = input("Is this correct? (yes/no): ").strip().lower()
            if confirmation == "yes":
                return recognized_text
            else:
                print("Retrying... Speak again.")
                return read_audio_input()

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio. Please try again.")
            return read_audio_input()
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")
            return ""
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return ""

def main():
    """
    Main function to run the Linguapal language learning assistant.
    """
    print("Welcome to Linguapal: AI Language Learning Assistant")
    print("Choose an input mode: text or audio")

    mode = input("Enter mode (text/audio): ").strip().lower()

    if mode == "text":
        # Accept text input
        user_input = input("Enter your text: ")
    elif mode == "audio":
        # Use audio input
        user_input = read_audio_input()
        if not user_input.strip():
            print("Audio input failed. Exiting.")
            return
        print(f"Recognized text: {user_input}")
    else:
        print("Invalid mode. Please choose 'text' or 'audio'.")
        return

    # Step 2: Preprocess input
    preprocessed_text = preprocess(user_input)

    # Step 3: Grammar analysis using BART-based correction
    grammar_correction = GrammarCorrectionWithBart()
    grammar_errors, corrected_text = grammar_correction.check_and_correct(preprocessed_text)

    # Step 4: Analyze vocabulary
    vocabulary_feedback = check_vocabulary(preprocessed_text)

    # Step 5: Evaluate progress
    evaluation_score = evaluate_progress(grammar_errors, vocabulary_feedback)

    # Step 6: Generate feedback
    feedback = generate_feedback(grammar_errors, vocabulary_feedback, evaluation_score, corrected_text)
    print("\nFeedback:\n", feedback)

    # Step 7: Recommend next lesson
    next_lesson = recommend_lesson(grammar_errors, vocabulary_feedback)
    print("\nRecommended Lesson:\n", next_lesson)

    # Optional: Provide audio feedback
    try:
        speak_feedback(feedback)
    except Exception as e:
        print(f"Audio feedback failed: {e}")

if __name__ == "__main__":
    main()
