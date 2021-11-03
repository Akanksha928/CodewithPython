import requests
import smtplib
import time
from datetime import datetime, timezone

MY_LAT = 12.9956
MY_LONG = 80.2586
my_email = "testforcode12@gmail.com"
password = "testforcode12@#"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def iss_above_me():
    """Returns True if the ISS is above the given location"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_longitude in range(int(MY_LONG) - 5, int(MY_LONG) + 5) and iss_latitude in range(int(MY_LAT) + 5, int(MY_LAT) + 5):
        return True


def is_night_time():
    """Returns TRUE if it's night time at the given location."""
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Converting current hour to UTC as time returned by Sunrise/Sunset API is in UTC, not local
    current_hour = datetime.now(timezone.utc).hour
    if current_hour >= sunset or current_hour <= sunrise:
        return True

# Runs indefinitely while checking every 60 seconds


while True:
    time.sleep(60)
    if iss_above_me() and is_night_time():
        # Sends an email to the given e-mail ID
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="akanksha.xo@gmail.com",
                                msg=f"Subject: ISS!\n\nThe ISS is currently above you! Look up!")
