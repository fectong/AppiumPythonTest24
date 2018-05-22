# -*- coding:utf-8 -*-
import os
import unittest
import time
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click, get_keycode

class Tune(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(cfg.get('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver('TuneInRadio')

  def test_music_network(self):
    logging.info('test_music_network: START')
    time.sleep(30)
    wait_el_xpath_click(self.driver, cfg.get('tune_in_radio', 'btn_search'))
    et_search = wait_el_xpath(self.driver, cfg.get('tune_in_radio', 'et_search'))
    et_search.clear()
    et_search.send_keys('love')
    self.driver.press_keycode(get_keycode('ENTER'))
    time.sleep(5)
    try:
      wait_el_xpath_click(self.driver, cfg.get('tune_in_radio', 'music_1st_path'))
      wait_el_xpath_click(self.driver, cfg.get('tune_in_radio', 'btn_profile_play'))
    except:
      logging.info('test_music_network: Check if there is network.')
    
    timeout = time.time() + 60*self.play_minutes
    logging.debug('test_music_network: Play for {0} minutes'.format(self.play_minutes))
    while time.time() < timeout:
      if (int(timeout-time.time()))%20 == 0:
        self.driver.get_window_size()
        logging.debug('test_music_network: Playing')
        time.sleep(5)

    logging.info('test_music_network: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()