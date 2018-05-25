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
from aptools.apconstants import Commands, Apps
from aptools.aputils import path, action, logging, wait_el_xpath, wait_el_xpath_click


class Camera(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(Apps.CAMERA)

  def test_take_picture(self):
    app = 'camera'
    prefix = 'test_take_picture'
    logging.info('{0}: START'.format(prefix))
    if not wait_el_xpath_click(self.driver, path(app, 'btn_yes')):
      logging.info('{0}: No need to initialize Camera.'.format(prefix))
    sleep(2)
    btn_shutter = wait_el_xpath(self.driver, path(app, 'shutter_path'))
    if btn_shutter is not None:
      wait_el_xpath_click(self.driver, path(app, 'camera_switcher_path'))
      wait_el_xpath_click(self.driver, path(app, 'photo_switcher_path'))
      wait_el_xpath_click(self.driver, path(app, 'shutter_path'))
    else:
      action(btn_shutter, Commands.CLICK)

    sleep(8)
    logging.info('{0}: Take a photo.'.format(prefix))
    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()