import os
import pytest
import time
from selenium import webdriver
from Tests.test_base import BaseTest
from Pages.Main import Main
from Config.config import Testdata
import configparser


class Test_Login(BaseTest):
    config = configparser.ConfigParser()
    config.read(os.path.join('config', 'config.ini'))

    # Read values from the config file
    name = config.get('createcustomer', 'name')
    username = config.get('createcustomer', 'username')
    email = config.get('createcustomer', 'email')
    invalidemail = config.get('createcustomer', 'invalidemail')

    def test_login_page_title(self):
        self.mainpage = Main(self.driver)
        titledata = self.mainpage.get_title(Testdata.TITLE)
        assert titledata == Testdata.TITLE

    def test_name_validation(self):
        self.mainpage = Main(self.driver)
        valdationcheck = self.mainpage.create_customer('', '', '')
        assert valdationcheck == Testdata.NAME

    def test_username_validation(self):
        self.mainpage = Main(self.driver)
        valdationcheck = self.mainpage.create_customer(self.name, '', '')
        assert valdationcheck == Testdata.USERNAME

    def test_email_validation(self):
        self.mainpage = Main(self.driver)
        valdationcheck = self.mainpage.create_customer(self.name, self.username, '')
        assert valdationcheck == Testdata.EMAILDI

    def test_email_valid_validation(self):
        self.mainpage = Main(self.driver)
        valdationcheck = self.mainpage.create_customer(self.name, self.username, self.invalidemail)
        assert valdationcheck == Testdata.VALIDEMAILID


    def test_create(self):
        self.mainpage = Main(self.driver)
        valdationcheck = self.mainpage.create_customer(self.name, self.username, self.email)
        assert valdationcheck == Testdata.CREATECUSTOMER
