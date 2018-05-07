# -*- coding:utf-8 -*-
import os
import sys
import time
import re
import configparser
import logging
from appium import webdriver

from common.mobile import get_serialno

#Read mobile deviceId
device_id = get_serialno()
#Read mobile os Version
os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
cfg = configparser.ConfigParser()
cfg.read(PATH('./element.ini'))

timestr = time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))
logging.basicConfig(
  level=logging.INFO,
  format="[%(asctime)s] %(levelname)s- %(message)s",
  filename=PATH("../logs/"+timestr+".log"),
  filemode = 'a'
)

def my_webdriver(app_name):
  return webdriver.Remote('http://127.0.0.1:4723/wd/hub', get_desired_caps(cfg.get('apps', app_name)))

def get_desired_caps(app_name):
  desired_caps = {
    'platformName': 'Android',
    'platformVersion': os_version,
    'deviceName': device_id,
    'appPackage': cfg.get(app_name, 'package'),
    'appActivity': cfg.get(app_name, 'activity'),
    'autoGrantPermissions': True,
    # 'noReset': True,
    # 'fullReset': False,
    # 'app': PATH('../apps/CandyCrushSaga.apk'),
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
    'automationName': 'UiAutomator2'
  }
  return desired_caps