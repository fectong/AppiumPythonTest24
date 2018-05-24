# -*- coding:utf-8 -*-
"""
04. Local Music Playback: Playback a provided audio playlist from local storage.
"""
import os
import unittest
import time
from appium import webdriver
from conf import appium_config
from common.utils import get_path, logging, wait_el_xpath, wait_el_xpath_click


class GoogleMusic(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.play_minutes = int(get_path('default', 'play_minutes'))
    self.driver = appium_config.my_webdriver('GoogleMusic')
  
  def test_music_palyback(self):
    app = 'music'
    prefix = 'test_music_palyback'
    logging.info('{0} START'.format(prefix))

    if not wait_el_xpath_click(self.driver, get_path(app, 'btn_skip_path')):
      logging.info('{0} No need to initialize Google Music.'.format(prefix))

    wait_el_xpath_click(self.driver, get_path(app, 'nav_listen_now_path'))
    time.sleep(3)
    wait_el_xpath_click(self.driver, get_path(app, 'shuffle_all_path'))
    logging.info('{0} Shuffle all of the music.'.format(prefix))
    btn_pause_play = wait_el_xpath(self.driver, get_path(app, 'btn_pause_play_path'))
    
    timeout = time.time() + 60*self.play_minutes
    while btn_pause_play.tag_name == get_path(app, 'status_playing') :
      if (int(timeout-time.time()))%20 == 0:
        logging.info('{0} Playing'.format(prefix))
        time.sleep(5)

    logging.info('{0} END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()