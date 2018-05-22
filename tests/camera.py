# -*- coding:utf-8 -*-
"""
13. Take and Save picture: Open the camera app and take a picture.
"""
import os
import unittest
from time import sleep
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click

class Camera(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Camera')

  def test_take_picture(self):
    logging.info('test_take_picture: START')
    try:
      wait_el_xpath_click(self.driver, cfg.get('camera', 'btn_yes'))
    except:
      logging.info('test_take_picture: No need to press button Yes.')
    sleep(2)
    btn_shutter = wait_el_xpath(self.driver, cfg.get('camera', 'shutter_path'))
    try:
      btn_shutter.click()
    except:
      wait_el_xpath_click(self.driver, cfg.get('camera', 'camera_switcher_path'))
      wait_el_xpath_click(self.driver, cfg.get('camera', 'photo_switcher_path'))
      btn_shutter.click()
    sleep(6)
    logging.info('test_take_picture: Take a photo.')
    logging.info('test_take_picture: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()