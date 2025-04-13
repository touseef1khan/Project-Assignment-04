import requests
import os

# ✅ Fetch API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather details for a given city using OpenWeather API"""

    if not API_KEY:
        return {"Error": "API key not found! Please set the OPENWEATHER_API_KEY environment variable."}

    try:
        params = {
            "q": city.strip(),
            "appid": API_KEY,
            "units": "metric"  # ✅ Temperature in Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = {
                "City": data["name"],
                "Temperature": f"{data['main']['temp']}°C",
                "Condition": data["weather"][0]["description"].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']} m/s",
                "Pressure": f"{data['main']['pressure']} hPa",
                "Visibility": f"{data.get('visibility', 'N/A')} meters"
            }
            return weather
        else:
            return {"Error": data.get("message", "City not found!")}

    except requests.exceptions.RequestException as e:
        return {"Error": f"Network error: {e}"}


# ✅ User Input with Validation
while True:
    city = input("\n🌍 Enter city name (or type 'exit' to quit): ").strip()

    if city.lower() == "exit":
        print("Goodbye! 👋")
        break

    if not city:
        print("⚠️ City name cannot be empty. Please enter a valid city name.")
        continue

    weather_info = get_weather(city)

    # ✅ Print Weather Report
    print("\n🌍 Weather Report 🌍")
    print("=" * 30)
    
    for key, value in weather_info.items():
        print(f"{key}: {value}")
    
    print("\n🔄 Want to check another city? (Press Enter to continue or type 'exit')")

