import os
import pytest
import time
from selenium import webdriver
from Tests.test_base import BaseTest
from Pages.move import Move
from Config.config import Testdata
import configparser


class Test_Move(BaseTest):
    config = configparser.ConfigParser()
    config.read(os.path.join('config', 'config.ini'))

    # Read values from the config file
    profilename = config.get('move', 'profilename')
    movemethod = config.get('move', 'movemethod')
    speedlimitrsync = config.get('move', 'speedlimitrsync')
    isoverwritecheck = config.get('move', 'isoverwritecheck')

    def test_move_profile_name_validation(self):
        self.mainpage = Move(self.driver)
        titledata = self.mainpage.create_moveprofile('', self.movemethod, self.isoverwritecheck, self.speedlimitrsync)
        assert titledata == Testdata.MOVEPROFILENAMEMESSAGE

    def test_move_profile_create(self):
        self.mainpage = Move(self.driver)
        titledata = self.mainpage.create_moveprofile(self.profilename, self.movemethod, self.isoverwritecheck, self.speedlimitrsync)
        assert titledata == Testdata.MOVESUCESSMESSAGE
