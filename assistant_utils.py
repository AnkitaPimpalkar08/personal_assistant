import pyttsx3
import speech_recognition as sr
import webbrowser
import requests
import datetime
import os

# Initialize the text-to-speech engine with adjusted settings
engine = pyttsx3.init('nsss')  # 'nsss' for macOS, 'sapi5' for Windows
engine.setProperty('rate', 160)  # Adjust the rate as needed
voices = engine.getProperty('voices')
engine.setProperty('volume', 0.8) 
engine.setProperty('voice', voices[0].id)  # You can change to voices[1].id to switch voices

def speak(audio):
    """Converts text to speech with improved clarity"""
    engine.say(audio)
    engine.runAndWait()

def take_command():
    """Takes voice input from the user and returns the recognized text as a string"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
            return "None"
        return query.lower()

def play_youtube_music(song_name):
    """Searches and plays a song on YouTube Music"""
    search_query = song_name.replace(' ', '+')
    url = f"https://music.youtube.com/search?q={search_query}"
    webbrowser.open(url)
    speak(f"Playing {song_name} on YouTube Music.")

def fetch_weather(city):
    """Fetches weather information for a specified city"""
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")  # Set your API key in environment variables
    if not api_key:
        speak("Weather API key is not set.")
        return "API key missing."
    
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"] - 273.15  # Convert from Kelvin to Celsius
        humidity = main["humidity"]
        weather_description = data["weather"][0]["description"]
        result = (f"The temperature in {city} is {temperature:.2f} degrees Celsius, "
                  f"with humidity of {humidity}% and overall {weather_description}.")
        speak(result)
        return result
    else:
        speak("City not found.")
        return "City not found."

def take_note():
    """Takes a note and saves it to a text file"""
    speak("What would you like me to write down?")
    note = take_command()
    if note != "None":
        with open('notes.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()}: {note}\n")
        speak("Note saved.")

def perform_calculation(expression):
    """Performs a simple mathematical calculation"""
    try:
        result = eval(expression)
        speak(f"The result is {result}")
        return result
    except Exception as e:
        speak("Sorry, I couldn't calculate that.")
        return None