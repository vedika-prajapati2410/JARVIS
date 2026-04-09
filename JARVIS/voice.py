import speech_recognition as sr
def Speech():
    r = sr.Recognizer()
    r.energy_threshold = 150 
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
        print("Audio Captured")

    try:
        text = r.recognize_google(audio, language="en-IN")
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        text = ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        text = ""

def wake(wake_word = "jarvis"):
    print(f"Say '{wake_word}' to wake me up...")
    text = Speech()
    if wake_word in text:
        print("Jarvis Activated! How may i assist you :)...")
        return Speech()
    return ""
