import pyttsx3
import speech_recognition as sr
import time
import wikipedia
import os
import webbrowser
import pyautogui
from tkinter import *

assistantName = "Jarvis"
username = "Bekaass"
dob = 2000
age = time.localtime(time.time()).tm_year - dob
r = sr.Recognizer()

time.sleep(0)

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
    r.energy_threshold = 3500
    print("Recognising..")
    speechText = ""
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.5)
            audio = r.listen(source)
            speechText = r.recognize_google(audio)
            speechText = speechText.lower()
            print("Did you say : " + speechText)
    except sr.RequestError as e:
        print("Could not request results")
        say("say again")
    except sr.UnknownValueError:
        print("Unknown error occurred")
        say("say again")
    return speechText


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
        wikisearch(searchText)

    elif ("your name" in text):
        say("my name is " + assistantName)
    
    elif ("my name" in text):
        say("your name is " + username)
        
    elif ("my age" in text):
        say("your age is " + str(age))
            
    elif ("working directory" in text):
        print(os.getcwd())
        say(os.getcwd())

    elif ("open browser" in text):
        webbrowser.open("google.com")
        print("--Browser opened--\n")

    elif ("search internet" in text):
        webbrowser.open("google.com")
        print("--Browser opened--")
        search = recognise()
        while (search == ""):
            say("say again")
            search = recognise()
        pyautogui.typewrite(search, interval=0.1)
        pyautogui.press("enter")
        print("--searched--")
        print("--Browser module closed--\n")

    elif ("scroll up" in text):
        pyautogui.scroll(30)
        print("--Scrolled up--\n")
    
    elif ("scroll down" in text):
        pyautogui.scroll(-30)
        print("--Scrolled down--\n")

    elif ("copy" in text):
        pyautogui.hotkey('ctrl','c')
        print("--Copied--\n")

    elif ("paste" in text):
        pyautogui.hotkey('ctrl','v')
        print("--Paste done--\n")
        
    elif ("sleep" in text):
        print("--Going to sleep--")
        say("going to sleep")
        time.sleep(300)
        print("--Returned from sleep--\n")
        say(assistantName + "is active")
        
