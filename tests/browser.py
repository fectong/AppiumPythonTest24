# -*- coding:utf-8 -*-
import os
import unittest

from time import sleep
from appium import webdriver
from conf import appium_config
from common.utils import get_path, logging, wait_el_xpath, wait_el_xpath_click, get_keycode


class GoogleChrome(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('GoogleChrome')

  def test_ten_websites(self):
    app = 'browser'
    prefix = 'test_ten_websites'
    logging.info('{0}: START'.format(prefix))
    if wait_el_xpath_click(self.driver, get_path(app, 'btn_terms_accept_path'),5):
      wait_el_xpath_click(self.driver, get_path(app, 'btn_negative_path'),5)
      wait_el_xpath_click(self.driver, get_path(app, 'btn_unchange_search_path'),5)
    else:
      logging.info('{0}: No need to initialize Google Chrome.'.format(prefix))

    if wait_el_xpath_click(self.driver, get_path(app, 'search_box_path')):
      logging.info('{0}: There is HomePage.'.format(prefix))

    url_bar = wait_el_xpath(self.driver, get_path(app, 'url_bar_path'))
    if url_bar is None:
      logging.info('{0}: URL bar load unsucceed.'.format(prefix))
      self.fail('{0}: URL bar load unsucceed.'.format(prefix))
      
    for index in range (0, 10):
      site = get_path('websites', 'site_{0}'.format(index))
      logging.info('{0}: {1}'.format(prefix, site))
      url_bar.click()
      url_bar.clear()
      url_bar.send_keys(site)
      self.driver.press_keycode(get_keycode('ENTER'))
      sleep(20)

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()