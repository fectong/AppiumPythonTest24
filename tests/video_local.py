# -*- coding:utf-8 -*-
import os
import sys
import unittest
import time

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, C_Video, C_Location
from aptools.aputils import action, value, logging, wait_el_xpath, wait_el_xpath_click, wait_els_xpath


class Video(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(C_Video.APP)

  def test_video_playback(self):
    prefix = C_Video.PREFIX
    play_minutes = C_Video.PLAY_MINUTES

    logging.info('{0}: START'.format(prefix))

    time.sleep(3)
    videos = wait_els_xpath(self.driver, C_Video.PATH_VIDEOS)
    if videos is None:
      logging.info('{0}: Check if there are videos'.format(prefix))
      self.fail("{0}: No Videos".format(prefix))

    logging.debug('{0}: Play each video for {1} minutes'.format(prefix, play_minutes/3))
    for video in videos:
      logging.info('{0}: {1} is playing'.format(prefix, value(video, Commands.TEXT)))
      time.sleep(1)

      action(video, Commands.CLICK)
      timeout = time.time() + 20*play_minutes

      select_play = wait_el_xpath(self.driver, C_Video.PATH_SELECT_PLAY, 3)
      if select_play is not None:
        action(select_play, Commands.CLICK)
      wait_el_xpath_click(self.driver, C_Video.PATH_BTN_ALWAYS, 2)

      if wait_el_xpath_click(self.driver, C_Location.BTN_ALLOW, 3):
        logging.info('{0}: Permission Allowed.'.format(prefix))

      if wait_el_xpath_click(self.driver, C_Video.PATH_START_OVER, 3):
        logging.info('{0}: Start Over'.format(prefix))

      while time.time() < timeout:
        if (int(timeout-time.time()))%20 == 0:
          self.driver.get_window_size()
          logging.info('{0}: Playing'.format(prefix))
          time.sleep(5)

      if wait_el_xpath(self.driver, C_Video.PATH_VIDEOS) is None:
        self.driver.back()
      else:
        continue

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()