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
  """
  APP: MESSAGING\n
  TEST CASE: test_SMS_MO, test_MMS_MO, test_SMS_MT, test_MMS_MT
  """
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('Messaging')

  def initM(self, num):
    """
    Init messaging's recipients and make text editor prepared
    """
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'btn_create_path'))
    recipients = wait_el_xpath(self.driver, cfg.get('messaging', 'recipients_path'))
    recipients.clear()

    # phone number: 147 8230 5348
    phone_number_str = cfg.get('default', num)
    for s in phone_number_str:
      self.driver.press_keycode(get_keycode(int(s)))
    
    self.driver.press_keycode(get_keycode('ENTER'))
    
    text_editor = wait_el_xpath(self.driver, cfg.get('messaging', 'text_editor_path'))
    return text_editor

  def test_SMS_MO(self):
    logging.info('test_SMS_MO: START')

    text_editor = self.initM('phone_num')
    
    btn_send_sms = wait_el_xpath(self.driver, cfg.get('messaging', 'btn_send_sms_path'))
    text_editor.click()
    text_editor.send_keys(cfg.get('messaging', 'default_msg'))
    btn_send_sms.click()
    logging.info('test_SMS_MO: Send a SMS to reference phone.')
    sleep(5)
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'navigate_up_path'))
    logging.info('test_SMS_MO: END')

  def test_MMS_MO(self):
    logging.info('test_SMS_MO: START')

    text_editor = self.initM('phone_num')

    wait_el_xpath_click(self.driver, cfg.get('messaging', 'add_attach_path'))
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'attach_subject_path'))
    et_subject = wait_el_xpath(self.driver, cfg.get('messaging', 'et_subject_path'))
    et_subject.send_keys(cfg.get('messaging', 'default_subject'))
    text_editor.click()
    text_editor.send_keys(cfg.get('messaging', 'default_msg'))
    btn_send_mms = wait_el_xpath(self.driver, cfg.get('messaging', 'btn_send_mms_path'))
    btn_send_mms.click()
    logging.info('test_MMS_MO: Send a MMS to reference phone.')
    sleep(5)
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'navigate_up_path'))
    logging.info('test_MMS_MO: END')

  """
  def test_SMS_MT(self):
    logging.info('test_SMS_MT: START')
    text_editor = self.initM('phone_num')
    
    btn_send_sms = wait_el_xpath(self.driver, cfg.get('messaging', 'btn_send_sms_path'))
    text_editor.click()
    text_editor.send_keys(cfg.get('messaging', 'default_msg'))
    btn_send_sms.click()
    logging.info('test_SMS_MT: Send a SMS to DUT.')
    sleep(5)
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'navigate_up_path'))
    logging.info('test_SMS_MT: END')

  def test_MMS_MT(self):
    logging.info('test_MMS_MT: START')

    text_editor = self.initM('phone_num')

    wait_el_xpath_click(self.driver, cfg.get('messaging', 'add_attach_path'))
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'attach_subject_path'))
    et_subject = wait_el_xpath(self.driver, cfg.get('messaging', 'et_subject_path'))
    et_subject.send_keys(cfg.get('messaging', 'default_subject'))
    text_editor.click()
    text_editor.send_keys(cfg.get('messaging', 'default_msg'))
    btn_send_mms = wait_el_xpath(self.driver, cfg.get('messaging', 'btn_send_mms_path'))
    btn_send_mms.click()
    logging.info('test_MMS_MT: Send a MMS to DUT.')
    sleep(5)
    wait_el_xpath_click(self.driver, cfg.get('messaging', 'navigate_up_path'))
    logging.info('test_MMS_MT: END')
  """

  @classmethod
  def tearDownClass(self):
    self.driver.quit()