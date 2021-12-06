from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path = r"C:\Development\chromedriver.exe"
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser, options=chrome_options)
form_link = "https://forms.gle/W7rnKaimLpdJzthp8"
ZILLOW_SITE_LINK = "https://www.zillow.com/new-york-ny/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.86263058902944%2C%22east%22%3A-73.09328241097057%2C%22south%22%3A40.058801623497665%2C%22north%22%3A41.34677775446179%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D"
BROWSER_HEADER = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
}

response = requests.get(url=ZILLOW_SITE_LINK, headers=BROWSER_HEADER)
webpage = response.text
response.raise_for_status()

soup = BeautifulSoup(webpage, "html.parser")
listings = soup.select(".list-card-top a")
price = soup.select(".list-card-price")
address = soup.select(".list-card-addr")

final_links = [
    "https://www.zillow.com" + listing.get('href') if "https" not in listing.get('href') else listing.get('href')
    for listing in listings]

final_prices = [
    prices.getText().split("/")[0] if "/" in prices.getText() else prices.getText().split("+")[0] for prices in price]

final_addresses = [a.getText() for a in address]

for i in range(len(final_links)):
    driver.get(form_link)
    time.sleep(5)
    address_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_input.send_keys(final_addresses[i])
    price_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input.send_keys(final_prices[i])
    link_input = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input.send_keys(final_links[i])
    submit = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
    submit.click()

