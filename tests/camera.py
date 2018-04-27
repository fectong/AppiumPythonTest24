# -*- coding:utf-8 -*-
"""
13. Take and Save picture: Open the camera app and take a picture.
"""
import os
import unittest

from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click

class Camera(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Camera')

  def test_take_picture(self):
    wait_el_xpath_click(self.driver, cfg.get('camera', 'btn_ok'))
    wait_el_xpath_click(self.driver, cfg.get('camera', 'shutter_path'))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()