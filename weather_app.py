from flask import Flask, render_template, request, flash
import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Get current weather data for the selected city.
def get_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use Celsius
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=5)
        
        if response.status_code == 200:
            return response.json()
        
        elif response.status_code == 404:
            return None
        
        else:
            return None
    
    except requests.exceptions.Timeout:
        return None
    
    except requests.exceptions.RequestException:
        return None


# Extract only the weather details needed for display.
def parse_weather_data(api_response):
    weather_data = {
        "city": api_response.get("name", "Unknown"),
        "country": api_response.get("sys", {}).get("country", "??"),
        "temperature": round(api_response.get("main", {}).get("temp", 0)),
        "feels_like": round(api_response.get("main", {}).get("feels_like", 0)),
        "description": api_response.get("weather", [{}])[0].get("description", "").title(),
        "icon": api_response.get("weather", [{}])[0].get("icon", "01d"),
        "humidity": api_response.get("main", {}).get("humidity", 0),
        "wind_speed": round(api_response.get("wind", {}).get("speed", 0), 1),
        "pressure": api_response.get("main", {}).get("pressure", 0)
    }
    
    # Build the weather icon URL from the icon code.
    weather_data["icon_url"] = f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png"
    
    return weather_data


# Flask app setup
app = Flask(__name__)
app.secret_key = "weather-dashboard-secret-key-2026"

# Load the API key from the environment file.
API_KEY = os.getenv("OPENWEATHER_API_KEY")


# Show the search page and handle weather searches.
@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        
        if not city:
            error = "Please enter a city name"
        
        else:
            api_response = get_weather_data(city, API_KEY)
            
            if api_response:
                weather = parse_weather_data(api_response)
            else:
                error = "City not found. Please check the spelling and try again."
    
    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
