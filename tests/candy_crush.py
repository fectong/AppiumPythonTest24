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
    sleep(13)
    logging.info('START')
    login_close_x = int(cfg.get('candy_crush', 'login_close_x'))
    login_close_y = int(cfg.get('candy_crush', 'login_close_y'))
    settings_x = int(cfg.get('candy_crush', 'settings_x'))
    settings_y = int(cfg.get('candy_crush', 'settings_y'))
    offset = 5
    self.driver.tap([(login_close_x, login_close_y), (login_close_x+offset, login_close_y+offset)], 100)
    sleep(1)
    self.driver.tap([(settings_x, settings_y), (settings_x+offset, settings_y+offset)], 100)
    logging.info('END')
    self.driver.close_app()

  @classmethod
  def tearDownClass(self):
    self.driver.quit()
