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
    # wait_el_xpath_click(self.driver, cfg.get('google_music', 'skip_button'))
    wait_el_xpath_click(self.driver, cfg.get('google_music', 'btn_menu'))
    wait_el_xpath_click(self.driver, cfg.get('google_music', 'shuffle_all'))
    btn_pause_play = wait_el_xpath(self.driver, cfg.get('google_music', 'btn_pause_play'))
    
    content = btn_pause_play.tag_name
    while content == 'Pause':
      logging.info(btn_pause_play.tag_name)
      content = btn_pause_play.tag_name

  @classmethod
  def tearDownClass(self):
    self.driver.quit()