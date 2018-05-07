# -*- coding:utf-8 -*-
import os
import sys
import time
import unittest
import HTMLTestRunner
import configparser
import traceback
from conf.appium_config import logging
from tests.settings import Settings
from tests.candy_crush import CandyCrush
from tests.map import GoogleMaps
from tests.music_local import GoogleMusic
from tests.camera import Camera
from tests.browser import GoogleChrome
from tests.messaging import Messaging

def runTest():
  times = 1
  timeout = time.time() + 60*10  # 24h = 60*60*24
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
    Settings('test_get_memory_status'),
    Settings('test_bluetooth_disable'),
    Settings('test_bluetooth_enable'),
    Settings('test_wlan_disable'),
    Settings('test_wlan_enable'),
    Camera('test_take_picture'),
    GoogleChrome('test_ten_websites'),
    GoogleMaps('test_multi_layers'),
    GoogleMusic('test_music_palyback'),
    Messaging('test_SMS_MO'),
    Messaging('test_MMS_MO'),
    CandyCrush('test_candy_crush')
  ]
  suite.addTests(test)
  return suite

if __name__ == "__main__":
  try:
    runTest()
  except KeyboardInterrupt as ki:
    logging.info('KeyboardInterrupt: {0}'.format(ki))
    logging.debug('KeyboardInterrupt: {0}'.format(traceback.format_exc()))
  except KeyError as ke:
    logging.info('KeyError: {0}'.format(ke))
    logging.debug('KeyError: {0}'.format(traceback.format_exc()))
  except AttributeError as ae:
    logging.info('AttributeError: {0}'.format(ae))
    logging.debug('AttributeError: {0}'.format(traceback.format_exc()))
  except Exception as e:
    logging.info('Exception: {0}'.format(e))
    logging.debug('Exception: {0}'.format(traceback.format_exc()))
  finally:
    print('Please check the Reports.')