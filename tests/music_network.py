# -*- coding:utf-8 -*-
import os
import unittest
import time
from appium import webdriver
from conf import appium_config
from common.utils import get_path, logging, wait_el_xpath, wait_el_xpath_click, get_keycode


class Tune(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('TuneInRadio')

  def test_music_network(self):
    app = 'tune_in_radio'
    prefix = 'test_music_network'
    logging.info('{0}: START'.format(prefix))
    time.sleep(30)
    wait_el_xpath_click(self.driver, get_path(app, 'btn_search_path'))
    et_search = wait_el_xpath(self.driver, get_path(app, 'et_search_path'))
    if et_search is None:
      self.fail('{0}: Load unsucceed.'.format(prefix))
    else:
      et_search.click()
      et_search.clear()
      et_search.send_keys('love')
      self.driver.press_keycode(get_keycode('ENTER'))
      song_1st = wait_el_xpath(self.driver, get_path(app, 'music_1st_path'), 30)
      if song_1st is None:
        self.fail('{0}: Please check if there is network or it is very slow.'.format(prefix))
      else:
        song_1st.click()
        if not wait_el_xpath_click(self.driver, get_path(app, 'btn_profile_play_path'), 30):
          self.fail('{0}: Please check if there is network or it is very slow.'.format(prefix))
        else:
          play_minutes = int(get_path('default', 'play_minutes'))
          timeout = time.time() + 60*play_minutes
          logging.debug('{0}: Play for {1} minutes'.format(prefix, play_minutes))
          while time.time() < timeout:
            if (int(timeout-time.time()))%20 == 0:
              self.driver.get_window_size()
              logging.info('{0}: Playing'.format(prefix))
              time.sleep(5)

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()