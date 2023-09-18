import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import requests  # Add this import for making HTTP requests

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.say("Alexa here")


def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'jokes' in command or 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'search' in command:
        search_query = command.replace('search', '')
        talk(f"Searching the web for {search_query}")
        pywhatkit.search(search_query)
    elif 'news' in command:
        # Add code here to fetch and read news headlines
        news_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY'
        response = requests.get(news_url)
        news_data = response.json()

        if 'articles' in news_data:
            articles = news_data['articles']
            if articles:
                talk("Here are the latest news headlines:")
                for i, article in enumerate(articles[:5]):
                    talk(f"Headline {i + 1}: {article['title']}")
        else:
            talk("Sorry, I couldn't fetch the news headlines at the moment.")

    else:
        talk('Please say the command again.')


while True:
    run_alexa()
