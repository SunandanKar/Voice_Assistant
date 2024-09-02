import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import time
import requests
import threading

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speaking rate
engine.setProperty('volume', 1.0)  # Adjust volume level

# Configure Google Generative AI
genai.configure(api_key="AIzaSyBQ2V3HfqjaN1vS7fGSHAa3YYAfqsVn-ck")  # Replace with your actual API key

# OpenWeatherMap API key
weather_api_key = "30d4741c779ba94c470ca1f63045390a"  # Replace with your actual API key

# Function to speak text aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for a specific voice command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, couldn't request results. Please check your internet connection.")
        return ""

# Function to generate a response using Google Generative AI
def generate_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Function to get weather updates
def get_weather(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={location}&appid={weather_api_key}"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()

        main_data = data["main"]
        temperature = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
        humidity = main_data["humidity"]
        weather_description = data["weather"][0]["description"]

        weather_update = (
            f"The current weather in {location} is {weather_description}. "
            f"The temperature is {temperature:.2f}°C and the humidity is {humidity}%."
        )
        return weather_update
    except (requests.RequestException, KeyError):
        return "Sorry, I couldn't retrieve the weather information."

# Function to handle the main interaction loop
def handle_interaction():
    while True:
        user_input = listen()

        if "question" in user_input:
            speak("What's your question?")
            question = listen()
            answer = generate_response(f"Answer this question: {question}")
            speak(answer)
            print(answer)
        elif "chat" in user_input:
            speak("Sure, what would you like to talk about?")
            prompt = listen()
            response = generate_response(f"Chat with user about: {prompt}")
            speak(response)
            print(response)
        elif "create email" in user_input:
            speak("Who is the recipient?")
            recipient = listen()
            speak("What is the subject?")
            subject = listen()
            speak("How should it sond like")
            body = listen()
            email_content = generate_response(f"Compose an email to {recipient} with subject '{subject}' and the content should be '{body}'")
            send_email(recipient, subject, email_content)  # Send AI-composed email
            print(email_content)
            speak("Email created successfully!")
        elif "set reminder" in user_input:
            speak("In how many seconds should I remind you?")
            seconds = listen()
            print("What should the reminder say?")
            speak("What should the reminder say?")
            message = listen()
            reminder_message = generate_response(f"Reminder message: {message}")
            threading.Thread(target=set_reminder, args=(seconds, reminder_message)).start()
            print("Reminder set successfully!")
            speak("Reminder set successfully!")
        elif "weather" in user_input:
            speak("Sure, what's the location?")
            location = listen()
            weather = get_weather(location)
            print(weather)
            speak(weather)
        elif "right passage" in user_input or "write passage" in user_input:
            speak("What should be the topic of the passage?")
            topic = listen()
            passage = generate_response(f"Write a detailed passage on the topic: {topic}")
            speak("Here is the passage:")
            print(passage)
            speak(passage)
        elif "stop" in user_input or "exit" in user_input:
            print("Goodbye")
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I cannot help with that.")

# Function to send an email (needs implementation)
def send_email(to, subject, body):
    print(f"Email sent to {to} with subject: {subject} and body: {body}")

# Function to set a reminder
from datetime import datetime, timedelta

# Function to set a reminder
def set_reminder(seconds, message):
    try:
        seconds = int(seconds)
        if seconds <= 0:
            raise ValueError("Reminder time must be positive.")
        reminder_time = datetime.now() + timedelta(seconds=seconds)
        print(f"Reminder set for {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")
        while datetime.now() < reminder_time:
            time.sleep(1)  # Sleep in small intervals to avoid high CPU usage
        speak(f"Reminder: {message}")
    except ValueError as e:
        speak(str(e))
        print(f"Error: {e}")

# Main function to activate the assistant
def main():
    speak("Give the activation code")
    while True:
        activation_keyword = listen()
        if "Javis" in activation_keyword:
            speak("Yes Boss")
            handle_interaction()
        else:
            print("Waiting for activation...")

if __name__ == "__main__":
    main()
