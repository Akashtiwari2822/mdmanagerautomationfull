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
    updatevaluechange = config.get('move', 'updatevaluechange')
    if updatevaluechange:
        profilename = config.get('move', 'updateprofilenamevalue')
        movemethod = config.get('move', 'updatemovemethod')
        speedlimitrsync = config.get('move', 'updatespeedlimitrsync')
        isoverwritecheck = config.get('move', 'updateisoverwritecheck')
        profilenameupdate = config.get('move', 'updateprofilename')
    else:
        profilename = config.get('move', 'profilename')
        movemethod = config.get('move', 'movemethod')
        speedlimitrsync = config.get('move', 'speedlimitrsync')
        isoverwritecheck = config.get('move', 'isoverwritecheck')
        profilenameupdate = config.get('move', 'updateprofilename')

    def test_move_profile_name_validation(self):
        self.mainpage = Move(self.driver)
        titledata = self.mainpage.create_moveprofile('', self.movemethod, self.isoverwritecheck, self.speedlimitrsync,
                                                     '', '')
        assert titledata == Testdata.MOVEPROFILENAMEMESSAGE

    def test_move_profile_create(self):
        self.mainpage = Move(self.driver)
        titledata = self.mainpage.create_moveprofile(self.profilename, self.movemethod, self.isoverwritecheck,
                                                     self.speedlimitrsync, '', '')
        assert titledata == Testdata.MOVESUCESSMESSAGE

    def test_move_profile_update(self):
        self.mainpage = Move(self.driver)
        titledata = self.mainpage.create_moveprofile(self.profilename, self.movemethod, self.isoverwritecheck,
                                                     self.speedlimitrsync, 'update', self.profilenameupdate)
        assert titledata == Testdata.MOVESUCESSMESSAGE

    def test_delete_profile(self):
        self.mainpage =Move(self.driver)
        ttitledate=self.mainpage.Delete_moveprofile(self.profilename)
        assert  ttitledate == Testdata.MOVEDELETEMESSAGE
