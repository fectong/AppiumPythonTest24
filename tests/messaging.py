# -*- coding:utf-8 -*-
"""
10. Receive MMS And Reply: Receive an MMS message (or RCS File Transfer, if RCS compatible) from the reference device, then send a MMS (or RCS File Transfer) response.
12. Receive SMS And Reply: Receive an SMS message (or RCS Chat, if RCS compatible) from the reference device, then send a SMS (or RCS Chat) response.
"""
import os
import unittest

from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath

class Messaging(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Messaging')

  def test_MMS(self):
    pass

  def test_SMS(self):
    pass

  @classmethod
  def tearDownClass(self):
    self.driver.quit()