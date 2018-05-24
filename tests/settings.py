# -*- coding:utf-8 -*-
"""
01. Get Phone Memory Status: Get the phone’s current memory status from the settings menu(this is mostly for post analysis upon instability)
14. Turn Bluetooth Off: Navigate to the appropriate settings menu and successfully disable Bluetooth.
15. Turn Bluetooth On: Navigate to the appropriate settings menu and successfully enable Bluetooth and pair to a provided headset.
16. Turn WiFi Off: Navigate to the appropriate settings menu and successfully disable WiFi.
17. Turn WiFi On: Navigate to the appropriate settings menu and successfully enable WiFi, connecting to a provided Access Point.
"""
import os
import unittest

from time import sleep
from appium import webdriver
from conf import appium_config
from conf.appium_config import cfg, logging
from common.utils import wait_el_xpath, wait_el_xpath_click, get_keycode, MobileSwipe
from selenium.common.exceptions import TimeoutException


class Settings(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Settings')
    self.swipe = MobileSwipe()

  def test_get_memory_status(self):
    logging.info('test_get_memory_status: START')
    sleep(5)
    wait_el_xpath_click(self.driver, cfg.get('settings', 'memory_path'))
    sleep(5)
    tv_total_memory = wait_el_xpath(self.driver, cfg.get('settings_memory', 'total_memory_path'))
    tv_used = wait_el_xpath(self.driver, cfg.get('settings_memory', 'used_path'))
    logging.info(tv_used.text + ' ' + tv_total_memory.text)
    sleep(2)
    self.driver.back()
    logging.info('test_get_memory_status: END')

  def initB(self):
    """
    Init bluetooth and return the bluetooth switch button.
    """
    wait_el_xpath_click(self.driver, cfg.get('settings', 'bluetooth_path'))
    wait_el_xpath_click(self.driver, cfg.get('settings_bluetooth', 'bluetooth_index_path'))
    switch_bluetooth = wait_el_xpath(self.driver, cfg.get('settings_bluetooth', 'switch_bluetooth_path'))
    return switch_bluetooth

  def test_bluetooth_disable(self):
    logging.info('test_bluetooth_disable: START')

    switch_bluetooth = self.initB()
    
    if switch_bluetooth.text == cfg.get('settings_bluetooth', 'bluetooth_enabled'):
      switch_bluetooth.click()
      logging.info('test_bluetooth_disable: Bluetooth disable succeed.')
    else:
      logging.info('test_bluetooth_disable: Bluetooth is already disabled.')
    self.driver.back()
    self.driver.back()
    logging.info('test_bluetooth_disable: END')

  def test_bluetooth_enable(self):
    logging.info('test_bluetooth_enable: START')

    switch_bluetooth = self.initB()

    if switch_bluetooth.text == cfg.get('settings_bluetooth', 'bluetooth_disabled'):
      switch_bluetooth.click()
      logging.info('test_bluetooth_enable: Bluetooth enable succeed.')
    else:
      logging.info('test_bluetooth_enable: Bluetooth is already enabled.')

    sleep(10)
    wait_el_xpath_click(self.driver, cfg.get('settings_bluetooth', 'headset_path'))
    wait_el_xpath_click(self.driver, cfg.get('settings_bluetooth', 'headset_path'))
    wait_el_xpath_click(self.driver, cfg.get('settings_bluetooth', 'btn_pair'))
    sleep(10)
    self.driver.back()
    self.driver.back()
    logging.info('test_bluetooth_enable: END')

  def initW(self):
    """
    Init wlan and return the wlan switch button.
    """
    wait_el_xpath_click(self.driver, cfg.get('settings', 'wlan_path'))
    wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'wlan_index_path'))
    switch_wlan = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'switch_wlan_path'))
    return switch_wlan

  def test_wlan_disable(self):
    logging.info('test_wlan_disable: START')
    switch_wlan = self.initW()
    
    if switch_wlan.text == cfg.get('settings_wlan', 'wlan_enabled'):
      switch_wlan.click()
      logging.info('test_wlan_disable: WLAN disable succeed.')
    else:
      logging.info('test_wlan_disable: WLAN is already disabled.')
    self.driver.back()
    self.driver.back()
    logging.info('test_wlan_disable: END')

  def test_wlan_enable(self):
    logging.info('test_wlan_enable: START')
    switch_wlan = self.initW()
    
    if switch_wlan.text == cfg.get('settings_wlan', 'wlan_disabled'):
      switch_wlan.click()
      logging.info('test_wlan_enable: WLAN enable succeed.')
      sleep(5)
    else:
      logging.info('test_wlan_enable: WLAN is already enabled.')
      sleep(3)
    
    ap_connected = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'ap_connected_path'))
    if ap_connected is not None:
      ap_connected.click()
      wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'ap_forget_path'))

    sleep(3)
    swipe_times=10

    while True:
      ap_point = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'ap_point_path'), 3)
      if ap_point is None:
        add_network = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'add_network_path'), 3)
        if add_network is None:
          if swipe_times!=0:
            swipe_times = swipe_times-1
            logging.info('test_wlan_enable: AP did not found')
            logging.info("test_wlan_enable: Try swipe up to find the AP '{0}', times: {1}".format(cfg.get('settings_wlan', 'ap_point_name'), 10-swipe_times))
            MobileSwipe.swipe_up(self, self.driver, 800)
            sleep(1)
            continue
          else:
            logging.info('test_wlan_enable: There is no AP named {0}'.format(cfg.get('settings_wlan', 'ap_point_name')))
            break
        else:
          add_network.click()
          logging.info('test_wlan_enable: Try to add network manually.')
          et_ssid = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'et_ssid_path'))
          et_ssid.click()
          et_ssid.clear()
          et_ssid.send_keys(cfg.get('settings_wlan', 'ap_point_name'))

          wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'spinner_security_path'))
          wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'wpa_security_path'))
          wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'checkbox_pw_show_path'))
          et_pw = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'et_pw_path'))
          et_pw.click()
          et_pw.clear()

          # password: 173925239
          password_str = cfg.get('settings_wlan', 'ap_password')
          for s in password_str:
            self.driver.press_keycode(get_keycode(int(s)))
          wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'btn_save_path'))
          sleep(2)
          break
      else:
        ap_point.click()
        wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'checkbox_pw_show_path'))
        et_pw = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'et_pw_path'))
        et_pw.click()
        et_pw.clear()
        # password: 173925239
        password_str = cfg.get('settings_wlan', 'ap_password')
        for s in password_str:
          self.driver.press_keycode(get_keycode(int(s)))
        wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'btn_connect_path'))
        sleep(1)
        break

    sleep(8)
    self.driver.back()
    sleep(8)
    wifi_status = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'wifi_status_path'))
    if wifi_status.text == cfg.get('settings_wlan', 'ap_point_name'):
      logging.info('test_wlan_enable: WLAN connect succeed.')
    else:
      logging.info('test_wlan_enable: WLAN connect unsucceed.')
      logging.info('test_wlan_enable: END')
      self.fail('test_wlan_enable: WLAN connect unsucceed.')
    sleep(2)
    self.driver.back()
    logging.info('test_wlan_enable: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()