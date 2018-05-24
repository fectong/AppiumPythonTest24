# -*- coding:utf-8 -*-
import os
import sys
import time
from appium import webdriver
from common.utils import PATH, get_path, logging
from common.mobile import get_devices, os_version

#Get mobile devices_id
devices_id = get_devices()

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
  return webdriver.Remote('{0}:{1}/wd/hub'.format(host, port), get_desired_caps(get_path('apps', app_name), device_name, platform_version, auto_grant_permissions, no_reset, fullReset, newCommandTimeout))

def get_desired_caps(app_name, device_name, platform_version, auto_grant_permissions, no_reset, fullReset, newCommandTimeout):
  desired_caps = {
    'appPackage': get_path(app_name, 'package'),
    'appActivity': get_path(app_name, 'activity'),
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