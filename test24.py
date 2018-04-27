# -*- coding:utf-8 -*-
import os
import sys
import time
import unittest
import HTMLTestRunner
import configparser

from tests.settings import Settings
from tests.candy_crush import CandyCrush
from tests.map import GoogleMaps
from tests.music_local import GoogleMusic
from tests.camera import Camera
from tests.browser import GoogleChrome

def runTest():
  times = 1
  timeout = time.time() + 60*60*24   # 24h = 60*60*24
  timestr = time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))

  filename = "./logs/"+timestr+".html"
  fp = open(filename, 'wb')
  
  while True:
    if time.time() > timeout:
      print('TEST OVER')
      break
    else:
      runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'Test Report: {0}'.format(times),
        description=u'Test reports by TG'
      )
      times+=1
      runner.run(suite())

  fp.close()

def suite():
  suite = unittest.TestSuite()
  test = [
    Settings('test_get_memory_status'),
    Settings('test_bluetooth_disable'),
    Settings('test_bluetooth_enable'),
    Settings('test_wlan_disable'),
    Settings('test_wlan_enable'),
    CandyCrush('test_candy_crush'),
    GoogleMaps('test_multi_layers'),
    GoogleMusic('test_music_palyback'),
    Camera('test_take_picture'),
    GoogleChrome('test_ten_websites')
  ]
  suite.addTests(test)
  return suite

if __name__ == "__main__":
  try:
    runTest()
  except Exception as e:
    print('Exception: {0}'.format(e))
  finally:
    print('Please check the Reports.')