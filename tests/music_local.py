# -*- coding:utf-8 -*-
"""
04. Local Music Playback: Playback a provided audio playlist from local storage.
"""
import os
import sys
import unittest
import time

sys.path.append("..")
from server import appium_server
from tools.constants import Commands, C_Music
from tools.utils import value, logging, wait_el_xpath, wait_el_xpath_click


class GoogleMusic(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.driver = appium_server.my_webdriver(C_Music.APP)

  @classmethod
  def setUp(self):
    if self.driver == None:
      self.fail('GoogleMusic: Get webdriver unsucceed.')

  def test_music_palyback(self):
    prefix = C_Music.PREFIX
    logging.info('{0}: START'.format(prefix))
    if not wait_el_xpath_click(self.driver, C_Music.PATH_BTN_SKIP):
      logging.info('{0}: No need to initialize Google Music.'.format(prefix))

    wait_el_xpath_click(self.driver, C_Music.PATH_NAV_LISTEN_NOW)
    time.sleep(3)
    if not wait_el_xpath_click(self.driver, C_Music.PATH_SHUFFLE_ALL):
      self.fail('{0}: If there are musics.'.format(prefix))
      logging.info('{0}: If there are musics.'.format(prefix))
    logging.info('{0}: Shuffle all of the music.'.format(prefix))
    btn_pause_play = wait_el_xpath(self.driver, C_Music.PATH_BTN_PAUSE_PLAY)
    
    timeout = time.time() + 60*C_Music.PLAY_MINUTES
    while value(btn_pause_play, Commands.TAG_NAME) == C_Music.STATUS_PLAYING:
      if (int(timeout-time.time()))%20 == 0:
        logging.info('{0}: Playing'.format(prefix))
        time.sleep(5)

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDown(self):
    self.driver.close_app()

  @classmethod
  def tearDownClass(self):
    self.driver.quit()