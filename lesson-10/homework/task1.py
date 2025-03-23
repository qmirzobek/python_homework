import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY") 
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]
    
    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description}")
else:
    print("Error fetching weather data.")
