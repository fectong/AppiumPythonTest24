# -*- coding:utf-8 -*-
"""
01. Get Phone Memory Status: Get the phone’s current memory status from the settings menu(this is mostly for post analysis upon instability)
14. Turn Bluetooth Off: Navigate to the appropriate settings menu and successfully disable Bluetooth.
15. Turn Bluetooth On: Navigate to the appropriate settings menu and successfully enable Bluetooth and pair to a provided headset.
16. Turn WiFi Off: Navigate to the appropriate settings menu and successfully disable WiFi.
17. Turn WiFi On: Navigate to the appropriate settings menu and successfully enable WiFi, connecting to a provided Access Point.
"""
import os
import sys
import unittest

from time import sleep

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, Apps
from aptools.aputils import path, value, action, logging, wait_el_xpath, wait_els_xpath, wait_el_xpath_click, keycode, MobileSwipe


class Settings(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(app_name=Apps.SETTINGS, no_reset=True)
    self.swipe = MobileSwipe()

  def test_get_memory_status(self):
    prefix = 'test_get_memory_status'
    logging.info('{0}: START'.format(prefix))
    sleep(5)
    if wait_el_xpath_click(self.driver, path('settings', 'memory_path')):
      sleep(5)
      tv_total_memory = wait_el_xpath(self.driver, path('settings_memory', 'total_memory_path'))
      tv_used = wait_el_xpath(self.driver, path('settings_memory', 'used_path'))
      logging.info(value(tv_used, Commands.TEXT) + ' ' + value(tv_total_memory, Commands.TEXT))
      sleep(2)
      self.driver.back()
    else:
      self.fail('{0}: Memory load unsucceed.'.format(prefix))
    logging.info('{0}: END'.format(prefix))

  def initB(self):
    """
    Init bluetooth and return the bluetooth switch button.
    """
    app = 'settings_bluetooth'
    wait_el_xpath_click(self.driver, path('settings', 'bluetooth_path'))
    wait_el_xpath_click(self.driver, path(app, 'bluetooth_index_path'))
    switch_bluetooth = wait_el_xpath(self.driver, path(app, 'switch_bluetooth_path'))
    return switch_bluetooth

  def test_bluetooth_disable(self):
    app = 'settings_bluetooth'
    prefix = 'test_bluetooth_disable'
    logging.info('{0}: START'.format(prefix))
    switch_bluetooth = self.initB()
    if switch_bluetooth is None:
      self.fail('{0}: Bluetooth Switch load unsucceed.'.format(prefix))

    if value(switch_bluetooth, Commands.TEXT) == path(app, 'bluetooth_enabled'):
      action(switch_bluetooth, Commands.CLICK)
      logging.info('{0}: Bluetooth disable succeed.'.format(prefix))
    else:
      logging.info('{0}: Bluetooth is already disabled.'.format(prefix))
    self.driver.back()
    self.driver.back()
    logging.info('{0}: END'.format(prefix))

  def test_bluetooth_enable(self):
    app = 'settings_bluetooth'
    prefix = 'test_bluetooth_enable'
    logging.info('{0}: START'.format(prefix))
    switch_bluetooth = self.initB()
    if switch_bluetooth is None:
      self.fail('{0}: Bluetooth Switch load unsucceed.'.format(prefix))

    if value(switch_bluetooth, Commands.TEXT) == path(app, 'bluetooth_disabled'):
      action(switch_bluetooth, Commands.CLICK)
      logging.info('{0}: Bluetooth enable succeed.'.format(prefix))
    else:
      logging.info('{0}: Bluetooth is already enabled.'.format(prefix))

    sleep(5)
    while True:
      if wait_el_xpath_click(self.driver, path(app, 'btn_devices_1st_settings'), 3):
        wait_el_xpath_click(self.driver, path(app, 'btn_foget_path'))
        logging.info('{0}: Forget remmerbered devices.'.format(prefix))
        sleep(2)
      else:
        break

    wait_el_xpath_click(self.driver, path(app, 'pair_new_device_path'))
    if wait_el_xpath_click(self.driver, path(app, 'headset_path'), 3):
      sleep(8)
      wait_el_xpath_click(self.driver, path(app, 'btn_pair'))
      sleep(8)
      if wait_el_xpath(self.driver, path(app, 'available_devices_path'), 3) is not None:
        logging.info('{0}: Pair with {1} unsucceed, Headset no response.'.format(prefix, path(app, 'headset_name')))
        self.fail('{0}: Pair with {1} unsucceed, Headset no response.'.format(prefix, path(app, 'headset_name')))
    else:
      self.fail('{0}: There is not a headset named {1}.'.format(prefix, path(app, 'headset_name')))

    if wait_el_xpath(self.driver, path(app, 'btn_devices_1st_settings'), 3) is None:
      logging.info('{0}: Pair with {1} unsucceed.'.format(prefix, path(app, 'headset_name')))
      self.fail('{0}: {1} not found.'.format(prefix, path(app, 'btn_devices_settings')))
    else:
      logging.info('{0}: Pair with {1} succeed.'.format(prefix, path(app, 'headset_name')))
    self.driver.back()
    self.driver.back()
    logging.info('{0}: END'.format(prefix))

  def initW(self):
    """
    Init wlan and return the wlan switch button.
    """
    app = 'settings_wlan'
    wait_el_xpath_click(self.driver, path('settings', 'wlan_path'))
    wait_el_xpath_click(self.driver, path(app, 'wlan_index_path'))
    switch_wlan = wait_el_xpath(self.driver, path(app, 'switch_wlan_path'))
    return switch_wlan

  def test_wlan_disable(self):
    app = 'settings_wlan'
    prefix = 'test_wlan_disable'
    logging.info('{0}: START'.format(prefix))
    switch_wlan = self.initW()
    if switch_wlan is None:
      self.fail('{0}: WLAN Switch load unsucceed.'.format(prefix))

    if value(switch_wlan, Commands.TEXT) == path(app, 'wlan_enabled'):
      action(switch_wlan, Commands.CLICK)
      logging.info('{0}: WLAN disable succeed.'.format(prefix))
    else:
      logging.info('{0}: WLAN is already disabled.'.format(prefix))
    self.driver.back()
    self.driver.back()
    logging.info('{0}: END'.format(prefix))

  def test_wlan_enable(self):
    app = 'settings_wlan'
    prefix = 'test_wlan_enable'
    logging.info('{0}: START'.format(prefix))
    switch_wlan = self.initW()
    if switch_wlan is None:
      self.fail('{0}: WLAN Switch load unsucceed.'.format(prefix))

    if value(switch_wlan, Commands.TEXT) == path(app, 'wlan_disabled'):
      action(switch_wlan, Commands.CLICK)
      logging.info('{0}: WLAN enable succeed.'.format(prefix))
      sleep(5)
    else:
      logging.info('{0}: WLAN is already enabled.'.format(prefix))
      sleep(3)
    
    ap_connected = wait_el_xpath(self.driver, path(app, 'ap_connected_path'))
    if ap_connected is not None:
      action(ap_connected, Commands.CLICK)
      wait_el_xpath_click(self.driver, path(app, 'ap_forget_path'))

    sleep(3)
    swipe_times=10

    while True:
      ap_point = wait_el_xpath(self.driver, path(app, 'ap_point_path'), 3)
      if ap_point is None:
        add_network = wait_el_xpath(self.driver, path(app, 'add_network_path'), 3)
        if add_network is None:
          if swipe_times!=0:
            swipe_times = swipe_times-1
            logging.info('{0}: AP did not found'.format(prefix))
            logging.info("{0}: Try swipe up to find the AP '{1}', times: {2}".format(prefix, path(app, 'ap_point_name'), 10-swipe_times))
            MobileSwipe.swipe_up(self, self.driver, 800)
            sleep(1)
            continue
          else:
            logging.info('{0}: There is no AP named {1}'.format(prefix, path(app, 'ap_point_name')))
            break
        else:
          action(add_network, Commands.CLICK)
          logging.info('{0}: Try to add network manually.'.format(prefix))
          et_ssid = wait_el_xpath(self.driver, path(app, 'et_ssid_path'))
          action(et_ssid, Commands.CLICK)
          action(et_ssid, Commands.CLEAR)
          action(et_ssid, Commands.SEND_KEYS, path(app, 'ap_point_name'))

          wait_el_xpath_click(self.driver, path(app, 'spinner_security_path'))
          wait_el_xpath_click(self.driver, path(app, 'wpa_security_path'))
          wait_el_xpath_click(self.driver, path(app, 'checkbox_pw_show_path'))
          et_pw = wait_el_xpath(self.driver, path(app, 'et_pw_path'))
          action(et_pw, Commands.CLICK)
          action(et_pw, Commands.CLICK)

          # password: 173925239
          password_str = path(app, 'ap_password')
          for s in password_str:
            self.driver.press_keycode(keycode(int(s)))
          wait_el_xpath_click(self.driver, path(app, 'btn_save_path'))
          sleep(2)
          break
      else:
        action(ap_point, Commands.CLICK)
        wait_el_xpath_click(self.driver, path(app, 'checkbox_pw_show_path'))
        et_pw = wait_el_xpath(self.driver, path(app, 'et_pw_path'))
        action(et_pw, Commands.CLICK)
        action(et_pw, Commands.CLEAR)
        # password: 173925239
        password_str = path(app, 'ap_password')
        for s in password_str:
          self.driver.press_keycode(keycode(int(s)))
        wait_el_xpath_click(self.driver, path(app, 'btn_connect_path'))
        sleep(1)
        break

    sleep(8)
    self.driver.back()
    sleep(8)
    wifi_status = wait_el_xpath(self.driver, path(app, 'wifi_status_path'))
    if value(wifi_status, Commands.TEXT) == path(app, 'ap_point_name'):
      logging.info('{0}: WLAN connect succeed.'.format(prefix))
    else:
      logging.info('{0}: WLAN connect unsucceed.'.format(prefix))
      self.fail('{0}: WLAN connect unsucceed.'.format(prefix))
    sleep(2)
    self.driver.back()
    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()