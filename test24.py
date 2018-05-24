# -*- coding:utf-8 -*-
import os
import sys
import time
import unittest
import HTMLTestRunner
import traceback

from common.utils import get_path, logging

from tests.settings import Settings
from tests.candy_crush import CandyCrush
from tests.map import GoogleMaps
from tests.camera import Camera
from tests.browser import GoogleChrome
from tests.messaging import Messaging
from tests.music_local import GoogleMusic
from tests.music_network import Tune
from tests.video_local import Video
from tests.video_network import Youtube
from tests.dialer import Dialer


def runTest():
  times = 1
  timeout = time.time() + 60*1  # 24h = 60*60*24
  timestr = time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))

  filename = "./logs/"+timestr+".html"
  with open(filename , 'wb') as f:
    while True:
      if time.time() > timeout:
        logging.info('TEST OVER')
        break
      else:
        runner = HTMLTestRunner.HTMLTestRunner(
          stream=f,
          title=u'Test Report: {0}'.format(times),
          description=u'Test reports by TG'
        )
        logging.info('Test Times: {0}'.format(times))
        times+=1
        runner.run(suite())

def suite():
  suite = unittest.TestSuite()
  test = [
    # Settings('test_get_memory_status'),         # OK
    # Settings('test_bluetooth_disable'),         # OK
    # Settings('test_bluetooth_enable'),          # Headset Needed
    # Settings('test_wlan_disable'),              # OK
    # Settings('test_wlan_enable'),               # OK
    # CandyCrush('test_candy_crush'),             # OK
    # Camera('test_take_picture'),                # OK
    Messaging('test_SMS_MO'),
    Messaging('test_MMS_MO'),
    # GoogleMaps('test_multi_layers_no_reset'),   # OK
    # GoogleChrome('test_ten_websites'),          # OK
    # GoogleMusic('test_music_palyback'),         # OK
    # Tune('test_music_network'),                 # OK
    # Video('test_video_playback'),               # OK
    # Youtube('test_video_network'),              # OK
    # Dialer('test_MOViLTE'),
    # Dialer('test_MOVoLTE'),
    # Dialer('test_MTVoLTE'),
    # Dialer('test_Vo2Vi2Vo'),
  ]
  suite.addTests(test)
  return suite

if __name__ == "__main__":
  # try:
  #   runTest()
  # except Exception as e:
  #   logging.info('Exception: {0}'.format(e))
  #   logging.debug('Exception: {0}'.format(traceback.format_exc()))
  # finally:
  #   print('Please check the Reports.')
  runTest()