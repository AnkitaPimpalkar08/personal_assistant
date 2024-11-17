from assistant_utils import speak, take_command, play_youtube_music, fetch_weather, take_note, perform_calculation

def main():
    """Main function to handle user commands"""
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        query = take_command()

        if 'time' in query:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif 'play music' in query:
            speak("Which song would you like to play?")
            song_name = take_command()
            if song_name != "None":
                play_youtube_music(song_name)

        elif 'weather' in query:
            speak("Which city's weather would you like to know?")
            city = take_command()
            if city != "None":
                fetch_weather(city)

        elif 'note' in query or 'write this down' in query:
            take_note()

        elif 'calculate' in query or 'perform calculation' in query:
            speak("Please say the mathematical expression.")
            expression = take_command()
            if expression != "None":
                perform_calculation(expression)

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("I am not sure how to help with that. Please try a different command.")

if __name__ == "__main__":
    main()