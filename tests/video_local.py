# -*- coding:utf-8 -*-
import os
import unittest
import time
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click, wait_els_xpath


class Video(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(cfg.get('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver('Video')

  def test_video_playback(self):
    logging.info('test_video_playback: START')
    btn_always_x = int(cfg.get('default', 'btn_always_x'))
    btn_always_y = int(cfg.get('default', 'btn_always_y'))
    btn_always_x1 = int(cfg.get('default', 'btn_always_x1'))
    btn_always_y1 = int(cfg.get('default', 'btn_always_y1'))
    
    time.sleep(3)
    videos = wait_els_xpath(self.driver, cfg.get('video', 'videos_path'))
    if videos is None:
      logging.info('test_video_playback: Check if there are videos')
      self.fail("test_video_playback: No Videos")
    
    select_play = wait_el_xpath(self.driver, cfg.get('video', 'select_play_path'))
    if select_play is not None:
      os.popen('adb shell input tap {0} {1}'.format(btn_always_x1, btn_always_y1))
    else:
      os.popen('adb shell input tap {0} {1}'.format(btn_always_x, btn_always_y))
    
    logging.debug('test_video_playback: Play each video for {0} minutes'.format(self.play_minutes/3))
    for video in videos:
      logging.info('test_video_playback: {0} is playing'.format(video.text))
      timeout = time.time() + 20*self.play_minutes
      video.click()
      while time.time() < timeout:
        if (int(timeout-time.time()))%20 == 0:
          self.driver.get_window_size()
          logging.info('test_video_playback: Playing')
          time.sleep(5)
      self.driver.back()

    logging.info('test_video_playback: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()