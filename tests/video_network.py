# -*- coding:utf-8 -*-
import os
import sys
import unittest
import time

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, C_Youtube
from aptools.aputils import action, logging, wait_el_xpath, wait_el_xpath_click


class Youtube(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(C_Youtube.APP)

  def test_video_network(self):
    play_minutes = C_Youtube.PLAY_MINUTES
    prefix = C_Youtube.PREFIX
    logging.info('{0}: START'.format(prefix))
    home_1st_video = wait_el_xpath(self.driver, C_Youtube.PATH_HOME_1ST_VIDEO, 30)
    if home_1st_video is None:
      logging.info('{0}: Check if there is network.'.format(prefix))
      logging.info('{0}: END'.format(prefix))
      self.fail('No network.')
    else:
      action(home_1st_video, Commands.CLICK)
      timeout = time.time() + 60*play_minutes
      logging.info('{0}: Play for {1} miuntes'.format(prefix, play_minutes))
      while time.time() < timeout:
        if (int(timeout-time.time()))%20 == 0:
          self.driver.get_window_size()
          logging.info('{0}: Playing'.format(prefix))
          time.sleep(5)
      logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()