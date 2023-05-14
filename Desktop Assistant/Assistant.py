import pyttsx3
import speech_recognition as sr
from features import GoogleSearch

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 170)

def output(audio):
    print(f":{audio}")
    print("  ")
    engine.say(audio)
    engine.runAndWait()

def Input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 600
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=8,phrase_time_limit=8)
        try:
            print("Recognising...")
            query = r.recognize_google(audio,language='en-in')
            print(f"Your command:{query}\n")
        except:
            return "error"
        return query.lower()
        
def TaskExecute():
    while True:
        query = Input()
        if "google search" in query:
            GoogleSearch(query)
        else:
            print("none")


