# -*- coding:utf-8 -*-
import os
import sys
import unittest

from time import sleep

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, Apps
from aptools.aputils import path, keycode, action, logging, wait_el_xpath, wait_el_xpath_click


class GoogleChrome(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(Apps.GOOGLE_CHROME)

  def test_ten_websites(self):
    app = 'browser'
    prefix = 'test_ten_websites'
    logging.info('{0}: START'.format(prefix))
    if wait_el_xpath_click(self.driver, path(app, 'btn_terms_accept_path'),5):
      wait_el_xpath_click(self.driver, path(app, 'btn_negative_path'),5)
      wait_el_xpath_click(self.driver, path(app, 'btn_unchange_search_path'),5)
    else:
      logging.info('{0}: No need to initialize Google Chrome.'.format(prefix))

    if wait_el_xpath_click(self.driver, path(app, 'search_box_path')):
      logging.info('{0}: There is HomePage.'.format(prefix))

    url_bar = wait_el_xpath(self.driver, path(app, 'url_bar_path'))
    if url_bar is None:
      logging.info('{0}: URL bar load unsucceed.'.format(prefix))
      self.fail('{0}: URL bar load unsucceed.'.format(prefix))
      
    for index in range (0, 10):
      site = path('websites', 'site_{0}'.format(index))
      logging.info('{0}: {1}'.format(prefix, site))
      action(url_bar, Commands.CLICK)
      action(url_bar, Commands.CLEAR)
      action(url_bar, Commands.SEND_KEYS, site)
      self.driver.press_keycode(keycode(Commands.ENTER))
      sleep(20)

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()