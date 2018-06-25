# -*- coding:utf-8 -*-
import os
import sys
import unittest

from time import sleep

sys.path.append("..")
from server import appium_server
from tools.constants import Commands, Keycode, C_Browser
from tools.utils import action, logging, wait_el_xpath, wait_el_xpath_click


class GoogleChrome(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_server.my_webdriver(C_Browser.APP)

  @classmethod
  def setUp(self):
    if self.driver == None:
      self.fail('GoogleChrome: Get webdriver unsucceed.')

  def test_ten_websites(self):
    prefix = C_Browser.PREFIX
    logging.info('{0}: START'.format(prefix))
    if wait_el_xpath_click(self.driver, C_Browser.PATH_BTN_TERMS_ACCEPT, 5):
      wait_el_xpath_click(self.driver, C_Browser.PATH_BTN_NEGATIVE, 20)
      wait_el_xpath_click(self.driver, C_Browser.PATH_BTN_UNCHANGE_SEARCH, 5)
    else:
      logging.info('{0}: No need to initialize Google Chrome.'.format(prefix))

    if wait_el_xpath_click(self.driver, C_Browser.PATH_SEARCH_BOX, 10):
      logging.info('{0}: There is HomePage.'.format(prefix))

    url_bar = wait_el_xpath(self.driver, C_Browser.PATH_URL_BAR, 10)
    if url_bar is None:
      logging.info('{0}: URL bar load unsucceed.'.format(prefix))
      self.fail('{0}: URL bar load unsucceed.'.format(prefix))
    
    sites = C_Browser.SITES
    for site in sites:
      logging.info('{0}: {1}'.format(prefix, site))
      action(url_bar, Commands.CLICK)
      action(url_bar, Commands.CLEAR)
      action(url_bar, Commands.SEND_KEYS, site)
      self.driver.press_keycode(Keycode.ENTER)
      sleep(20)

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDown(self):
    self.driver.close_app()

  @classmethod
  def tearDownClass(self):
    self.driver.quit()