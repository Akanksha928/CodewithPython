import requests
import smtplib
import config
from twilio.rest import Client
my_email = "testforcode12@gmail.com"
password = "testforcode12@#"
number = "+16186032597"
MY_LAT = 13.082680
MY_LONG = 80.270721
my_phone_number = config.my_phone_num
account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token
api_key = config.OWM_api_key
parameters = {"lat": MY_LAT,
              "lon": MY_LONG,
              "appid": api_key,
              "exclude": "current,minutely,daily",
              "hourly": "hourly.weather.id"}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False

sliced_list = weather_data["hourly"][:12]
for i in range(0, 12):
    id = sliced_list[i]["weather"][0]["id"]
    if int(id) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's gonna rain today. Carry an umbrella.",
        from_="+16186032597",
        to=my_phone_number
    )
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="akanksha.xo@gmail.com",
                            msg="Subject: Rain Prediction\n\nIt's going to rain today. Carry your umbrella!")
    print(message.status)


