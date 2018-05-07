# -*- coding:utf-8 -*-
"""
04. Local Music Playback: Playback a provided audio playlist from local storage.
"""
import os
import unittest

from appium import webdriver
from conf import appium_config
from conf.appium_config import cfg, logging
from common.utils import wait_el_xpath, wait_el_xpath_click

class GoogleMusic(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('GoogleMusic')
  
  def test_music_palyback(self):
    logging.info('test_music_palyback: START')
    wait_el_xpath(self.driver, cfg.get('music', 'btn_skip_path'))
    wait_el_xpath_click(self.driver, cfg.get('music', 's'))
    wait_el_xpath_click(self.driver, cfg.get('music', 'shuffle_all_path'))
    logging.info('test_music_palyback: Shuffle all of the music.')
    btn_pause_play = wait_el_xpath(self.driver, cfg.get('music', 'btn_pause_play_path'))
    wait_el_xpath_click(self.driver, cfg.get('music', 'btn_menu_path'))
    
    while btn_pause_play.tag_name == cfg.get('music', 'status_playing') :
      logging.debug(btn_pause_play.tag_name)
      
    logging.info('test_music_palyback: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()