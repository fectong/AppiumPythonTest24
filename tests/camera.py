# -*- coding:utf-8 -*-
"""
13. Take and Save picture: Open the camera app and take a picture.
"""
import os
import sys
import unittest
from time import sleep

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, C_Camera
from aptools.aputils import action, logging, wait_el_xpath, wait_el_xpath_click


class Camera(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(C_Camera.APP)

  def test_take_picture(self):
    prefix = C_Camera.PREFIX
    logging.info('{0}: START'.format(prefix))
    if not wait_el_xpath_click(self.driver, C_Camera.PATH_BTN_YES):
      logging.info('{0}: No need to initialize Camera.'.format(prefix))
    sleep(2)
    btn_shutter = wait_el_xpath(self.driver, C_Camera.PATH_SHUTTER)
    if btn_shutter is not None:
      wait_el_xpath_click(self.driver, C_Camera.PATH_CAMERA_SWITCHER)
      wait_el_xpath_click(self.driver,C_Camera.PATH_PHOTO_SWITCHER)
      wait_el_xpath_click(self.driver, C_Camera.PATH_SHUTTER)
    else:
      action(btn_shutter, Commands.CLICK)

    sleep(8)
    logging.info('{0}: Take a photo.'.format(prefix))
    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()