import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

INTERVAL_TIME = 60 * 10  # 10 minutes
RANDOM_INTERVAL = 1      # 1 second

options = webdriver.ChromeOptions()
options.add_argument(
    r"--user-data-dir=C:\Users\egmox\AppData\Local\Google\Chrome\User Data"
)
options.add_argument("--profile-directory=Default")
#options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

driver.get("https://www.naukrigulf.com/mnj/userProfile/myCV")

# Wait 2 seconds before starting the loop
time.sleep(5)

while True:
    try:
        try:
            edit_button = driver.find_element(
                By.CSS_SELECTOR,
                ".ng-link.edit-cta.fr"
            )
            edit_button.click()

        except NoSuchElementException:
            print("Edit button not found. Redirecting...")

            driver.get(
                "https://www.naukrigulf.com/mnj/userProfile/myCV"
            )

            time.sleep(3)

            edit_button = driver.find_element(
                By.CSS_SELECTOR,
                ".edit"
            )
            edit_button.click()

        time.sleep(1.5)

        save_button = driver.find_element(
            By.CSS_SELECTOR,
            ".ng-btn.blue"
        )
        save_button.click()

        print("Profile saved successfully")

    except Exception as e:
        print(f"Error: {e}")

    sleep_time = INTERVAL_TIME + random.randint(1, RANDOM_INTERVAL)
    print(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)