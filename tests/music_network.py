# -*- coding:utf-8 -*-
import os
import sys
import unittest
import time

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, Apps
from aptools.aputils import path, action, logging, wait_el_xpath, wait_el_xpath_click, keycode


class Tune(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(Apps.TUNE_IN_RADIO)

  def test_music_network(self):
    app = 'tune_in_radio'
    prefix = 'test_music_network'
    logging.info('{0}: START'.format(prefix))
    time.sleep(30)
    wait_el_xpath_click(self.driver, path(app, 'btn_search_path'))
    et_search = wait_el_xpath(self.driver, path(app, 'et_search_path'))
    if et_search is None:
      self.fail('{0}: Load unsucceed.'.format(prefix))
    else:
      action(et_search, Commands.CLICK)
      action(et_search, Commands.CLEAR)
      action(et_search, Commands.SEND_KEYS, 'love')
      self.driver.press_keycode(keycode(Commands.ENTER))
      song_1st = wait_el_xpath(self.driver, path(app, 'music_1st_path'), 30)
      if song_1st is None:
        self.fail('{0}: Please check if there is network or it is very slow.'.format(prefix))
      else:
        action(song_1st, Commands.CLICK)
        if not wait_el_xpath_click(self.driver, path(app, 'btn_profile_play_path'), 30):
          self.fail('{0}: Please check if there is network or it is very slow.'.format(prefix))
        else:
          play_minutes = int(path('default', 'play_minutes'))
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