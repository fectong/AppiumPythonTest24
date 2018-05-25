# -*- coding:utf-8 -*-
import os
import sys
import time

from appium import webdriver

sys.path.append("..")
from aptools.aputils import PATH, path, logging
from aptools.apmobile import get_devices, os_version

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
  full_reset = False,
  system_port = 8200,
  newCommandTimeout = 60):
  return webdriver.Remote('{0}:{1}/wd/hub'.format(host, port), get_desired_caps(path('apps', app_name), device_name, platform_version, auto_grant_permissions, no_reset, full_reset, system_port, newCommandTimeout))

def get_desired_caps(app_name, device_name, platform_version, auto_grant_permissions, no_reset, full_reset, system_port, newCommandTimeout):
  desired_caps = {
    'appPackage': path(app_name, 'package'),
    'appActivity': path(app_name, 'activity'),
    'platformName': 'Android',
    'platformVersion': platform_version,
    'deviceName': device_name,
    'autoGrantPermissions': auto_grant_permissions,
    'noReset': no_reset,
    'fullReset': full_reset,
    'systemPort': system_port,
    'newCommandTimeout': newCommandTimeout,
    # 'udid': device_name,
    # 'app': PATH('../apps/CandyCrushSaga.apk'),
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
    'automationName': 'UiAutomator2'
  }
  return desired_caps