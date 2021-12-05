from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "dessert__lover"
USERNAME = "botfortestingg"
PASSWORD = Your password


class InstaFollower:
    def __init__(self):
        self.ser = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.ser)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(7)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]").click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        pop_up_window = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.driver.find_element(By.XPATH, "//div[@class='isgrP']")))
        for i in range(10):
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            time.sleep(3)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
