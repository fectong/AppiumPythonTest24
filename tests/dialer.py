# -*- coding:utf-8 -*-
"""
06. MO ViLTE: Establish an outgoing IR94 Video over LTE call and stay connected to the reference device for three minutes.
07. Make MO Call: Establish an outgoing VoLTE call and stay connected to the reference device for three minutes.
11. Receive MT Call: Receive an incoming VoLTE call from the reference device and stay for three minutes.
19. VoLTE to ViLTE to VoLTE: Establish an outgoing VoLTE call to the reference device, upgrade to IR94 after 15 seconds, stay connected on the video call for three minutes, downgrade to VoLTE, then end the call after 15 seconds of audio calling.
"""

import os
import unittest

from time import sleep
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click

class Dialer(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Dialer')

  def test_MOViLTE(self):
    pass

  def test_MOVoLTE(self):
    pass
  
  def test_MTVoLTE(self):
    pass
  
  def test_Vo2Vi2Vo(self):
    pass

  @classmethod
  def tearDownClass(self):
    self.driver.quit()