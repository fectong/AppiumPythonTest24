# -*- coding:utf-8 -*-
import os
import unittest
import time
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click

class Video(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(cfg.get('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver('Video')

  def test_play_video(self):
    logging.info('test_play_video: START')
    btn_always_x = int(cfg.get('default', 'btn_always_x'))
    btn_always_y = int(cfg.get('default', 'btn_always_y'))
    btn_always_x1 = int(cfg.get('default', 'btn_always_x1'))
    btn_always_y1 = int(cfg.get('default', 'btn_always_y1'))
    
    
    timeout = time.time() + 60*self.play_minutes
    logging.debug('test_play_video: Play for {0} minutes'.format(self.play_minutes))
    while time.time() < timeout:
      try:
        wait_el_xpath_click(self.driver, cfg.get('video', 'video_1st_path'))
      except:
        logging.info('test_play_video: Check if there are videos')
      try:
        wait_el_xpath(self.driver, cfg.get('video', 'select_video_player_path')).click()
        os.popen('adb shell input tap {0} {1}'.format(btn_always_x1, btn_always_y1))
      except:
        os.popen('adb shell input tap {0} {1}'.format(btn_always_x, btn_always_y))

      if (int(timeout-time.time()))%20 == 0:
        self.driver.get_window_size()
        logging.debug('test_play_video: Playing')
        time.sleep(5)

    logging.info('test_play_video: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()