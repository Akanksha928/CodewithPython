# Program saves job profiles instead of applying
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = r"C:\Development\chromedriver.exe"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.get("https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Bangalore%20Urban%2C%20Karnataka%2C%20India&geoId=112376381&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
driver.maximize_window()
driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click()
time.sleep(5)

email = driver.find_element(By.XPATH, "//*[@id='username']")
email.send_keys("akanksha.xo@gmail.com")
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("anushka555")

driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button").click()
time.sleep(7)
jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for job in jobs:
    job.click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "jobs-save-button").click()

