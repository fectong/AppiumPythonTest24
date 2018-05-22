# -*- coding:utf-8 -*-
"""
02. Launch Game: Launch a popular App Store game (currently Candy Crush), navigate the menu, then quit.
"""
import os
import unittest

from time import sleep
from appium import webdriver
from conf import appium_config
from conf.appium_config import cfg, logging
from common.utils import wait_el_xpath

class CandyCrush(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('CandyCrush')

  def test_candy_crush(self):
    sleep(20)
    logging.info('test_candy_crush: START')
    login_close_x = int(cfg.get('candy_crush', 'login_close_x'))
    login_close_y = int(cfg.get('candy_crush', 'login_close_y'))
    settings_x = int(cfg.get('candy_crush', 'settings_x'))
    settings_y = int(cfg.get('candy_crush', 'settings_y'))
    os.popen('adb shell input tap {0} {1}'.format(login_close_x, login_close_y))
    logging.info('test_candy_crush: Close Logging popup.')
    sleep(1)
    os.popen('adb shell input tap {0} {1}'.format(settings_x, settings_y))
    logging.info('test_candy_crush: Open settings.')
    logging.info('test_candy_crush: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()
