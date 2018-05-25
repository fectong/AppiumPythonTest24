# -*- coding:utf-8 -*-
import os
import sys
import unittest
import time

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, Apps
from aptools.aputils import path, action, value, logging, wait_el_xpath, wait_el_xpath_click, wait_els_xpath


class Video(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(path('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver(Apps.VIDEO)

  def test_video_playback(self):
    app = 'video'
    prefix = 'test_video_playback'
    logging.info('{0}: START'.format(prefix))
    btn_always_x = int(path('default', 'btn_always_x'))
    btn_always_y = int(path('default', 'btn_always_y'))
    btn_always_x1 = int(path('default', 'btn_always_x1'))
    btn_always_y1 = int(path('default', 'btn_always_y1'))
    
    time.sleep(3)
    videos = wait_els_xpath(self.driver, path(app, 'videos_path'))
    if videos is None:
      logging.info('{0}: Check if there are videos'.format(prefix))
      self.fail("{0}: No Videos".format(prefix))
    
    select_play = wait_el_xpath(self.driver, path(app, 'select_play_path'))
    if select_play is not None:
      os.popen('adb shell input tap {0} {1}'.format(btn_always_x1, btn_always_y1))
    else:
      os.popen('adb shell input tap {0} {1}'.format(btn_always_x, btn_always_y))
    
    logging.debug('{0}: Play each video for {1} minutes'.format(prefix, self.play_minutes/3))
    for video in videos:
      logging.info('{0}: {1} is playing'.format(prefix, value(video, Commands.TEXT)))
      timeout = time.time() + 20*self.play_minutes
      action(video, Commands.CLICK)
      while time.time() < timeout:
        if (int(timeout-time.time()))%20 == 0:
          self.driver.get_window_size()
          logging.info('{0}: Playing'.format(prefix))
          time.sleep(5)
      self.driver.back()

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()