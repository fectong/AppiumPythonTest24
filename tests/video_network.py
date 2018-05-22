# -*- coding:utf-8 -*-
import os
import unittest
import time
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click

class Youtube(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(cfg.get('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver('Youtube')

  def test_video_network(self):
    logging.info('test_video_network: START')
    time.sleep(15)
    try:
      wait_el_xpath_click(self.driver, cfg.get('youtube', 'home_1st_video_path'))
    except:
      logging.info('test_video_network: Check if there is network.')

    timeout = time.time() + 60*self.play_minutes
    logging.info('test_video_network: Play for {0} miuntes'.format(self.play_minutes))
    while time.time() < timeout:
      if (int(timeout-time.time()))%20 == 0:
        self.driver.get_window_size()
        logging.debug('test_video_network: Playing')
        time.sleep(5)

    logging.info('test_video_network: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()