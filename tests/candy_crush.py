# -*- coding:utf-8 -*-
"""
02. Launch Game: Launch a popular App Store game (currently Candy Crush), navigate the menu, then quit.
"""
import os
import sys
import unittest

from time import sleep

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, Apps
from aptools.aputils import path, logging


class CandyCrush(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(Apps.CANDY_CRUSH)

  def test_candy_crush(self):
    app = 'candy_crush'
    prefix = 'test_candy_crush'
    sleep(20)
    logging.info('{0}: START'.format(prefix))
    login_close_x = int(path(app, 'login_close_x'))
    login_close_y = int(path(app, 'login_close_y'))
    settings_x = int(path(app, 'settings_x'))
    settings_y = int(path(app, 'settings_y'))
    os.popen('adb shell input tap {0} {1}'.format(login_close_x, login_close_y))
    logging.info('{0}: Close Logging popup.'.format(prefix))
    sleep(1)
    os.popen('adb shell input tap {0} {1}'.format(settings_x, settings_y))
    logging.info('{0}: Open settings.'.format(prefix))
    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()
