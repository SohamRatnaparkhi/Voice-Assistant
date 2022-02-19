from gtts import gTTS
from playsound import playsound
import win32com
from win32com import client
import os

def tts():
    audio = 'speech.mp3'
    language = 'en'
    sentence = input("Enter the text to be spoken :- ")
    # choice = input("Do you want a male voice or a female voice ? (M/F) ")
    # choice = choice.lower()
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    # #if choice == 'f':
    #     sp = gTTS( text = sentence, lang = language, slow = False )
    #     sp.save(audio)
    #     playsound(audio)  
    # elif choice == 'm':
    sp = speaker.Speak(sentence)
    

