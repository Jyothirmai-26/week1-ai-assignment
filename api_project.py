import requests
city = "Guntur"
url = f"https://wttr.in/{city}?format=j1"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    current = data["current_condition"][0]
    temperature = current["temp_C"]
    humidity = current["humidity"]
    wind_speed = current["windspeedKmph"]
    weather_desc = current["weatherDesc"][0]["value"]
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")
    print(f"Weather: {weather_desc}")

except requests.exceptions.RequestException as e:
    print("Error fetching weather data:", e)