# -*- coding:utf-8 -*-
"""
04. Local Music Playback: Playback a provided audio playlist from local storage.
"""
import os
import unittest
import time
from appium import webdriver
from conf import appium_config
from conf.appium_config import cfg, logging
from common.utils import wait_el_xpath, wait_el_xpath_click
from selenium.common.exceptions import TimeoutException


class GoogleMusic(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(cfg.get('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver('GoogleMusic')
  
  def test_music_palyback(self):
    logging.info('test_music_palyback: START')
    try:
      wait_el_xpath(self.driver, cfg.get('music', 'btn_skip_path'))
    except TimeoutException:
      logging.info('test_music_palyback: No need to initialize Google Music.')

    wait_el_xpath_click(self.driver, cfg.get('music', 'nav_listen_now_path'))
    time.sleep(3)
    wait_el_xpath_click(self.driver, cfg.get('music', 'shuffle_all_path'))
    logging.info('test_music_palyback: Shuffle all of the music.')
    btn_pause_play = wait_el_xpath(self.driver, cfg.get('music', 'btn_pause_play_path'))
    
    timeout = time.time() + 60*self.play_minutes
    while btn_pause_play.tag_name == cfg.get('music', 'status_playing') :
      if (int(timeout-time.time()))%20 == 0:
        logging.info('test_music_palyback: Playing')
        time.sleep(5)

    logging.info('test_music_palyback: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()