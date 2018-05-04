# -*- coding:utf-8 -*-
"""
10. Receive MMS And Reply: Receive an MMS message (or RCS File Transfer, if RCS compatible) from the reference device, then send a MMS (or RCS File Transfer) response.
12. Receive SMS And Reply: Receive an SMS message (or RCS Chat, if RCS compatible) from the reference device, then send a SMS (or RCS Chat) response.
"""
import os
import unittest

from time import sleep
from appium import webdriver
from conf.appium_config import cfg, logging
from conf import appium_config
from common.utils import wait_el_xpath, wait_el_xpath_click

class Messaging(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Messaging')

  def test_SMS_Mo(self):
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'btn_create_path'))
    recipients = wait_el_xpath(self.driver, cfg.get('messaging', 'recipients_path'))
    text_editor = wait_el_xpath(self.driver, cfg.get('messaging', 'text_editor_path'))
    btn_send_sms = wait_el_xpath(self.driver, cfg.get('messaging', 'btn_send_sms_path'))
    recipients.clear()
    self.driver.press_keycode(8)
    self.driver.press_keycode(11)
    self.driver.press_keycode(14)
    self.driver.press_keycode(15)
    self.driver.press_keycode(9)
    self.driver.press_keycode(10)
    self.driver.press_keycode(7)
    self.driver.press_keycode(12)
    self.driver.press_keycode(10)
    self.driver.press_keycode(11)
    self.driver.press_keycode(15)
    self.driver.press_keycode(66)
    text_editor.click()
    text_editor.send_keys(cfg.get('default', 'default_msg'))
    btn_send_sms.click()
    sleep(5)
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'navigate_up_path'))

  def test_MMS_MO(self):
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'btn_create_path'))
    recipients = wait_el_xpath(self.driver, cfg.get('messaging', 'recipients_path'))
    recipients.clear()
    self.driver.press_keycode(8)
    self.driver.press_keycode(11)
    self.driver.press_keycode(14)
    self.driver.press_keycode(15)
    self.driver.press_keycode(9)
    self.driver.press_keycode(10)
    self.driver.press_keycode(7)
    self.driver.press_keycode(12)
    self.driver.press_keycode(10)
    self.driver.press_keycode(11)
    self.driver.press_keycode(15)
    self.driver.press_keycode(66)
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'add_attach_path'))
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'attach_subject_path'))
    et_subject = wait_el_xpath(self.driver, cfg.get('messaging', 'et_subject_path'))
    text_editor = wait_el_xpath(self.driver, cfg.get('messaging', 'text_editor_path'))
    et_subject.send_keys(cfg.get('default', 'default_subject'))
    text_editor.click()
    text_editor.send_keys(cfg.get('default', 'default_msg'))
    btn_send_mms = wait_el_xpath(self.driver, cfg.get('messaging', 'btn_send_mms_path'))
    btn_send_mms.click()
    sleep(5)
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'navigate_up_path'))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()