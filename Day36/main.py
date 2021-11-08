import requests
import smtplib
my_email = "testforcode12@gmail.com"
password = "testforcode12@#"
api_key = "VCZST67HN0JFHY6V"
news_api_key = "d6767f5af02643ce8f256c384e848fb0"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,
}

parameters_for_news = {
    'q': COMPANY_NAME,
    'pageSize': 10,
    'apiKey': news_api_key,
}

response_for_stock = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response_for_stock.raise_for_status()
data = response_for_stock.json()["Time Series (Daily)"]
dict_data = [value for (key, value) in data.items()]

yesterday_price = dict_data[0]['4. close']
previous_day_price = dict_data[1]['4. close']

difference = float(yesterday_price) - float(previous_day_price)
diff_percent = (abs(difference)/float(yesterday_price))*100

up_down = None
if difference > 0:
    up_down = "is up by"
else:
    up_down = "is down by"

# Checking if stock risen/fallen beyond 5%
if diff_percent >= 5:
    response_for_news = requests.get(url='https://newsapi.org/v2/everything?', params=parameters_for_news)
    response_for_news.raise_for_status()
    data = response_for_news.json()

    news_list = []
    for i in range(1, 4):
        news_list.append(data["articles"][i]["title"])

    for i in range(0, 3):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="akanksha.xo@gmail.com",
                                msg=f"Subject: Tesla Inc {up_down} {round(diff_percent, 2)}%\n\nHeadline: "
                                    f"{news_list[i]}")

