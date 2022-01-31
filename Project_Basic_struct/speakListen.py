import time
from turtle import delay
from anyio import sleep
import speech_recognition as sr
'''from gtts import gTTS
from playsound import playsound
import win32com
from win32com import client'''
import os
import pyttsx3
import datetime


python = pyttsx3.init("sapi5")
voices = python.getProperty("voices")
#print(voices)
python.setProperty("voice", voices[1].id)
python.setProperty("rate", 140)


def speak(text):
    """[This function would speak aloud some text provided as parameter]

    Args:
        text ([str]): [It is the speech to be spoken]
    """    
    python.say(text)
    python.runAndWait()

def greet(g):
    if g == "start" or g == "s":
        h = datetime.datetime.now().hour
        text = ''
        if h > 12 and h < 17:
            text = "Hello ! Good Afternoon  "
        elif h < 12 and h > 0:
            text = "Hello! Good Morning  "
        elif h > 17 :
            text = "Hello! Good Evening "
        text += " I am Python, How may i help you ?"
        speak(text)    
    
    elif g == "quit" or g == "end" or g == "over" or g == "e":
        text = 'Thank you!Sir. Good Bye ! '
        speak(text)

def hear():
    """[It will process the speech of user using Google_Speech_Recognizer(recognize_google)]

    Returns:
        [str]: [Speech of user as a string in English(en - IN)]
    """    
    r = sr.Recognizer()
    """Reconizer is a class which has lot of functions related to Speech i/p and o/p.
    """
    r.pause_threshold = 1 # a pause of more than 1 second will stop the microphone temporarily
    r.energy_threshold = 300 # python by default sets it to 300. It is the minimum input energy to be considered. 
    r.dynamic_energy_threshold = True # pyhton now can dynamically change the threshold energy

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Listening...")
        #time.sleep(0.5)

        speech = r.record(source, duration = 5)  # option 
        #speech = r.listen(source)
        # convert speech to text
        try:
            print("Recognizing...")
            speech = r.recognize_google(speech)
            print(speech)
        
        except Exception as exception:
            print(exception)
            return "None"
    return speech


if __name__ == '__main__':
    print("Enter your name")
    name = hear()
    speak("Hello " + name)
    greet("s")
    greet("e")
    pass
    #hear()
    
