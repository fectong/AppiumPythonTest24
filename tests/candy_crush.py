# -*- coding:utf-8 -*-
"""
02. Launch Game: Launch a popular App Store game (currently Candy Crush), navigate the menu, then quit.
"""
import os
import unittest

from time import sleep
from appium import webdriver
from conf import appium_config
from common.utils import get_path, logging, wait_el_xpath

class CandyCrush(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('CandyCrush')

  def test_candy_crush(self):
    app = 'candy_crush'
    prefix = 'test_candy_crush'
    sleep(20)
    logging.info('{0}: START'.format(prefix))
    login_close_x = int(get_path(app, 'login_close_x'))
    login_close_y = int(get_path(app, 'login_close_y'))
    settings_x = int(get_path(app, 'settings_x'))
    settings_y = int(get_path(app, 'settings_y'))
    os.popen('adb shell input tap {0} {1}'.format(login_close_x, login_close_y))
    logging.info('{0}: Close Logging popup.'.format(prefix))
    sleep(1)
    os.popen('adb shell input tap {0} {1}'.format(settings_x, settings_y))
    logging.info('{0}: Open settings.'.format(prefix))
    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()
