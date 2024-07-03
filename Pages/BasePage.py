from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
import pytest

""" This page is all pages comman page   """
""" it contain all the generic methods and utilites for all pages   """


class BasePage:
    # __int is behave a constructure function

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def do_click_force(self, by_locator):
        self.driver.execute_script("arguments[0].click();",
                                   WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)))
        # button = driver.find_element_by_xpath(by_locator)
        # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(by_locator)).click()
        # self.driver.execute_script("arguments[0].click();", button)
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_element_text_new(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_currenturl(self, currenturl):
        WebDriverWait(self.driver, 10).until(EC.url_changes(currenturl))
        return self.driver.currenturl

    def do_upload(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()
        pyautogui.write(text)
        pyautogui.press('enter')
