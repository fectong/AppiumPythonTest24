# -*- coding:utf-8 -*-
import os
import sys
import time
import unittest
import HTMLTestRunner

from urllib.error import URLError
from tests.test_settings import Settings
from tests.test_candy_crush import CandyCrush
from tests.test_google_maps import GoogleMaps
from tests.test_google_music import GoogleMusic

def runTest():
  timestr = time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))
  filename = "./logs/"+timestr+".html"
  fp = open(filename, 'wb')
  runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'Test Report',
    description=u'Test report for bluetooth by Fe2Cu'
  )
  runner.run(suite())
  fp.close()

def suite():
  suite = unittest.TestSuite()
  test = [
    # Settings('test_getMemoryStatus'),
    # CandyCrush('test_candyCrushIO'),
    # GoogleMaps('test_multi_layers'),
    GoogleMusic('test_music_palyback')
  ]
  suite.addTests(test)
  return suite

if __name__ == "__main__":
  try:
    runTest()
  except ConnectionRefusedError as crfe:
    print('ConnectionRefusedError: {0}'.format(crfe))
  except URLError as url_error:
    print('URLError: {0}'.format(url_error))
  except AttributeError as ae:
    print('AttributeError: {0}'.format(ae))
  finally:
    print('Please check if the Appium is running')
