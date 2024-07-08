import os
import pytest
import time
from selenium import webdriver
from Tests.test_base import BaseTest
from Pages.Transfer import Transfer
from Config.config import Testdata
import configparser


class Test_Transfer(BaseTest):
    config = configparser.ConfigParser()
    # config.read(os.path.join('config', 'config.ini'))
    filepath = "../Config/config.ini"
    config.read(filepath)

    updateenable = config.get('transfer', 'updateenable')
    if updateenable:
        profilename = config.get('transfer', 'profilename')
        validprefix = config.get('transfer', 'validprefix')
        validextention = config.get('transfer', 'validextention')
        remark = config.get('transfer', 'remark')
        overwritecheck = config.get('transfer', 'overwritecheck')
        checksum = config.get('transfer', 'checksum')
        deleteafterfailure = config.get('transfer', 'deleteafterfailure')
        transferprotocal = config.get('transfer', 'transferprotocal')
        operationtype = config.get('transfer', 'operationtype')
        updateprofilename = config.get('transfer', 'updateprofilename')
        deleteprofilename = config.get('transfer', 'deleteprofilename')
    else:
        profilename = config.get('transfer', 'profilename')
        validprefix = config.get('transfer', 'validprefix')
        validextention = config.get('transfer', 'validextention')
        remark = config.get('transfer', 'remark')
        overwritecheck = config.get('transfer', 'overwritecheck')
        checksum = config.get('transfer', 'checksum')
        deleteafterfailure = config.get('transfer', 'deleteafterfailure')
        transferprotocal = config.get('transfer', 'transferprotocal')
        operationtype = config.get('transfer', 'operationtype')
        updateprofilename = config.get('transfer', 'updateprofilename')
        deleteprofilename = config.get('transfer', 'deleteprofilename')

    def test_Tranfer_profile_name_validation(self):
        self.pagename = Transfer(self.driver)
        testdata = self.pagename.Create_validation_check_Transfercprofile('', self.validprefix,
                                                                          self.validextention, self.remark,
                                                                          self.overwritecheck, self.checksum, self.deleteafterfailure,
                                                                          self.transferprotocal, self.operationtype)
        assert testdata == Testdata.TRANSFERPROFILENAMEMESSAGE

    def test_Tranfer_Check_sum_validation(self):
        self.pagename = Transfer(self.driver)
        testdata = self.pagename.Create_validation_check_Transfercprofile('', self.validprefix,
                                                                          self.validextention, self.remark,
                                                                          self.overwritecheck, '', self.deleteafterfailure,
                                                                          self.transferprotocal, self.operationtype)
        assert testdata == Testdata.TRANSFERCHECKSUM
    def test_Tranfer_Tansfer_protocol_validation(self):
        self.pagename = Transfer(self.driver)
        testdata = self.pagename.Create_validation_check_Transfercprofile('', self.validprefix,
                                                                          self.validextention, self.remark,
                                                                          self.overwritecheck, self.checksum, self.deleteafterfailure,
                                                                          '', self.operationtype)
        assert testdata == Testdata.TRANSFERPROTOCOL

    def test_Tranfer_optaion_type_validation(self):
        self.pagename = Transfer(self.driver)
        testdata = self.pagename.Create_validation_check_Transfercprofile('', self.validprefix,
                                                                          self.validextention, self.remark,
                                                                          self.overwritecheck, self.checksum, self.deleteafterfailure,
                                                                          self.transferprotocal, '')
        assert testdata == Testdata.TRANSFERPROTOCOL

    def test_Tranfer_profile_Create(self):
        self.pagename = Transfer(self.driver)
        testdata = self.pagename.Create_validation_check_Transfercprofile(self.profilename, self.validprefix,
                                                                          self.validextention, self.remark,
                                                                          self.overwritecheck, self.checksum, self.deleteafterfailure,
                                                                          self.transferprotocal, self.operationtype)
        assert testdata == Testdata.TRANSFERSAVEMESSAGE
