import urllib.request
import json

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    with urllib.request.urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))

    current = data["current_condition"][0]

    temperature = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    humidity = current["humidity"]
    weather = current["weatherDesc"][0]["value"]

    print("\n🌤️ Weather Report")
    print("-------------------")
    print("City:", city)
    print("Weather:", weather)
    print("Temperature:", temperature, "°C")
    print("Feels Like:", feels_like, "°C")
    print("Humidity:", humidity, "%")

except Exception:
    print("❌ Could not get weather data.")
    print("Please check your internet connection and city name.")