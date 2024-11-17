Personal Assistant Project
This project is a simple voice-activated personal assistant built using Python. It can perform various tasks such as taking notes, playing music from YouTube Music, fetching weather information, performing basic calculations, and more.
Features
•	- Text-to-Speech: Converts text into speech using the pyttsx3 library.
•	- Voice Command Recognition: Listens for and recognizes voice commands using speech_recognition.
•	- Weather Information: Fetches weather data for a specified city using the OpenWeatherMap API.
•	- Music Playback: Plays music on YouTube Music based on user commands.
•	- Note-Taking: Allows the user to take notes, which are saved to a text file.
•	- Basic Calculations: Performs simple mathematical calculations.
Requirements
Python 3.7+
Libraries used:
•	- pyttsx3
•	- speech_recognition
•	- webbrowser
•	- requests
•	- datetime
Installation
Clone the repository:
git clone https://github.com/AnkitaPimpalkar08/personal_assistant.git
Navigate to the project directory:
cd personal_assistant
Create a virtual environment (optional but recommended):
python -m venv venv
Activate the virtual environment:
- For Windows: venv\Scripts\activate
- For macOS/Linux: source venv/bin/activate
Install the required packages:
pip install -r requirements.txt
Usage
Run the main script:
python main.py
Follow the voice prompts or type commands to interact with the assistant.
Configuration
Weather API Key: Set your OpenWeatherMap API key as an environment variable:
export OPENWEATHERMAP_API_KEY="your_api_key_here"
Additional Configuration: Ensure your microphone is configured correctly for voice commands. Make sure you have an internet connection for fetching weather data and playing music.
Contributing
Contributions are welcome! Please fork the repository and use a feature branch for your changes. Pull requests are warmly welcome.
License
MIT License
Contact
For issues or feature requests, please reach out to apimpalkar707@gmail.com.
![image](https://github.com/user-attachments/assets/af2f8fd8-b7c0-4350-9eb3-bdd6ffa267f2)
