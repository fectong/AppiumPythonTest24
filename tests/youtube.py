# -*- coding:utf-8 -*-
import os
import unittest

from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click

class Youtube(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Youtube')

  def test_video_network(self):
    pass

  @classmethod
  def tearDownClass(self):
    self.driver.quit()