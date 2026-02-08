import speech_recognition as sr
import pyttsx3
import sys

# ---------------- INITIALIZATION ----------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

recognizer = sr.Recognizer()

# ---------------- SPEAK ----------------
def speak(text):
    print("🤖 Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- LIST MICROPHONES ----------------
def show_microphones():
    print("\n🎙️ Available Microphones:")
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{i}: {name}")
    print()

# ---------------- LISTEN ----------------
def listen():
    try:
        with sr.Microphone(device_index=0) as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        command = recognizer.recognize_google(audio, language="en-IN")
        print("🗣️ You said:", command)
        return command.lower()

    except sr.WaitTimeoutError:
        print("⏰ No speech detected")
        return ""

    except sr.UnknownValueError:
        speak("I did not understand that.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service error.")
        return ""

    except Exception as e:
        print("❌ ERROR:", e)
        return ""

# ---------------- COMMAND HANDLER ----------------
def handle_command(command):
    if not command:
        return

    if command.startswith(("hi", "hello", "hey")):
        speak("Hello! How is your day going?")

    elif "your name" in command:
        speak("I am your Python voice assistant.")

    elif "python" in command:
        speak("Your Python class ends today.")

    elif any(word in command for word in ("exit", "stop", "bye")):
        speak("Goodbye. Have a great day.")
        sys.exit()

    else:
        speak("Sorry, I cannot help with that yet.")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    show_microphones()
    speak("Hello! I am your virtual assistant.")

    while True:
        command = listen()
        handle_command(command)