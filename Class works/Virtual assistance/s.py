#pip install pyttsx3 SpeechRecognition
import speech_recognition as sr
import pyttsx3


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)


        try:
            command = recognizer.recognize_google(audio,language='en-in')
            print("🗣️ You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand.")
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("❌ Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""

speak("Hello! I'm your virtual assistant. How can I help you?")
while True:
    command = listen()

    if "hi" in command:
        speak("Hello, How is your day?")

    elif "python" in command:
        speak("Python classes will be end today")
    elif 'your name' in command:
        speak("I am your Python assistant!")

    elif 'stop' in command or 'exit' in command or 'bye' in command:
        speak("Okay bye bye! Have a good day")
        break
    else:
         speak("Sorry, I can't do that yet.")
