# -*- coding:utf-8 -*-
"""
01. Get Phone Memory Status: Get the phone’s current memory status from the settings menu(this is mostly for post analysis upon instability)
14. Turn Bluetooth Off: Navigate to the appropriate settings menu and successfully disable Bluetooth.
15. Turn Bluetooth On: Navigate to the appropriate settings menu and successfully enable Bluetooth and pair to a provided headset.
16. Turn WiFi Off: Navigate to the appropriate settings menu and successfully disable WiFi.
17. Turn WiFi On: Navigate to the appropriate settings menu and successfully enable WiFi, connecting to a provided Access Point.
"""
import os
import unittest

from appium import webdriver
from conf import appium_config
from conf.appium_config import cfg, logging
from common.utils import wait_el_xpath, MobileSwipe

class Settings(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Settings')
    self.MobileSwipe = MobileSwipe()

  def test_getMemoryStatus(self):
    MobileSwipe.swipe_down(self, self.driver, 500)
    wait_el_xpath(self.driver, cfg.get('settings', 'memory_path')).click()
    tv_performance = wait_el_xpath(self.driver, cfg.get('settings_memory', 'performance_path'))
    tv_total_memory = wait_el_xpath(self.driver, cfg.get('settings_memory', 'total_memory_path'))
    tv_average_used = wait_el_xpath(self.driver, cfg.get('settings_memory', 'average_used_path'))
    tv_free = wait_el_xpath(self.driver, cfg.get('settings_memory', 'free_path'))
    logging.info(tv_performance.text)
    logging.info(tv_total_memory.text)
    logging.info(tv_average_used.text)
    logging.info(tv_free.text)

  @classmethod
  def tearDownClass(self):
    self.driver.quit()