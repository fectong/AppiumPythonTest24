# -*- coding:utf-8 -*-
import os
import unittest
import time
from appium import webdriver
from conf import appium_config
from common.utils import get_path, logging, wait_el_xpath, wait_el_xpath_click, wait_els_xpath


class Video(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(get_path('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver('Video')

  def test_video_playback(self):
    app = 'video'
    prefix = 'test_video_playback'
    logging.info('{0}: START'.format(prefix))
    btn_always_x = int(get_path('default', 'btn_always_x'))
    btn_always_y = int(get_path('default', 'btn_always_y'))
    btn_always_x1 = int(get_path('default', 'btn_always_x1'))
    btn_always_y1 = int(get_path('default', 'btn_always_y1'))
    
    time.sleep(3)
    videos = wait_els_xpath(self.driver, get_path(app, 'videos_path'))
    if videos is None:
      logging.info('{0}: Check if there are videos'.format(prefix))
      self.fail("{0}: No Videos".format(prefix))
    
    select_play = wait_el_xpath(self.driver, get_path(app, 'select_play_path'))
    if select_play is not None:
      os.popen('adb shell input tap {0} {1}'.format(btn_always_x1, btn_always_y1))
    else:
      os.popen('adb shell input tap {0} {1}'.format(btn_always_x, btn_always_y))
    
    logging.debug('{0}: Play each video for {1} minutes'.format(prefix, self.play_minutes/3))
    for video in videos:
      logging.info('{0}: {1} is playing'.format(prefix, video.text))
      timeout = time.time() + 20*self.play_minutes
      video.click()
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