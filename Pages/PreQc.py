import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import Testdata


class PreQc(BasePage):
    GOTOPROFILE = (By.XPATH, "//div[@routerlink='/profiles']")
    MOVETAB = (By.XPATH, "//div[@id='mat-tab-label-4-0']")
    MESSAGE = (By.XPATH, "//simple-snack-bar/span")
    ADDNEW = (By.XPATH, "//button[@class='mat-focus-indicator new-button mat-raised-button mat-button-base']")
    PROFILENAME = (By.XPATH, "//input[@data-placeholder='Profile Name']")
    CHECKSUMVALIDATIONMETHOD = (By.XPATH, "//mat-expansion-panel/div/div/div/div[1]/div[2]/mat-form-field/div/div[1]/div/mat-select")
    CHECKSUMERROR = (By.XPATH, "//input[@data-placeholder='Custom Error Check']")
    IGNORECUSOM = (By.XPATH, "//input[@data-placeholder='Ignore Custom Error']")
    REMARK = (By.XPATH, "//input[@data-placeholder='Enter Remarks']")
    CHECKMETADATAERROR = (By.XPATH, "//mat-expansion-panel/div/div/div/div[2]/div[1]/mat-checkbox")
    CHECKMETADATAWARNING = (By.XPATH, "//mat-accordion/mat-expansion-panel/div/div/div/div[2]/div[2]/mat-checkbox")
    CHECKSUMMETHODENABLE = (By.XPATH, "//mat-expansion-panel/div/div/div/div[1]/mat-checkbox/label")
    SUBMITBUTTON = (By.XPATH, "//button[@class='mat-focus-indicator action-button-update-global mat-raised-button mat-button-base']")
    CONFORMATIONBUTTON = (By.XPATH, "//div[@class='cdk-overlay-container']//button[2]")

    def __init__(self, driver):
        super(PreQc, self).__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    def Create_validation_check_Preqcprofile(self, profilename, checksummethoenable, valueofchecksum, customererro,
                                             ignanorsum, remark, metadatwerning, metadataerror):
        try:
            self.do_click(self.GOTOPROFILE)
            self.hard_refresh()
            self.hard_refresh()
            self.do_click(self.ADDNEW)
            self.do_send_keys(self.PROFILENAME, profilename)
            if checksummethoenable:
                time.sleep(5)
                self.do_click(self.CHECKSUMMETHODENABLE)
                time.sleep(5)
                self.do_click(self.CHECKSUMVALIDATIONMETHOD)
                MOVEMETHODVALUE = (By.XPATH, f"//span[normalize-space()='{valueofchecksum}']")
                self.do_click(MOVEMETHODVALUE)
            self.do_send_keys(self.CHECKSUMERROR, customererro)
            self.do_send_keys(self.IGNORECUSOM, ignanorsum)
            self.do_send_keys(self.REMARK, remark)
            if metadataerror:
                self.do_click(self.CHECKMETADATAERROR)
            if metadatwerning:
                self.do_click(self.CHECKMETADATAWARNING)
            self.do_click(self.SUBMITBUTTON)
            if self.is_visible(self.MESSAGE):
                return self.get_element_text(self.MESSAGE)
        except Exception as e:
            print(f"An error occurred: {e}")

    def Update_Preqcprofile(self, profilename, checksummethoenable, valueofchecksum, customererro, ignanorsum, remark,
                            metadatwerning, metadataerror, updateprofilename):
        try:
            self.do_click(self.GOTOPROFILE)
            self.hard_refresh()
            self.hard_refresh()
            MOVEMETHODVALUE = (By.XPATH, f"//span[normalize-space()='{updateprofilename}']")
            self.do_click(MOVEMETHODVALUE)
            self.do_send_keys(self.PROFILENAME, profilename)
            if self.is_checkbox_checked(self.CHECKSUMMETHODENABLE):
                if not checksummethoenable:
                    self.do_click(self.CHECKSUMMETHODENABLE)
                    self.do_click(self.CHECKSUMVALIDATIONMETHOD)
                    MOVEMETHODVALUE = (By.XPATH, f"//span[normalize-space()='{valueofchecksum}']")
                    self.do_click(MOVEMETHODVALUE)
            else:
                if checksummethoenable:
                    self.do_click(self.CHECKSUMMETHODENABLE)
                    self.do_click(self.CHECKSUMVALIDATIONMETHOD)
                    MOVEMETHODVALUE = (By.XPATH, f"//span[normalize-space()='{valueofchecksum}']")
                    self.do_click(MOVEMETHODVALUE)
            self.do_send_keys(self.CHECKSUMERROR, customererro)
            self.do_send_keys(self.IGNORECUSOM, ignanorsum)
            self.do_send_keys(self.REMARK, remark)
            if self.is_checkbox_checked(self.CHECKMETADATAERROR):
                if not metadataerror:
                    self.do_click(self.CHECKMETADATAERROR)
            else:
                self.do_click(self.CHECKMETADATAERROR)
            if self.is_checkbox_checked(self.CHECKMETADATAWARNING):
                if not metadatwerning:
                    self.do_click(self.CHECKMETADATAWARNING)
            else:
                self.do_click(self.CHECKMETADATAWARNING)
            self.do_click(self.SUBMITBUTTON)
            if self.is_visible(self.MESSAGE):
                return self.get_element_text(self.MESSAGE)
        except Exception as e:
            print(f"An error occurred: {e}")

    def Delete_Preqcprofile(self, profilename):
        try:
            DELTEPATH = (By.XPATH, f"//span[normalize-space()='{profilename}']/../../div/button")
            self.do_click(DELTEPATH)
            self.do_click(self.CONFORMATIONBUTTON)
            if self.is_visible(self.MESSAGE):
                return self.get_element_text(self.MESSAGE)
        except Exception as e:
            print(f"An error occurred: {e}")
