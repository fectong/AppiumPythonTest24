# -*- coding:utf-8 -*-
import os
import unittest

from time import sleep
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click, get_keycode
from selenium.common.exceptions import TimeoutException


class GoogleChrome(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('GoogleChrome')

  def test_ten_websites(self):
    logging.info('test_ten_websites: START')
    if wait_el_xpath_click(self.driver, cfg.get('browser', 'btn_terms_accept_path')):
      wait_el_xpath_click(self.driver, cfg.get('browser', 'btn_negative_path'))
      wait_el_xpath_click(self.driver, cfg.get('browser', 'btn_unchange_search_path'))
    else:
      logging.info('test_ten_websites: No need to initialize Google Chrome.')

    if wait_el_xpath_click(self.driver, cfg.get('browser', 'search_box_path')):
      logging.info('test_ten_websites: There is HomePage.')

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
      logging.info('test_ten_websites: {0}'.format(site))
      url_bar.click()
      url_bar.clear()
      url_bar.send_keys(site)
      self.driver.press_keycode(get_keycode('ENTER'))
      sleep(20)

    logging.info('test_ten_websites: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()