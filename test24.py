# -*- coding:utf-8 -*-
import os
import sys
import time
import unittest
import traceback

from aptools import HTMLTestRunner
from aptools.aputils import logging
from aptools.apconstants import Tests

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
  timeout = time.time() + 60*60*24  # 24h = 60*60*24
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
          description=u'24 test case, test by TG'
        )
        logging.info('Test Times: {0}'.format(times))
        times+=1
        runner.run(suite())

def suite():
  suite = unittest.TestSuite()
  tests = [
    Settings(Tests.GET_MEMORY_STATUS),         # OK
    Settings(Tests.BLUETOOTH_DISABLE),         # OK
    Settings(Tests.BLUETOOTH_ENABLE),          # Headset Needed
    Settings(Tests.WLAN_DISABLE),              # OK
    Settings(Tests.WLAN_ENABLE),               # OK
    CandyCrush(Tests.CANDY_CRUSH),             # OK
    Camera(Tests.TAKE_PICTURE),                # OK
    Messaging(Tests.SMS_MO),                   # OK
    Messaging(Tests.MMS_MO),                   # OK
    GoogleMaps(Tests.MULTI_LAYERS),            # OK
    GoogleChrome(Tests.TEN_WEBSITES),          # OK
    GoogleMusic(Tests.MUSIC_PLAYBACK),         # OK
    Tune(Tests.MUSIC_NETWORK),                 # OK
    Video(Tests.VIDEO_PLAYBACK),               # OK
    Youtube(Tests.VIDEO_NETWORK),              # OK
    Dialer(Tests.MOVILTE),
    Dialer(Tests.MOVOLTE),
    Dialer(Tests.MTVOLTE),
    Dialer(Tests.VO2VI2VO)
  ]
  suite.addTests(tests)
  return suite

if __name__ == "__main__":
  try:
    runTest()
  except Exception as e:
    logging.info('Exception: {0}'.format(e))
    logging.debug('Exception: {0}'.format(traceback.format_exc()))
  finally:
    print('Please check the Reports.')