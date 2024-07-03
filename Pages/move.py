import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import Testdata


class Move(BasePage):
    GOTOPROFILE = (
        By.XPATH, "//div[@routerlink='/profiles']")
    MOVETAB = (By.XPATH, "//div[@id='mat-tab-label-0-5']")
    ADDNEW = (By.XPATH, "//button[@class='mat-focus-indicator new-button mat-raised-button mat-button-base']")
    PROFILENAME = (By.XPATH, "//input[@data-placeholder='Profile Name']")
    MOVEMETHOD = (By.XPATH, "//mat-expansion-panel/div/div/div/div[1]/div[2]/mat-form-field/div/div[1]/div/mat-select")
    MESSAGE = (By.XPATH, "//simple-snack-bar/span")
    SPEEDLIMIT = (
    By.XPATH, "//mat-accordion/mat-expansion-panel/div/div/div/div[1]/div[3]/mat-form-field/div/div[1]/div/mat-select")
    CHECKOVERWRITE = (By.XPATH, "//mat-expansion-panel/div/div/div/div[2]/div/mat-checkbox")
    SUBMITBUTTON=(By.XPATH,"//button[@class='mat-focus-indicator action-button-update-global mat-raised-button mat-button-base']")

    def __init__(self, driver):
        super(Move, self).__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    def create_moveprofile(self, profilename, movevalue, isoverwrite,valuesync):
        self.do_click(self.GOTOPROFILE)
        self.do_click(self.MOVETAB)
        self.hard_refresh()
        self.hard_refresh()
        self.do_click(self.MOVETAB)
        # self.execute_script("location.reload(true);")
        self.do_click(self.ADDNEW)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_click(self.MOVEMETHOD)
        MOVEMETHODVALUE = (By.XPATH, f"//span[normalize-space()='{movevalue}']")
        self.do_click(MOVEMETHODVALUE)
        if MOVEMETHODVALUE == 'rsync':
            RSYNCOPTIONVAL=(By.XPATH,f"//span[@class='mat-option-text'][normalize-space()='{valuesync}']")
            self.do_click(self.SPEEDLIMIT)
            self.do_click(RSYNCOPTIONVAL)
        if isoverwrite:
            self.do_click(self.CHECKOVERWRITE)
        self.do_click(self.SUBMITBUTTON)
        if self.is_visible(self.MESSAGE):
            return self.get_element_text(self.MESSAGE)
