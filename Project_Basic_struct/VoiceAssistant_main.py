from speakListen import *
from voice_recorder import *
from websiteWork import *
from textRead import *
from essay import *
from menu import *
from speechtotext import *
from TextTospeech import *


def main():
    start = 0
    if start == 0:
        print("\nSay \"Hello Python\" to activate the Voice Assistant!")
        start += 1
    while True:
        # print("Say \"Python\" to activate the Voice Assistant!")
        q = hear().lower()
        if "python" in q:
            greet("start")
            print_menu()
            while True:
                
                query = hear().lower()
                if "close" in query:
                    greet("end")
                    return 0
                if "search on google" in query or "search google" in query or "google" in query:
                    google_search()
                    break
        elif "close" in q:
            return 0
        else:
            continue

main()