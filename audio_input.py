import speech_recognition as sr

def read_audio_input():
    """
    Captures speech input and converts it to text using Google Speech API.
    Adjusts for longer audio inputs with increased timeout and listening duration.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjust for noise for 2 seconds
        print("Speak now (you have up to 30 seconds):")

        try:
            # Increased timeout and phrase time limit to capture longer inputs
            audio = recognizer.listen(
                source, 
                timeout=40,      # Total timeout of 40 seconds
                phrase_time_limit=35,  # Allow speaking up to 35 seconds
                dynamic_energy_threshold=True  # Automatically adjust energy threshold
            )

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
