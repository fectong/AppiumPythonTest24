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
from aptools.apconstants import Commands, C_Settings, C_Memorry, C_Bluetooth, C_WLAN
from aptools.aputils import value, action, logging, wait_el_xpath, wait_els_xpath, wait_el_xpath_click, keycode, MobileSwipe


class Settings(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(C_Settings.APP)
    self.swipe = MobileSwipe()

  @classmethod
  def setUp(self):
    self.driver.launch_app()

  def test_get_memory_status(self):
    prefix = C_Memorry.PREFIX
    logging.info('{0}: START'.format(prefix))
    sleep(5)
    if wait_el_xpath_click(self.driver, C_Settings.PATH_MEMORY):
      sleep(5)
      tv_total_memory = wait_el_xpath(self.driver, C_Memorry.PATH_TOTAL_MEMORY)
      tv_used = wait_el_xpath(self.driver, C_Memorry.PATH_USED)
      logging.info(value(tv_used, Commands.TEXT) + ' ' + value(tv_total_memory, Commands.TEXT))
      sleep(2)
      # self.driver.back()
    else:
      self.fail('{0}: Memory load unsucceed.'.format(prefix))
    logging.info('{0}: END'.format(prefix))

  def initB(self):
    """
    Init bluetooth and return the bluetooth switch button.
    """
    wait_el_xpath_click(self.driver, C_Settings.PATH_BLUETOOTH)
    wait_el_xpath_click(self.driver, C_Bluetooth.PATH_BLUETOOTH_INDEX)
    switch_bluetooth = wait_el_xpath(self.driver, C_Bluetooth.PATH_SWITCH_BLUETOOTH)
    return switch_bluetooth

  def test_bluetooth_disable(self):

    prefix = C_Bluetooth.PREFIX_D
    logging.info('{0}: START'.format(prefix))
    switch_bluetooth = self.initB()
    if switch_bluetooth is None:
      self.fail('{0}: Bluetooth Switch load unsucceed.'.format(prefix))

    if value(switch_bluetooth, Commands.TEXT) == C_Bluetooth.BLUETOOTH_ENABLED:
      action(switch_bluetooth, Commands.CLICK)
      logging.info('{0}: Bluetooth disable succeed.'.format(prefix))
    else:
      logging.info('{0}: Bluetooth is already disabled.'.format(prefix))
    # self.driver.back()
    # self.driver.back()
    logging.info('{0}: END'.format(prefix))

  def test_bluetooth_enable(self):
    
    headset_name = C_Bluetooth.HEADSET_NAME
    prefix = C_Bluetooth.PREFIX_E
    logging.info('{0}: START'.format(prefix))
    switch_bluetooth = self.initB()
    if switch_bluetooth is None:
      self.fail('{0}: Bluetooth Switch load unsucceed.'.format(prefix))

    if value(switch_bluetooth, Commands.TEXT) == C_Bluetooth.BLUETOOTH_DISABLED:
      action(switch_bluetooth, Commands.CLICK)
      logging.info('{0}: Bluetooth enable succeed.'.format(prefix))
    else:
      logging.info('{0}: Bluetooth is already enabled.'.format(prefix))

    sleep(5)
    while True:
      if wait_el_xpath_click(self.driver, C_Bluetooth.PATH_DEVICES_1ST_SETTINGS, 3):
        wait_el_xpath_click(self.driver, C_Bluetooth.PATH_BTN_FOGET)
        logging.info('{0}: Forget remmerbered devices.'.format(prefix))
        sleep(2)
      else:
        break

    wait_el_xpath_click(self.driver, C_Bluetooth.PATH_PAIR_NEW_DEVICE)
    if wait_el_xpath_click(self.driver, C_Bluetooth.PATH_HEADSET):
      sleep(8)
      wait_el_xpath_click(self.driver, C_Bluetooth.PATH_BTN_PAIR)
      sleep(8)
      if wait_el_xpath(self.driver, C_Bluetooth.PATH_AVAILABLE_DEVICES, 3) is not None:
        logging.info('{0}: Pair with {1} unsucceed, Headset no response.'.format(prefix, headset_name))
        self.fail('{0}: Pair with {1} unsucceed, Headset no response.'.format(prefix, headset_name))
    else:
      self.fail('{0}: There is not a headset named {1}.'.format(prefix, headset_name))

    if wait_el_xpath(self.driver, C_Bluetooth.PATH_DEVICES_1ST_SETTINGS, 3) is None:
      logging.info('{0}: Pair with {1} unsucceed.'.format(prefix, headset_name))
      self.fail('{0}: {1} not found.'.format(prefix, C_Bluetooth.PATH_DEVICES_1ST_SETTINGS))
    else:
      logging.info('{0}: Pair with {1} succeed.'.format(prefix, headset_name))
    # self.driver.back()
    # self.driver.back()
    logging.info('{0}: END'.format(prefix))

  def initW(self):
    """
    Init wlan and return the wlan switch button.
    """
    wait_el_xpath_click(self.driver, C_Settings.PATH_WLAN)
    wait_el_xpath_click(self.driver, C_WLAN.PATH_WLAN_INDEX)
    switch_wlan = wait_el_xpath(self.driver, C_WLAN.PATH_SWITCH_WLAN)
    return switch_wlan

  def test_wlan_disable(self):
    prefix = C_WLAN.PREFIX_D
    logging.info('{0}: START'.format(prefix))
    switch_wlan = self.initW()
    if switch_wlan is None:
      self.fail('{0}: WLAN Switch load unsucceed.'.format(prefix))

    if value(switch_wlan, Commands.TEXT) == C_WLAN.WLAN_ENABLED:
      action(switch_wlan, Commands.CLICK)
      logging.info('{0}: WLAN disable succeed.'.format(prefix))
    else:
      logging.info('{0}: WLAN is already disabled.'.format(prefix))
    # self.driver.back()
    # self.driver.back()
    logging.info('{0}: END'.format(prefix))

  def test_wlan_enable(self):
    ap_point_name = C_WLAN.AP_POINT_NAME
    prefix = C_WLAN.PREFIX_E
    logging.info('{0}: START'.format(prefix))
    switch_wlan = self.initW()
    if switch_wlan is None:
      self.fail('{0}: WLAN Switch load unsucceed.'.format(prefix))

    if value(switch_wlan, Commands.TEXT) == C_WLAN.WLAN_DISABLED:
      action(switch_wlan, Commands.CLICK)
      logging.info('{0}: WLAN enable succeed.'.format(prefix))
      sleep(5)
    else:
      logging.info('{0}: WLAN is already enabled.'.format(prefix))
      sleep(3)
    
    ap_connected = wait_el_xpath(self.driver, C_WLAN.PATH_AP_CONNECTED)
    if ap_connected is not None:
      action(ap_connected, Commands.CLICK)
      wait_el_xpath_click(self.driver, C_WLAN.PATH_AP_FORGET)

    sleep(3)
    swipe_times=10

    while True:
      ap_point = wait_el_xpath(self.driver, C_WLAN.PATH_AP_POINT, 3)
      if ap_point is None:
        add_network = wait_el_xpath(self.driver, C_WLAN.PATH_ADD_NETWORK, 3)
        if add_network is None:
          if swipe_times!=0:
            swipe_times = swipe_times-1
            logging.info('{0}: AP did not found'.format(prefix))
            logging.info("{0}: Try swipe up to find the AP '{1}', times: {2}".format(prefix, ap_point_name, 10-swipe_times))
            MobileSwipe.swipe_up(self, self.driver, 800)
            sleep(1)
            continue
          else:
            logging.info('{0}: There is no AP named {1}'.format(prefix, ap_point_name))
            break
        else:
          action(add_network, Commands.CLICK)
          logging.info('{0}: Try to add network manually.'.format(prefix))
          et_ssid = wait_el_xpath(self.driver, C_WLAN.PATH_ET_SSID)
          action(et_ssid, Commands.CLICK)
          action(et_ssid, Commands.CLEAR)
          action(et_ssid, Commands.SEND_KEYS, ap_point_name)

          wait_el_xpath_click(self.driver, C_WLAN.PATH_SPINNER_SECURITY)
          wait_el_xpath_click(self.driver, C_WLAN.PATH_WPA_SECURITY)
          wait_el_xpath_click(self.driver, C_WLAN.PATH_CHECKBOX_PW_SHOW)
          et_pw = wait_el_xpath(self.driver, C_WLAN.PATH_ET_PW)
          action(et_pw, Commands.CLICK)
          action(et_pw, Commands.CLICK)

          # password: 173925239
          password_str = C_WLAN.AP_PASSWORD
          for s in password_str:
            self.driver.press_keycode(keycode(int(s)))
          wait_el_xpath_click(self.driver, C_WLAN.PATH_BTN_SAVE)
          sleep(2)
          break
      else:
        action(ap_point, Commands.CLICK)
        wait_el_xpath_click(self.driver, C_WLAN.PATH_CHECKBOX_PW_SHOW)
        et_pw = wait_el_xpath(self.driver, C_WLAN.PATH_ET_PW)
        action(et_pw, Commands.CLICK)
        action(et_pw, Commands.CLEAR)
        # password: 173925239
        password_str = C_WLAN.AP_PASSWORD
        for s in password_str:
          self.driver.press_keycode(keycode(int(s)))
        wait_el_xpath_click(self.driver, C_WLAN.PATH_BTN_CONNECT)
        sleep(1)
        break

    sleep(8)
    self.driver.back()
    sleep(8)
    wifi_status = wait_el_xpath(self.driver, C_WLAN.PATH_WLAN_STATUS)
    if value(wifi_status, Commands.TEXT) == ap_point_name:
      logging.info('{0}: WLAN connect succeed.'.format(prefix))
    else:
      logging.info('{0}: WLAN connect unsucceed.'.format(prefix))
      self.fail('{0}: WLAN connect unsucceed.'.format(prefix))
    sleep(2)
    # self.driver.back()
    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDown(self):
    sleep(3)
    self.driver.close_app()

  @classmethod
  def tearDownClass(self):
    self.driver.quit()