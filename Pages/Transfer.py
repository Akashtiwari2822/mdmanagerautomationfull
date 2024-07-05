import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import Testdata


class Transfer(BasePage):
    GOTOPROFILE = (
        By.XPATH, "//div[@routerlink='/profiles']")
    MOVETAB = (By.XPATH, "//mat-tab-header/div[2]/div/div/div[5]")
    MESSAGE = (By.XPATH, "//simple-snack-bar/span")
    ADDNEW = (By.XPATH, "//button[@class='mat-focus-indicator new-button mat-raised-button mat-button-base']")
    PROFILENAME = (By.XPATH, "//input[@data-placeholder='Profile Name']")
    VALIDPREFIX = (By.XPATH, "//input[@data-placeholder='Valid Prefix (optional)']")
    VALIDEXTENTION = (By.XPATH, "//input[@data-placeholder='Valid Extension (optional)']")
    REMARK = (By.XPATH, "//input[@data-placeholder='Remarks (optional)']")
    OVERWRITE = (By.XPATH, "//mat-expansion-panel[1]/div/div/div/div[2]/div/mat-checkbox")
    TRANSFERVALIDATION = (By.XPATH, "//mat-expansion-panel[2]/mat-expansion-panel-header")
    CHECKSUM = (By.XPATH, "//mat-expansion-panel[2]/div/div/div/div[1]/mat-form-field/div/div[1]/div/mat-select")
    DELETEAFTERFAILURE = (By.XPATH, "//mat-select[@placeholder='Delete After Failure']")
    TRANSFERMACHANISM = (By.XPATH, "//mat-accordion/mat-expansion-panel[3]/mat-expansion-panel-header")
    TRANSFERPROTOCOL = (By.XPATH, "//mat-select[@placeholder='Transfer Protocol']")
    OPRATIONTYPE = (By.XPATH, "//mat-select[@placeholder='Operation Type']")
    SUBMITBUTTON = (By.XPATH, "//button[@class='mat-focus-indicator action-button-update-global mat-raised-button "
                              "mat-button-base']")
    CONFORMATIONBUTTON = (By.XPATH, "//div[@class='cdk-overlay-container']//button[2]")

    def __init__(self, driver):
        super(Transfer, self).__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    def Create_validation_check_Transfercprofile(self, profilename, validprefix, validextention, remark, overwrite,
                                                 valuechecksumval, deleteafterfailure, transferprotocol,oprationtypeval):
        self.do_click(self.GOTOPROFILE)
        self.hard_refresh()
        self.hard_refresh()
        self.do_click(self.MOVETAB)
        self.do_click(self.ADDNEW)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.VALIDPREFIX, validprefix)
        self.do_send_keys(self.VALIDEXTENTION, validextention)
        self.do_send_keys(self.REMARK, remark)
        if overwrite:
            self.do_click(self.OVERWRITE)
        self.do_click(self.TRANSFERVALIDATION)
        self.do_click(self.CHECKSUM)
        CHECKSUMVALUE = (By.XPATH, f"//span[normalize-space()='{valuechecksumval}']")
        self.do_click(CHECKSUMVALUE)
        self.do_click(self.DELETEAFTERFAILURE)
        DELETAFTERFAILURE = (By.XPATH, f"//span[normalize-space()='{deleteafterfailure}']")
        self.do_click(DELETAFTERFAILURE)
        self.do_click(self.TRANSFERMACHANISM)
        self.do_click(self.TRANSFERPROTOCOL)
        TRANSFERPROTOCOLVAL = (By.XPATH, f"//span[normalize-space()='{transferprotocol}']")
        self.do_click(TRANSFERPROTOCOLVAL)
        self.do_click(self.OPRATIONTYPE)
        OPRATIONTYPEVAL = (By.XPATH, f"//span[normalize-space()='{oprationtypeval}']")
        self.do_click(OPRATIONTYPEVAL)
        self.do_click(self.SUBMITBUTTON)
        if self.is_visible(self.MESSAGE):
            return self.get_element_text(self.MESSAGE)

    def Update_Transfercprofile(self, profilename, validprefix, validextention, remark, overwrite,
                                                 valuechecksumval, deleteafterfailure, transferprotocol,oprationtypeval,updateprofilename):
        self.do_click(self.GOTOPROFILE)
        self.hard_refresh()
        self.hard_refresh()
        self.do_click(self.MOVETAB)
        MOVEMETHODVALUE = (By.XPATH, f"//span[normalize-space()='{updateprofilename}']")
        # self.do_click(self.ADDNEW)
        self.do_click(MOVEMETHODVALUE)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.VALIDPREFIX, validprefix)
        self.do_send_keys(self.VALIDEXTENTION, validextention)
        self.do_send_keys(self.REMARK, remark)
        if self.is_checkbox_checked(self.CHECKSUMMETHODENABLE):
            if not overwrite:
                self.do_click(self.OVERWRITE)
        else:
            if overwrite:
                self.do_click(self.OVERWRITE)
        self.do_click(self.TRANSFERVALIDATION)
        self.do_click(self.CHECKSUM)
        CHECKSUMVALUE = (By.XPATH, f"//span[normalize-space()='{valuechecksumval}']")
        self.do_click(CHECKSUMVALUE)
        self.do_click(self.DELETEAFTERFAILURE)
        DELETAFTERFAILURE = (By.XPATH, f"//span[normalize-space()='{deleteafterfailure}']")
        self.do_click(DELETAFTERFAILURE)
        self.do_click(self.TRANSFERMACHANISM)
        self.do_click(self.TRANSFERPROTOCOL)
        TRANSFERPROTOCOLVAL = (By.XPATH, f"//span[normalize-space()='{transferprotocol}']")
        self.do_click(TRANSFERPROTOCOLVAL)
        self.do_click(self.OPRATIONTYPE)
        OPRATIONTYPEVAL = (By.XPATH, f"//span[normalize-space()='{oprationtypeval}']")
        self.do_click(OPRATIONTYPEVAL)
        self.do_click(self.SUBMITBUTTON)
        if self.is_visible(self.MESSAGE):
            return self.get_element_text(self.MESSAGE)

    def Delete_Transferprofile(self, profilename):
        DELTEPATH = (By.XPATH, f"//span[normalize-space()='{profilename}']/../../div/button")
        self.do_click(DELTEPATH)
        self.do_click(self.CONFORMATIONBUTTON)
        if self.is_visible(self.MESSAGE):
            return self.get_element_text(self.MESSAGE)