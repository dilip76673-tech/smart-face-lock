import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak_access_failed():
    engine.say("Access Failed. Unauthorized user detected.")
    engine.runAndWait()