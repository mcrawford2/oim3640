import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "").strip()

if not OPENWEATHER_API_KEY:
    print("Set OPENWEATHER_API_KEY in your .env file or environment variables.")
else:
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q=Boston&appid={OPENWEATHER_API_KEY}&units=imperial"
    )
    response = requests.get(url, timeout=10)
    data = response.json()

    if response.ok and "main" in data and "weather" in data and data["weather"]:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print("Boston weather")
        print(f"Temperature: {temperature}°F")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        message = data.get("message", response.text)
        print(f"OpenWeather error ({response.status_code}): {message}")

#invalid key error: OpenWeather error (401): Invalid API key. Please see http://openweathermap.org/faq#error401 for more info.