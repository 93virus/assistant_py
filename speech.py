import pyttsx3
import speech_recognition as sr
import time
import wikipedia

assistantName = "Jarvis"
username = "Bekaass"
dob = 2000
age = time.localtime(time.time()).tm_year - dob
r = sr.Recognizer()

def say(string):
    engine = pyttsx3.init()
    engine.setProperty("rate",140)
    engine.say(string)
    engine.runAndWait()

def greet():
    hour = time.localtime(time.time()).tm_hour
    if hour > 4 and hour < 12:
        say("Good Morning" + username)
    elif hour >= 12 and hour <= 16:
        say("Good afternoon" + username)
    elif hour > 16 and hour <= 20:
        say("Good Evening"+ username)
    else:
        say("Good Night" + username)


def wikisearch(string):
    try:
        result = wikipedia.summary(string, sentences=2)
        print(result)
        say(result)
    except:
        say("Something went wrong")

def recognise():
    print("Recognising..")
    speechText = ""
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio = r.listen(source)
            speechText = r.recognize_google(audio)
            speechText = speechText.lower()
            print("Did you say : " + speechText)
    except sr.RequestError as e:
        print("Could not request results")
    except sr.UnknownValueError:
        print("Unknown error occurred")
    return speechText



time.sleep(0)
while True:
    text = recognise()
    
    if ("wikipedia" in text):
        say("What do you want to search?")
        time.sleep(1)
        searchText = recognise()
        while (searchText == ""):
            say("Say again ?")
            searchText = recognise()
            time.sleep(1)
        else:
            wikisearch(searchText)

    elif ("your name" in text):
        say("my name is " + assistantName)
        
            
