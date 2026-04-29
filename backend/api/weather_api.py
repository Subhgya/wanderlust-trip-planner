import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url)
        data = res.json()

        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except:
        return {
            "temperature": "N/A",
            "description": "Unavailable"
        }