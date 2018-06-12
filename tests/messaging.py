# -*- coding:utf-8 -*-
"""
10. Receive MMS And Reply: Receive an MMS message (or RCS File Transfer, if RCS compatible) from the reference device, then send a MMS (or RCS File Transfer) response.
12. Receive SMS And Reply: Receive an SMS message (or RCS Chat, if RCS compatible) from the reference device, then send a SMS (or RCS Chat) response.
"""
import os
import sys
import unittest

from time import sleep

sys.path.append("..")
from server import appium_config
from tools.constants import Commands, Keycode, C_Messaging
from tools.utils import action, logging, wait_el_xpath, wait_el_xpath_click

class Messaging(unittest.TestCase):
  """
  APP: MESSAGING\n
  TEST CASE: test_SMS_MO, test_MMS_MO, test_SMS_MT, test_MMS_MT
  """
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(app=C_Messaging.APP, auto_grant_permissions=False)

  @classmethod
  def setUp(self):
    self.driver.launch_app()

  def initM(self, num):
    """
    Init messaging's recipients and make text editor prepared
    """
    prefix = C_Messaging.PREFIX
    if not wait_el_xpath_click(self.driver, C_Messaging.PATH_BTN_CREATE):
      logging.info('{0}: Create new message unsucceed.'.format(prefix))
      self.fail('{0}: Create new message unsucceed.'.format(prefix))
    recipients = wait_el_xpath(self.driver, C_Messaging.PATH_RECIPIENTS)
    action(recipients, Commands.CLEAR)
    action(recipients, Commands.CLICK)

    # phone number: 147 8230 5348
    for s in num:
      self.driver.press_keycode(Keycode.get(self, s))

    self.driver.press_keycode(Keycode.ENTER)

    text_editor = wait_el_xpath(self.driver, C_Messaging.PATH_TEXT_EDITOR)
    return text_editor

  def test_SMS_MO(self):
    prefix = C_Messaging.PREFIX_O
    logging.info('{0}: START'.format(prefix))

    text_editor = self.initM(C_Messaging.REF_PHONE_NUM)
    if text_editor is None:
      logging.info('{0}: Text editor load unsucceed.'.format(prefix))
      self.fail('{0}: Text editor load unsucceed.'.format(prefix))
    else:
      btn_send_sms = wait_el_xpath(self.driver, C_Messaging.PATH_BTN_SEND_SMS)
      action(text_editor, Commands.CLICK)
      action(text_editor, Commands.SEND_KEYS, C_Messaging.DEFAULT_MSG)
      action(btn_send_sms, Commands.CLICK)
      logging.info('{0}: Send a SMS to reference phone.'.format(prefix))
      sleep(10)
      self.driver.back()
      logging.info('{0}: END'.format(prefix))

  def test_MMS_MO(self):
    prefix = C_Messaging.PREFIX_T
    logging.info('{0}: START'.format(prefix))

    text_editor = self.initM(C_Messaging.REF_PHONE_NUM)

    if text_editor is None:
      logging.info('{0}: Text editor load unsucceed.'.format(prefix))
      self.fail('{0}: Text editor load unsucceed.'.format(prefix))
    else:
      wait_el_xpath_click(self.driver, C_Messaging.PATH_ADD_ATTACH)
      wait_el_xpath_click(self.driver, C_Messaging.PATH_ATTACH_SUBJECT)
      et_subject = wait_el_xpath(self.driver, C_Messaging.PATH_ET_SUBJECT)
      action(et_subject, Commands.SEND_KEYS, C_Messaging.DEFAULT_SUBJECT)
      action(text_editor, Commands.CLICK)
      action(text_editor, Commands.SEND_KEYS, C_Messaging.DEFAULT_MSG)
      btn_send_mms = wait_el_xpath(self.driver, C_Messaging.PATH_BTN_SEND_MMS)
      action(btn_send_mms, Commands.CLICK)
      logging.info('{0}: Send a MMS to reference phone.'.format(prefix))
      sleep(10)
      self.driver.back()
      logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDown(self):
    self.driver.close_app()

  @classmethod
  def tearDownClass(self):
    self.driver.quit()