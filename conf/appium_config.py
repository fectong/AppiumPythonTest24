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

logging.basicConfig(
  level=logging.DEBUG,
  format="[%(asctime)s] %(levelname)s: %(message)s",
  filename=PATH('../logs/sys.log'),
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

# def get_appInfo(x):
#   return{
#     cfg.get('apps', 'settings'):[cfg.get('settings', 'package'), cfg.get('settings', 'activity')],
#     cfg.get('apps', 'candy_crush'):[cfg.get('candy_crush', 'package'), cfg.get('candy_crush', 'activity')]
#   }.get(x, "Please confirm the app's name")