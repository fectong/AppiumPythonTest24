# -*- coding:utf-8 -*-
"""
Local Music Playback:
  Playback a provided audio playlist from local storage.
"""
import os
import unittest
import configparser
import logging
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
cfg = configparser.ConfigParser()
cfg.read(PATH('../conf/element.ini'))
logging.basicConfig(
  level=logging.DEBUG,
  format="[%(asctime)s] %(levelname)s: %(message)s"
)

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