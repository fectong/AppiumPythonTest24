# -*- coding:utf-8 -*-
import os
import sys
import unittest
import time

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, C_Video
from aptools.aputils import action, value, logging, wait_el_xpath, wait_el_xpath_click, wait_els_xpath


class Video(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(C_Video.APP)

  def test_video_playback(self):
    prefix = C_Video.PREFIX
    play_minutes = C_Video.PLAY_MINUTES
    
    logging.info('{0}: START'.format(prefix))
    btn_always_x = C_Video.BTN_ALWAYS_X
    btn_always_y = C_Video.BTN_ALWAYS_Y
    btn_always_x1 = C_Video.BTN_ALWAYS_X1
    btn_always_y1 = C_Video.BTN_ALWAYS_Y1
    
    time.sleep(3)
    videos = wait_els_xpath(self.driver, C_Video.PATH_VIDEOS)
    if videos is None:
      logging.info('{0}: Check if there are videos'.format(prefix))
      self.fail("{0}: No Videos".format(prefix))
    
    select_play = wait_el_xpath(self.driver, C_Video.PATH_SELECT_PLAY)
    logging.info(value(select_play, Commands.TEXT))
    if select_play is not None:
      os.popen('adb shell input tap {0} {1}'.format(btn_always_x1, btn_always_y1))
    else:
      os.popen('adb shell input tap {0} {1}'.format(btn_always_x, btn_always_y))
    
    logging.debug('{0}: Play each video for {1} minutes'.format(prefix, play_minutes/3))
    for video in videos:
      logging.info('{0}: {1} is playing'.format(prefix, value(video, Commands.TEXT)))
      # timeout = time.time() + 20*play_minutes
      action(video, Commands.CLICK)
      # while time.time() < timeout:
      #   if (int(timeout-time.time()))%20 == 0:
      #     self.driver.get_window_size()
      #     logging.info('{0}: Playing'.format(prefix))
      #     time.sleep(5)
      time.sleep(5)
      self.driver.back()

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()