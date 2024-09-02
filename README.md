# Voice Assistant with AI and Weather Integration

This repository contains a Python-based voice assistant project that leverages various APIs, such as Google Generative AI and OpenWeatherMap, to perform a wide range of tasks, including answering questions, engaging in conversations, generating emails, setting reminders, and providing weather updates.

## Repository Structure

- **`README.md`**: This file, which provides an overview of the project, setup instructions, usage guidelines, and other relevant information.
- **`VoiceAsst.py`**: The main Python script that contains the implementation of the voice assistant, integrating various APIs and functionalities.

## Features

- **Voice Command Recognition**: Listens for specific voice commands using speech recognition.
- **Text-to-Speech Integration**: Provides spoken feedback using the `pyttsx3` library.
- **AI-Powered Responses**: Uses Google Generative AI to generate intelligent responses to user queries and prompts.
- **Weather Updates**: Retrieves real-time weather information for any location using the OpenWeatherMap API.
- **Email Composition**: Automatically composes emails based on user input. (Note: Email sending needs further implementation.)
- **Reminders**: Sets and manages voice-activated reminders for specified intervals.
  
## Prerequisites

- Python 3.7 or later.
- Required Python libraries:
  - `SpeechRecognition`
  - `pyttsx3`
  - `requests`
  - `google-generativeai`
- Microphone access for voice commands.
- API keys:
  - [Google Generative AI](https://cloud.google.com/genai)
  - [OpenWeatherMap](https://openweathermap.org/api)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SunandanKar/Voice_Assistant.git
   cd Voice_Assistant
   ```

2. **Install the required dependencies:**
   ```bash
   pip install SpeechRecognition pyttsx3 requests google-generativeai
   ```

3. **Configure API keys:**
   - Replace the API key in `genai.configure(api_key="YOUR_API_KEY")` in `VoiceAsst.py` with your Google Generative AI API key.
   - Replace the `weather_api_key` in `VoiceAsst.py` with your OpenWeatherMap API key.

## Usage

1. **Run the application:**
   ```bash
   python VoiceAsst.py
   ```

2. **Activate the assistant:**  
   Speak the activation keyword "Friday" to start interacting with the assistant.

3. **Supported Commands:**
   - **Ask a question:** "Question."
   - **Start a chat:** "Chat."
   - **Create an email:** "Create email."
   - **Set a reminder:** "Set reminder."
   - **Get weather information:** "Weather."
   - **Request a passage:** "Write passage."
   - **Stop the assistant:** "Stop" or "Exit."

## Customization

- **Voice Settings:** Adjust speaking rate and volume in the text-to-speech engine settings in `VoiceAsst.py`.
- **Weather API Configuration:** Ensure your OpenWeatherMap API key is correctly set.
- **Generative AI Configuration:** Make sure you have a valid Google Generative AI API key.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your proposed changes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
