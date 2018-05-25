# -*- coding:utf-8 -*-
import os
import sys
import unittest
import time

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, Apps
from aptools.aputils import path, action, logging, wait_el_xpath, wait_el_xpath_click


class Youtube(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(path('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver(Apps.YOUTUBE)

  def test_video_network(self):
    app = 'youtube'
    prefix = 'test_video_network'
    logging.info('{0}: START'.format(prefix))
    home_1st_video = wait_el_xpath(self.driver, path(app, 'home_1st_video_path'), 30)
    if home_1st_video is None:
      logging.info('{0}: Check if there is network.'.format(prefix))
      logging.info('{0}: END'.format(prefix))
      self.fail('No network.')
    else:
      action(home_1st_video, Commands.CLICK)
      timeout = time.time() + 60*self.play_minutes
      logging.info('{0}: Play for {1} miuntes'.format(prefix, self.play_minutes))
      while time.time() < timeout:
        if (int(timeout-time.time()))%20 == 0:
          self.driver.get_window_size()
          logging.debug('{0}: Playing'.format(prefix))
          time.sleep(5)
      logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()