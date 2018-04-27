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
from common.utils import wait_el_xpath, wait_el_xpath_click, MobileSwipe

class Settings(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Settings')
    self.MobileSwipe = MobileSwipe()

  def test_getMemoryStatus(self):
    MobileSwipe.swipe_down(self, self.driver, 400)
    wait_el_xpath_click(self.driver, cfg.get('settings', 'memory_path'))
    tv_performance = wait_el_xpath(self.driver, cfg.get('settings_memory', 'performance_path'))
    tv_total_memory = wait_el_xpath(self.driver, cfg.get('settings_memory', 'total_memory_path'))
    tv_average_used = wait_el_xpath(self.driver, cfg.get('settings_memory', 'average_used_path'))
    tv_free = wait_el_xpath(self.driver, cfg.get('settings_memory', 'free_path'))
    logging.info(tv_performance.text)
    logging.info(tv_total_memory.text)
    logging.info(tv_average_used.text)
    logging.info(tv_free.text)
    sleep(2)
    self.driver.back()
    MobileSwipe.swipe_up(self, self.driver, 400)

  def test_bluetoothDisable(self):
    wait_el_xpath_click(self.driver, cfg.get('settings', 'bluetooth_path'))
    switch_bluetooth = wait_el_xpath(self.driver, cfg.get('settings_bluetooth', 'switch_bluetooth_path'))
    
    if switch_bluetooth.text == cfg.get('settings_bluetooth', 'bluetooth_enabled'):
      switch_bluetooth.click()
    else:
      logging.info('Bluetooth is already disabled.')
    self.driver.back()

  def test_bluetoothEnable(self):
    wait_el_xpath_click(self.driver, cfg.get('settings', 'bluetooth_path'))
    switch_bluetooth = wait_el_xpath(self.driver, cfg.get('settings_bluetooth', 'switch_bluetooth_path'))

    if switch_bluetooth.text == cfg.get('settings_bluetooth', 'bluetooth_disabled'):
      switch_bluetooth.click()
      switch_bluetooth.is_displayed()
    else:
      logging.info('Bluetooth is already enabled.')

    sleep(10)
    wait_el_xpath_click(self.driver, cfg.get('settings_bluetooth', 'headset_path'))
    wait_el_xpath_click(self.driver, cfg.get('settings_bluetooth', 'btn_pair'))
    sleep(10)
    self.driver.back()

  def test_wlanDisable(self):
    wait_el_xpath_click(self.driver, cfg.get('settings', 'wlan_path'))
    switch_wlan = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'switch_bluetooth_path'))
    
    if switch_wlan.text == cfg.get('settings_wlan', 'wlan_enabled'):
      switch_wlan.click()
    else:
      logging.info('WLAN is already disabled.')
    self.driver.back()

  def test_wlanEnable(self):
    wait_el_xpath_click(self.driver, cfg.get('settings', 'wlan_path'))
    switch_wlan = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'switch_bluetooth_path'))
    
    if switch_wlan.text == cfg.get('settings_wlan', 'wlan_disabled'):
      switch_wlan.click()
    else:
      logging.info('WLAN is already enabled.')

    sleep(3)
    wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'ap_point_path'))
    wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'checkbox_pw_show_path'))
    et_pw = wait_el_xpath(self.driver, cfg.get('settings_wlan', 'edit_text_pw_path'))
    et_pw.clear()
    # 输入密码
    # et_pw.send_keys('173925239')
    self.driver.press_keycode(8)
    self.driver.press_keycode(14)
    self.driver.press_keycode(10)
    self.driver.press_keycode(16)
    self.driver.press_keycode(9)
    self.driver.press_keycode(12)
    self.driver.press_keycode(9)
    self.driver.press_keycode(10)
    self.driver.press_keycode(16)
    wait_el_xpath_click(self.driver, cfg.get('settings_wlan', 'btn_connect_path'))
    sleep(1)
    self.driver.back()

  @classmethod
  def tearDownClass(self):
    self.driver.quit()