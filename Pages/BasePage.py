from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
import pytest

""" This page is all pages common page   """
""" It contains all the generic methods and utilities for all pages   """


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except Exception as e:
            print(f"Failed to click on element: {e}")

    def is_checkbox_checked(self, by_locator):
        try:
            checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            return checkbox.is_selected()
        except Exception as e:
            print(f"Failed to determine checkbox state: {e}")
            return False

    def hard_refresh(self):
        try:
            self.driver.execute_script("location.reload(true);")
            return True
        except Exception as e:
            print(f"Failed to perform hard refresh: {e}")
            return False

    def do_clear(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
        except Exception as e:
            print(f"Failed to clear element: {e}")

    def do_click_force(self, by_locator):
        try:
            self.driver.execute_script(
                "arguments[0].click();",
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
            )
        except Exception as e:
            print(f"Failed to force click on element: {e}")

    def do_send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except Exception as e:
            print(f"Failed to send keys to element: {e}")

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except Exception as e:
            print(f"Failed to get text of element: {e}")
            return None

    def get_element_text_new(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.get_attribute("innerText")
        except Exception as e:
            print(f"Failed to get attribute text of element: {e}")
            return None

    def is_enabled(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except Exception as e:
            print(f"Failed to check if element is enabled: {e}")
            return False

    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except Exception as e:
            print(f"Failed to check if element is visible: {e}")
            return False

    def get_title(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
            return self.driver.title
        except Exception as e:
            print(f"Failed to get page title: {e}")
            return None

    def get_currenturl(self, currenturl):
        try:
            WebDriverWait(self.driver, 10).until(EC.url_changes(currenturl))
            return self.driver.current_url
        except Exception as e:
            print(f"Failed to get current URL: {e}")
            return None

    def do_upload(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()
            pyautogui.write(text)
            pyautogui.press('enter')
        except Exception as e:
            print(f"Failed to upload file: {e}")
