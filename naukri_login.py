#! python3
# -*- coding: utf-8 -*-
"""Naukri login flow module."""

import logging
import os
import sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import constants

# Naukri login configuration
username = constants.USERNAME
password = constants.PASSWORD
NaukriURL = constants.NAUKRI_LOGIN_URL
headless = True

logging.basicConfig(
    level=logging.INFO,
    filename="naukri_login.log",
    format="%(asctime)s    : %(message)s",
)

os.environ["WDM_LOCAL"] = "1"
os.environ["WDM_LOG_LEVEL"] = "0"


def log_msg(message):
    """Print to console and log message."""
    print(message)
    logging.info(message)


def catch(error):
    """Catch exceptions and log error details."""
    _, _, exc_tb = sys.exc_info()
    line_no = str(exc_tb.tb_lineno)
    msg = "%s : %s at Line %s." % (type(error), error, line_no)
    print(msg)
    logging.error(msg)


def getObj(locatorType):
    """Map locator types to Selenium By selectors."""
    return {
        "ID": By.ID,
        "NAME": By.NAME,
        "XPATH": By.XPATH,
        "TAG": By.TAG_NAME,
        "CLASS": By.CLASS_NAME,
        "CSS": By.CSS_SELECTOR,
        "LINKTEXT": By.LINK_TEXT,
    }.get(locatorType.upper(), By.ID)


def is_element_present(driver, how, what):
    """Return True if the element exists."""
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True


def GetElement(driver, elementTag, locator="ID"):
    """Wait for element and return it when available."""
    try:
        _by = getObj(locator)
        if is_element_present(driver, _by, elementTag):
            return WebDriverWait(driver, 15).until(
                lambda d: d.find_element(_by, elementTag)
            )
        log_msg("Element not found with %s : %s" % (locator, elementTag))
    except Exception as e:
        catch(e)
    return None


def WaitTillElementPresent(driver, elementTag, locator="ID", timeout=30):
    """Wait till the element is present on page."""
    driver.implicitly_wait(0)
    locator = locator.upper()
    result = False

    for _ in range(timeout):
        time.sleep(0.99)
        try:
            if is_element_present(driver, getObj(locator), elementTag):
                result = True
                break
        except Exception:
            pass

    if not result:
        log_msg("Element not found with %s : %s" % (locator, elementTag))
    driver.implicitly_wait(3)
    return result


def LoadNaukri(headless):
    options = webdriver.ChromeOptions()

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--window-size=1920,1080")

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=ChromeService(),
        options=options
    )

    driver.implicitly_wait(5)

    driver.get(NaukriURL)

    log_msg(f"URL: {driver.current_url}")
    log_msg(f"Title: {driver.title}")

    with open("page_dump.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    return driver


def naukriLogin():
    """Perform login to Naukri and return the browser driver."""
    status = False
    driver = None
    username_locator = "usernameField"
    password_locator = "passwordField"
    login_btn_locator = "//*[@type='submit' and normalize-space()='Login']"
    skip_locator = "//*[text() = 'SKIP AND CONTINUE']"
    close_locator = "//*[contains(@class, 'cross-icon') or @alt='cross-icon']"

    try:
        driver = LoadNaukri(headless)
        log_msg(driver.title)
        if "naukri.com" in driver.title.lower():
            log_msg("Website Loaded Successfully.")

        email_field_element = None
        if is_element_present(driver, By.ID, username_locator):
            email_field_element = GetElement(driver, username_locator, locator="ID")
            time.sleep(1)
            pass_field_element = GetElement(driver, password_locator, locator="ID")
            time.sleep(1)
            login_button = GetElement(driver, login_btn_locator, locator="XPATH")
        else:
            log_msg("None of the elements found to login.")

        if email_field_element is not None:
            email_field_element.clear()
            email_field_element.send_keys(username)
            time.sleep(1)
            pass_field_element.clear()
            pass_field_element.send_keys(password)
            time.sleep(1)
            login_button.send_keys(Keys.ENTER)
            time.sleep(3)

            if WaitTillElementPresent(driver, close_locator, "XPATH", 10):
                GetElement(driver, close_locator, "XPATH").click()
            if WaitTillElementPresent(driver, skip_locator, "XPATH", 5):
                GetElement(driver, skip_locator, "XPATH").click()

            if WaitTillElementPresent(driver, "ff-inventory", locator="ID", timeout=40):
                if GetElement(driver, "ff-inventory", locator="ID"):
                    log_msg("Naukri Login Successful")
                    status = True
                else:
                    log_msg("Unknown Login Error")
            else:
                log_msg("Unknown Login Error")

    except Exception as e:
        catch(e)
    return status, driver


def main():
    status, driver = naukriLogin()
    if status:
        log_msg("Login flow completed successfully.")
    else:
        log_msg("Login flow failed.")
    if driver is not None:
        driver.quit()


if __name__ == "__main__":
    main()
