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
from common.utils import wait_el_xpath, wait_el_xpath_click, get_keycode

class Messaging(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Messaging')

  def initM(self):
    """
    Init messaging's recipients and make text editor prepared
    """
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'btn_create_path'))
    recipients = wait_el_xpath(self.driver, cfg.get('messaging', 'recipients_path'))
    recipients.clear()

    # phone number: 147 8230 5348
    num = [
      get_keycode(1), get_keycode(4), get_keycode(7),
      get_keycode(8), get_keycode(2), get_keycode(3), get_keycode(0), 
      get_keycode(5), get_keycode(3), get_keycode(4), get_keycode(8)
    ]
    for n in num:
      self.driver.press_keycode(n)

    text_editor = wait_el_xpath(self.driver, cfg.get('messaging', 'text_editor_path'))
    return text_editor

  def test_SMS_Mo(self):
    logging.info('test_SMS_Mo: START')

    text_editor = self.initM()
    
    btn_send_sms = wait_el_xpath(self.driver, cfg.get('messaging', 'btn_send_sms_path'))
    text_editor.click()
    text_editor.send_keys(cfg.get('default', 'default_msg'))
    btn_send_sms.click()
    logging.info('test_SMS_Mo: Send a SMS.')
    sleep(5)
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'navigate_up_path'))
    logging.info('test_SMS_Mo: END')

  def test_MMS_MO(self):
    logging.info('test_MMS_MO: START')

    text_editor = self.initM()

    wait_el_xpath_click(self.driver, cfg.get('messaging', 'add_attach_path'))
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'attach_subject_path'))
    et_subject = wait_el_xpath(self.driver, cfg.get('messaging', 'et_subject_path'))
    et_subject.send_keys(cfg.get('default', 'default_subject'))
    text_editor.click()
    text_editor.send_keys(cfg.get('default', 'default_msg'))
    btn_send_mms = wait_el_xpath(self.driver, cfg.get('messaging', 'btn_send_mms_path'))
    btn_send_mms.click()
    logging.info('test_SMS_Mo: Send a MMS.')
    sleep(5)
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'navigate_up_path'))
    logging.info('test_MMS_MO: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()