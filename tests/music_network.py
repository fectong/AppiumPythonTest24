# -*- coding:utf-8 -*-
import os
import unittest
import time
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click, get_keycode
from selenium.common.exceptions import TimeoutException


class Tune(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(cfg.get('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver('TuneInRadio')

  def test_music_network(self):
    logging.info('test_music_network: START')
    time.sleep(30)
    wait_el_xpath_click(self.driver, cfg.get('tune_in_radio', 'btn_search_path'))
    et_search = wait_el_xpath(self.driver, cfg.get('tune_in_radio', 'et_search_path'))
    if et_search is None:
      self.fail('test_music_network: Load unsucceed.')
    else:
      et_search.click()
      et_search.clear()
      et_search.send_keys('love')
      self.driver.press_keycode(get_keycode('ENTER'))
      song_1st = wait_el_xpath(self.driver, cfg.get('tune_in_radio', 'music_1st_path'), 30)
      if song_1st is None:
        self.fail('test_music_network: Please check if there is network or it is very slow.')
      else:
        song_1st.click()
        if not wait_el_xpath_click(self.driver, cfg.get('tune_in_radio', 'btn_profile_play_path'), 30):
          self.fail('test_music_network: Please check if there is network or it is very slow.')
        else:
          timeout = time.time() + 60*self.play_minutes
          logging.debug('test_music_network: Play for {0} minutes'.format(self.play_minutes))
          while time.time() < timeout:
            if (int(timeout-time.time()))%20 == 0:
              self.driver.get_window_size()
              logging.info('test_music_network: Playing')
              time.sleep(5)

    logging.info('test_music_network: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()