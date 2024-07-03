from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import Testdata


class Main(BasePage):
    GOTOCUSTOMER=(By.XPATH,"//button[@class='mat-focus-indicator show-dashboard-button mat-flat-button mat-button-base']")
    ADDCUSTOMER=(By.XPATH,"//button[@class='mat-tooltip-trigger add-customer-button']")
    NAME=(By.XPATH,"//input[@name='name']")
    USERNAME=(By.XPATH,"//input[@name='username']")
    EMAILID=(By.XPATH,"//input[@name='email_id']")
    SUBMITBUTTON = (By.XPATH,"//button[@id='saveButton']")
    MESSAGE = (By.XPATH, "//simple-snack-bar/span")


    def __init__(self, driver):
        super(Main, self).__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def create_customer(self,name,username,emailid):
        self.do_click(self.GOTOCUSTOMER)
        self.do_click(self.ADDCUSTOMER)
        self.do_send_keys(self.NAME,name)
        self.do_send_keys(self.USERNAME,username)
        self.do_send_keys(self.EMAILID,emailid)
        self.do_click(self.SUBMITBUTTON)
        if self.is_visible(self.MESSAGE):
            return self.get_element_text(self.MESSAGE)

