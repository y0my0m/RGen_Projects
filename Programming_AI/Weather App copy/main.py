import requests
import json
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

#Load the Gemini API key from environment variables
GEMINI_API_KEY = os.getenv("api_key2")

client = genai.Client(api_key=GEMINI_API_KEY)

# Function to retrieve weather information
def get_weather(city_name):
    # Your OpenWeather API key
    api_key = os.getenv("api_key")  # Retrieve API key from environment variables
    
    # Constructing the API URL with the city name and API key
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    # Sending a request to the API and getting the response
    response = requests.get(weather_url)
    
    # Parsing the response JSON into a Python dictionary
    weather_info = response.json()
    
    # Checking if the city was found (API returns 'cod': 200 if successful)
    if weather_info['cod'] == 200:
        kelvin = 273  # Value to convert Kelvin to Celsius
        # Extracting relevant weather details
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        description = weather_info['weather'][0]['description']
        
        # Returning a formatted string with the weather information
        return f"Weather of {city_name}:\nTemperature: {temp}°C\nFeels like: {feels_like_temp}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {description}"
    else:
        # Return error message if city is not found
        return f"Weather for '{city_name}' not found! Please enter a valid city name."


city = input("Enter the city name: ")  # Take city name as input
weather_report = get_weather(city)  # Fetch weather information
print(weather_report)  # Print the weather report

stream = client.interactions.create(
model="gemini-3.1-flash-lite",
input="You are a weather specialist. Provide a short and simple suggestion for this weather report with a maximum of 30 make it fun with emojis: " + weather_report,
stream=True,

)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)