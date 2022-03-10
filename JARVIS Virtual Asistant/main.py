# This is a sample Python script.

# ______________________-MODULES-______________________ #
from datetime import datetime as dt
from random import choice, randint
from os import listdir, startfile, system, popen, walk
import webbrowser as web
import pyttsx3
from json import load
from configparser import ConfigParser
from speech_recognition import Recognizer, Microphone
from wikipedia import summary

# ______________________VARIABLES______________________ #
# [loading phrases from json file...]
with open('phrases.json') as json:
    phrase = load(json)

# [loading settings form ini file...]
config = ConfigParser()
config.read("settings.ini")

# // Basic:
_assistant = config.get('name', 'assistant')
_operator = config.get('name', 'operator')

# // Path:
# / Program
_pycharm = ""
_vscode = ""
_word = ""
_excel = ""
_powerpnt = ""
_photoshop = ""
_illustrator = ""
_indesign = ""
_audition = ""
_premierpro = ""
_flstudio = ""

# / Music:

engine = pyttsx3.init('sapi5')
# ______________________FUNCTIONS______________________ #


def say(what_to):
    engine.say(what_to)
    print(what_to)
    engine.runAndWait()


def wish():
    hour = dt.now().hour

    if 12 > hour >= 0:
        return "Good Morning!"
    elif 17 > hour >= 12:
        return "Good Afternoon!"
    else:
        return "Good Evening!"


def listen():
    with Microphone() as source:
        print("Listening ...")
        Recognizer().pause_threshold = 2
        voice = Recognizer().listen(source)

    try:
        print("Recognizing ...")
        query = Recognizer().recognize_google(voice, language='en-in')
        print(f">_ {query}\n")

    except Exception as e:
        print("Sorry, say that again please ...")
        return None

    return query


# ______________________MAIN CODE______________________ #

if __name__ == '__main__':
    say(f"{choice(phrase['wish']['hello'])} {_operator}, {wish()}")

    # """
    while 1:
        query = listen().lower()

        if 'quit' or 'exit' or 'close' in query:
            exit()
        elif 'about' in query:
            say("Searching wikipedia, please wait ...")

            question = query.replace('about', '')
            result = summary(question, sentences=2)

            say(f"according to wikipedia, {result}")
        elif 'start' in query:
            # have to add exception with a program list possibly
            say(choice(phrase['response']['ok']))
            system(f"start {query.replace('start', '')}")
        elif 'open' or 'visit' in query:
            # list of frequently visited sites have to be added
            say(choice(phrase['response']['ok']))
            web.open(url=f"{query.replace('open', '')}.com")
        else:
            continue
    # """


