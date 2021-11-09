import requests
from datetime import datetime

APP_ID = "9a262e7f"
API_KEY = "0e030b80078b4f19329603d833571792"

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/df0a55feab958ca2c40ca30f5fb58800/workoutLog/workouts"

date = datetime.now()

exercise_parameters = {
    "query": input("What exercise did you do today?"),
    "gender": "female",
    "weight_kg": 48,
    "height_cm": 154,
    "age": 21,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

response = requests.post(url=api_endpoint, json=exercise_parameters, headers=headers)
data = response.json()

sheety_params = {
    "workout":
        {
            "date": date.strftime("%d/%m/%Y"),
            "time": date.strftime("%H:%M:%S"),
            "exercise": data["exercises"][0]["name"].title(),
            "duration": int(data["exercises"][0]["duration_min"]),
            "calories": int(data["exercises"][0]["nf_calories"]),
        }
}
sheet_response = requests.post(url=sheety_endpoint, json=sheety_params)
