# -*- coding:utf-8 -*-
import os
import sys
import time
import re
import configparser
import logging
from appium import webdriver

from common.mobile import get_serialno

#Get mobile devices_id
devices_id = get_serialno()

def os_version(device_name):
  """
  Get mobile os Version \n
  By device id
  """
  return os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_name)).read()

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
cfg = configparser.ConfigParser()
cfg.read(PATH('./element.ini'))

timestr = time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))
logging.basicConfig(
  level=logging.DEBUG,
  format="[%(asctime)s] %(levelname)s- %(message)s",
  filename=PATH("../logs/"+timestr+".log"),
  filemode = 'a'
)

def my_webdriver(
  app_name,
  host = 'http://127.0.0.1',
  port = 4723,
  device_name = devices_id[0],
  platform_version = os_version(devices_id[0]),
  auto_grant_permissions = True,
  no_reset = False,
  fullReset = False,
  newCommandTimeout = 60):
  return webdriver.Remote('{0}:{1}/wd/hub'.format(host, port), get_desired_caps(cfg.get('apps', app_name), device_name, platform_version, auto_grant_permissions, no_reset, fullReset, newCommandTimeout))

def get_desired_caps(app_name, device_name, platform_version, auto_grant_permissions, no_reset, fullReset, newCommandTimeout):
  desired_caps = {
    'appPackage': cfg.get(app_name, 'package'),
    'appActivity': cfg.get(app_name, 'activity'),
    'platformName': 'Android',
    'platformVersion': platform_version,
    'deviceName': device_name,
    'udid': device_name,
    'autoGrantPermissions': auto_grant_permissions,
    'noReset': no_reset,
    'fullReset': fullReset,
    'newCommandTimeout': newCommandTimeout,
    # 'app': PATH('../apps/CandyCrushSaga.apk'),
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
    'automationName': 'UiAutomator2'
  }
  return desired_caps