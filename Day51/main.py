from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Development\chromedriver.exe"

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = "@botfortestingg"
TWITTER_PASSWORD = "anushka555"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.ser = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.ser)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(50)
        self.down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text
        # print(self.down)
        # print(self.up)

    def tweet_to_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(6)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div").click()
        time.sleep(10)
        username = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(6)
        password = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        tweet_box = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        tweet_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} mbps down and {self.up} mbps up when I pay for {PROMISED_DOWN}mbps and {PROMISED_UP}mbps up?")
        tweet_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
        tweet_button.click()
        time.sleep(3)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if int(float(bot.up)) < PROMISED_UP or int(float(bot.down)) < PROMISED_DOWN:
    bot.tweet_to_provider()
