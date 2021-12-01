from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = r"C:\Development\chromedriver.exe"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
five_min = time.time() + 60*5
cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# Get IDs of upgrades
upgrade_item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()
    # Every 5 secs
    if time.time() > timeout:
        # Get current cookie count
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money_element = money.replace(",", "")
        cookie_count = int(money)

        # Get prices of upgrades
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for item in all_prices:
            element = item.text
            if element != "":
                price = item.text.split("-")[1]
                item_prices.append(int(price.replace(",", "")))

        # Create dictionary of store items and prices
        cookie_upgrades = dict(zip(upgrade_item_ids, item_prices))

        # Find the upgrades that are currently affordable
        affordable_upgrades = {}
        for item, cost in cookie_upgrades.items():
            if cost < cookie_count:
                affordable_upgrades[cost] = item
        print(cookie_count)

        # Purchase the most expensive affordable upgrade
        highest_affordable_upgrade = max(affordable_upgrades)
        id_of_upgrade = affordable_upgrades[highest_affordable_upgrade]
        driver.find_element(By.ID, id_of_upgrade).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > five_min:
            cps = driver.find_element(By.ID, "cps").text
            print(cps)
            break
