# -*- coding:utf-8 -*-
import os
import sys
import time

from appium import webdriver

sys.path.append("..")
from aptools.aputils import PATH, logging
from aptools.apmobile import get_devices, os_version

#Get mobile devices_id
devices_id = get_devices()

def my_webdriver(
  app,
  host = '127.0.0.1',
  port = 4723,
  device_name = devices_id[0],
  auto_grant_permissions = True,
  no_reset = False,
  full_reset = False,
  system_port = 8200,
  newCommandTimeout = 60,
  app_path = ''):
  
  try:
    return webdriver.Remote('http://{0}:{1}/wd/hub'.format(host, port), get_desired_caps(app, device_name, auto_grant_permissions, no_reset, full_reset, system_port, newCommandTimeout, app_path))
  except Exception as e:
    logging.info('please confirm if the appium server is running.')
    logging.debug('Exception: {0}, please confirm if the appium server is running.'.format(e))
    return None

def get_desired_caps(app, device_name, auto_grant_permissions, no_reset, full_reset, system_port, newCommandTimeout, app_path):
  desired_caps = {
    'appPackage': app[1],
    'appActivity': app[2],
    'platformName': 'Android',
    'platformVersion': os_version(device_name),
    'deviceName': device_name,
    'autoGrantPermissions': auto_grant_permissions,
    'noReset': no_reset,
    'fullReset': full_reset,
    'systemPort': system_port,
    'newCommandTimeout': newCommandTimeout,
    'app': app_path,
    'udid': device_name,
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
    'noSign': True,
    'automationName': 'UiAutomator2'
  }
  return desired_caps