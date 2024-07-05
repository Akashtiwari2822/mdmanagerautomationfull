import os
import pytest
import time
from selenium import webdriver
from Tests.test_base import BaseTest
from Pages.PreQc import PreQc
from Config.config import Testdata
import configparser


class Test_PreQc(BaseTest):
    config = configparser.ConfigParser()
    # config.read(os.path.join('config', 'config.ini'))
    filepath="../Config/config.ini"
    config.read(filepath)

    # Read values from the config file
    updateenable = config.get('preqc', 'updateenable')
    if updateenable:
        profilename = config.get('preqc', 'updateprofilevalue')
        checksumenable = config.get('preqc', 'updatechecksumenable')
        checksumenablevalue = config.get('preqc', 'updatechecksumenablevalue')
        checksumerror = config.get('preqc', 'updatechecksumerror')
        ignorecustom = config.get('preqc', 'updateignorecustom')
        remark = config.get('preqc', 'updateremark')
        checkmatadataerror = config.get('preqc', 'updatecheckmatadataerror')
        checkmatadatawarning = config.get('preqc', 'updatecheckmatadatawarning')
        deleteprofilename = config.get('preqc', 'deleteprofilename')
        updateprofilename = config.get('preqc', 'updateprofilename')
    else:
        profilename = config.get('preqc', 'profilename')
        checksumenable = config.get('preqc', 'checksumenable')
        checksumenablevalue = config.get('preqc', 'checksumenablevalue')
        checksumerror = config.get('preqc', 'checksumerror')
        ignorecustom = config.get('preqc', 'ignorecustom')
        remark = config.get('preqc', 'remark')
        checkmatadataerror = config.get('preqc', 'checkmatadataerror')
        checkmatadatawarning = config.get('preqc', 'checkmatadatawarning')
        deleteprofilename = config.get('preqc', 'deleteprofilename')
        updateprofilename = config.get('preqc', 'updateprofilename')

    def test_PreQc_profile_name_validation(self):
        self.mainpage = PreQc(self.driver)
        titledata = self.mainpage.Create_validation_check_Preqcprofile('', self.checksumenable,
                                                                       self.checksumenablevalue, self.checksumerror,
                                                                       self.ignorecustom, self.remark,
                                                                       self.checkmatadatawarning,
                                                                       self.checkmatadataerror)
        assert titledata == Testdata.PREQCPROFILENAMEMESSAGE

    def test_PreQc_profile_create(self):
        self.mainpage = PreQc(self.driver)
        titledata = self.mainpage.Create_validation_check_Preqcprofile(self.profilename, self.checksumenable,
                                                                       self.checksumenablevalue, self.checksumerror,
                                                                       self.ignorecustom, self.remark,
                                                                       self.checkmatadatawarning,
                                                                       self.checkmatadataerror)
        assert titledata == Testdata.PREQCSAVEMESSAGE

    def test_PreQ_Profile_Delete(self):
        self.mainpage = PreQc(self.driver)
        titledata = self.mainpage.Update_Preqcprofile(self.profilename, self.checksumenable,
                                                                       self.checksumenablevalue, self.checksumerror,
                                                                       self.ignorecustom, self.remark,
                                                                       self.checkmatadatawarning,
                                                                       self.checkmatadataerror, self.updateprofilename)
        assert titledata == Testdata.PREQCUPDATEMESSAGE

    def test_PreQ_Profile_Delete(self):
        self.mainpage = PreQc(self.driver)
        titledata = self.mainpage.Delete_Preqcprofile(self.deleteprofilename)
        assert titledata == Testdata.PREQCUPDATEMESSAGE
