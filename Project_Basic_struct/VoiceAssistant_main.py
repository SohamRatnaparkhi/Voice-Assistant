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
    end = 0
    if start == 0:
        print("\nSay \"Hello Python\" to activate the Voice Assistant!")
        start += 1
    while True:
        # print("Say \"Python\" to activate the Voice Assistant!")

        q = hear().lower()
        if "close" in q:
            greet("end")
            exit(0)
        if "hello python" in q:
            greet("start")
            print_menu()
            while True:
                
                query = hear().lower()
                if "close" in query:
                    greet("end")
                    end += 1
                    return 0
                elif "search on google" in query or "search google" in query or "google" in query:
                    google_search()
                    break
                elif "search on wikipedia" in query or "search wikipedia" in query or "wikipedia" in query:
                    wiki_search()
                    break
                elif "word" in query:
                    ms_word()
                    break
                elif "book" in query:
                    pdf_read()
                    break
                elif "speech to text" in query:
                    big_text()

        elif "close" in q:
            return 0
        else:
            continue

main()