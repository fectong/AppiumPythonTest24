# -*- coding:utf-8 -*-
import os
import sys
import unittest
import time

sys.path.append("..")
from server import appium_server
from tools.constants import Commands, Keycode, C_Tune
from tools.utils import action, logging, wait_el_xpath, wait_el_xpath_click, PATH


class Tune(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_server.my_webdriver(app=C_Tune.APP, app_path=PATH('../apps/TuneInRadio.apk'))

  def test_music_network(self):
    prefix = C_Tune.PREFIX
    logging.info('{0}: START'.format(prefix))
    time.sleep(20)
    if wait_el_xpath(self.driver, C_Tune.PATH_HOMEPAGE) is not None:
      time.sleep(5)
      os.open("adb shell input tap {0} {1}".format(C_Tune.CLOSE_HOMEPAGE_X, C_Tune.CLOSE_HOMEPAGE_Y))
    else:
      logging.info('{0}: No need to initialize Tune.'.format(prefix))
    wait_el_xpath_click(self.driver, C_Tune.PATH_BTN_SEARCH)
    et_search = wait_el_xpath(self.driver, C_Tune.PATH_ET_SEARCH)
    if et_search is None:
      self.fail('{0}: Load unsucceed.'.format(prefix))
    else:
      action(et_search, Commands.SEND_KEYS, 'love')
      self.driver.press_keycode(Keycode.ENTER)
      song_1st = wait_el_xpath(self.driver, C_Tune.PATH_MUSIC_1ST, 30)
      if song_1st is None:
        self.fail('{0}: Please check if there is network or it is very slow.'.format(prefix))
      else:
        action(song_1st, Commands.CLICK)
        if not wait_el_xpath_click(self.driver, C_Tune.PATH_BTN_PROFILE_PLAY, 30):
          self.fail('{0}: Please check if there is network or it is very slow.'.format(prefix))
        else:
          play_minutes = C_Tune.PLAY_MINUTES
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