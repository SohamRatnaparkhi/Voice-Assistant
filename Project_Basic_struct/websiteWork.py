from speakListen import greet, hear
from speakListen import speak

""" 1. speakListen.speak(text)
    2. speakListen.greet()
    3. speakListen.hear()
"""
import wikipedia
import webbrowser


def google_search():
    """[Goes to google and searches the website asked by the user]
    """
    google_search_link = "https://www.google.co.in/search?q="
    google_search = "What do you want me to search on Google? Please tell me the exact sentence or word to Search."
    print(google_search)
    speak(google_search)
    
    query = hear()

    if query != "None":
        webbrowser.open(google_search_link+query)

def wiki_search():
    """[Speak out the summary in wikipedia and going to the website according to user's choice.]
    """    
    wiki_search = "What do you want me to search on Wikipedia? Please tell me the exact sentence or word to Search."
    wiki_search_link = "https://en.wikipedia.org/wiki/"
    
    print(wiki_search)
    speak(wiki_search)

    query = hear()

    if query is not "None":
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

        print("Do you want me to open the Wikipedia page?")
        speak("Do you want me to open the Wikipedia page?")
        q = hear().lower()

        if "yes" in q or "okay" in q or "okay" in q:
            print(wiki_search_link + query)
            webbrowser.open(wiki_search_link + query)

#wiki_search()
#google_search()
