import requests
import json

def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=en&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data. Please check the city name or API key.")
        return None

def display_weather_info(data):
    if data:
        city_name = data["name"]
        country = data["sys"]["country"]
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        min_temperature = data["main"]["temp_min"]
        max_temperature = data["main"]["temp_max"]
        feels_like_temperature = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        print(f"Weather in {city_name}, {country}:")
        print(f"Description: {weather_description.title()}")
        print(f"Temperature: {temperature}°C")
        print(f"Min Temperature: {min_temperature}°C")
        print(f"Max Temperature: {max_temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Feels Like: {feels_like_temperature}°C")
    else:
        print("No weather data available.")

def main():
    api_key = "80c8b2b0d8236feca8f2b64537f1edb5"
    
    while True:
        city = input("Enter the city to check the weather (or type 'quit'or 'q' to exit): ").strip().lower()
        if city == "quit"or "q":
            break
        
        weather_data = get_weather_data(city, api_key)
        display_weather_info(weather_data)

if __name__ == "__main__":
    main()
