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
from common.utils import wait_el_xpath, wait_el_xpath_click, get_keycode
from selenium.common.exceptions import TimeoutException

class Settings(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Settings')

  def test_get_memory_status(self):
    logging.info('test_get_memory_status: START')
    wait_el_xpath_click(self.driver, cfg.get('settings', 'memory_path'))
    tv_total_memory = wait_el_xpath(self.driver, cfg.get('settings_memory', 'total_memory_path'))
    tv_used = wait_el_xpath(self.driver, cfg.get('settings_memory', 'used_path'))
    logging.info(tv_used.text + ' ' + tv_total_memory.text)
    sleep(1)
    self.driver.back()
    # wait_el_xpath_click(self.driver, cfg.get('settings', 'navigate_up_path'))
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
    else:
      logging.info('test_wlan_enable: WLAN is already enabled.')
    
    sleep(3)
    try:
      ap_connected = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'ap_connected_path'))
      ap_connected.click()
      wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'ap_forget_path'))
    except TimeoutException:
      logging.info('No ap connected.')

    sleep(3)
    ap_point = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'ap_point_path'))
    ap_point.click()
    wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'checkbox_pw_show_path'))
    et_pw = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'edit_text_pw_path'))
    et_pw.clear()
    
    # password: 173925239
    password_str = cfg.get('settings_wlan', 'ap_password')
    for s in password_str:
      self.driver.press_keycode(get_keycode(int(s)))
    
    wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'btn_connect_path'))
    logging.info('test_wlan_enable: WLAN connect succeed.')
    sleep(1)
    self.driver.back()
    self.driver.back()
    logging.info('test_wlan_enable: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()