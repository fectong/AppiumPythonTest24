# -*- coding:utf-8 -*-
import os
import unittest

from time import sleep
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click

class GoogleChrome(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('GoogleChrome')

  def test_tenWebsites(self):
    wait_el_xpath_click(self.driver, cfg.get('browser', 'btn_terms_accept_path'))
    wait_el_xpath_click(self.driver, cfg.get('browser', 'search_box_path'))
    url_bar = wait_el_xpath(self.driver, cfg.get('browser', 'url_bar_path'))

    websites = [
      cfg.get('websites', 'site_0'),
      cfg.get('websites', 'site_1'),
      cfg.get('websites', 'site_2'),
      cfg.get('websites', 'site_3'),
      cfg.get('websites', 'site_4'),
      cfg.get('websites', 'site_5'),
      cfg.get('websites', 'site_6'),
      cfg.get('websites', 'site_7'),
      cfg.get('websites', 'site_8'),
      cfg.get('websites', 'site_9'),
    ]

    for site in websites:
      url_bar.clear()
      url_bar.send_keys(site)
      self.driver.press_keycode(66)
      sleep(15)

  @classmethod
  def tearDownClass(self):
    self.driver.quit()