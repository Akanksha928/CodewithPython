import requests
import smtplib
from pprint import pprint
from bs4 import BeautifulSoup

my_email = "testforcode12@gmail.com"
my_password = "testforcode12@#"
target_price = 3000

URL = "https://www.amazon.in/Kerashine-Straightener-Thermoprotect-Technology-Keratin-Infused/dp/B086XTM88X/ref=sr_1_7" \
      "?crid=DGL0TXMJLRPK&keywords=philips+hair+straighteners&qid=1637664366&sprefix=philips+hair+stariaghtner%2Caps" \
      "%2C324&sr=8-7 "
response = requests.get(url=URL,
                        headers=
                        {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                          "like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                            "Accept-Language": "en-US,en;q=0.9"})
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
data = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text()
price = data.split("₹")[1]
price = price.replace(',', '')
current_price = int(float(price))

if current_price <= target_price:
    message = f"Subject: Price Drop!\n\nThe PHILIPS Bhs378/10 Kerashine Straightener (Pink) is now at Rs.{current_price}. Grab it now before the price increases again!"
    message = message.encode("ascii", errors="ignore")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="akanksha.xo@gmail.com",
                            msg=message)

