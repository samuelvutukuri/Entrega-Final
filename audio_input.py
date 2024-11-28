import speech_recognition as sr

def read_audio_input():
    """
    Captures speech input and converts it to text using Google Speech API.
    Adjusts for ambient noise and increases the listening timeout to capture longer inputs.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjust for noise for 2 seconds
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
