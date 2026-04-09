import json
import os
from urllib import error, parse, request

from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
render_template

app = Flask(__name__)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route("/")
def home():
    return 'Hello, World!'

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    if name is None:
        name = "World"
    name = name.capitalize()
    return render_template("hello.html", name=name)


# create another route that shows the current weather in any city
# /weather/<city>
@app.route("/weather/<city>")
def weather(city):
    if not OPENWEATHER_API_KEY:
        return (
            "Set the OPENWEATHER_API_KEY environment variable first.",
            500,
        )

    city_name = city.strip()
    query = parse.urlencode(
        {
            "q": city_name,
            "appid": OPENWEATHER_API_KEY,
            "units": "imperial",
        }
    )
    url = f"https://api.openweathermap.org/data/2.5/weather?{query}"

    try:
        with request.urlopen(url, timeout=10) as response:
            weather_data = json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        if exc.code == 404:
            return f"Could not find weather for {city_name}.", 404
        return f"Weather service error: {exc.reason}", 502
    except error.URLError:
        return "Could not connect to the weather service.", 502

    description = weather_data["weather"][0]["description"].capitalize()
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]

    return (
        f"<h1>Weather in {weather_data['name']}</h1>"
        f"<p>{description}</p>"
        f"<p>Temperature: {temperature:.0f} F</p>"
        f"<p>Feels like: {feels_like:.0f} F</p>"
    )


if __name__ == '__main__':
    app.run(debug=True)

