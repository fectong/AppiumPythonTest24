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
from conf import appium_config
from aptools.apconstants import Commands, Apps
from aptools.aputils import path, action, logging, wait_el_xpath, wait_el_xpath_click, keycode

class Messaging(unittest.TestCase):
  """
  APP: MESSAGING\n
  TEST CASE: test_SMS_MO, test_MMS_MO, test_SMS_MT, test_MMS_MT
  """
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(app_name=Apps.MESSAGING, auto_grant_permissions=False)

  def initM(self, num):
    """
    Init messaging's recipients and make text editor prepared
    """
    app = 'messaging'
    prefix = 'test_SMS_M*'
    if not wait_el_xpath_click(self.driver, path(app, 'btn_create_path')):
      logging.info('{0}: Create new message unsucceed.'.format(prefix))
      self.fail('{0}: Create new message unsucceed.'.format(prefix))
    recipients = wait_el_xpath(self.driver, path(app, 'recipients_path'))
    action(recipients, Commands.CLEAR)

    # phone number: 147 8230 5348
    phone_number_str = path('default', num)
    for s in phone_number_str:
      self.driver.press_keycode(keycode(int(s)))

    self.driver.press_keycode(keycode(Commands.ENTER))

    text_editor = wait_el_xpath(self.driver, path(app, 'text_editor_path'))
    return text_editor

  def test_SMS_MO(self):
    app = 'messaging'
    prefix = 'test_SMS_MO'
    logging.info('{0}: START'.format(prefix))

    text_editor = self.initM('phone_num')
    if text_editor is None:
      logging.info('{0}: Text editor load unsucceed.'.format(prefix))
      self.fail('{0}: Text editor load unsucceed.'.format(prefix))
    else:
      btn_send_sms = wait_el_xpath(self.driver, path(app, 'btn_send_sms_path'))
      action(text_editor, Commands.CLICK)
      action(text_editor, Commands.SEND_KEYS, path(app, 'default_msg'))
      action(btn_send_sms, Commands.CLICK)
      logging.info('{0}: Send a SMS to reference phone.'.format(prefix))
      sleep(10)
      # wait_el_xpath_click(self.driver, path(app, 'navigate_up_path'))
      self.driver.back()
      logging.info('{0}: END'.format(prefix))

  def test_MMS_MO(self):
    app = 'messaging'
    prefix = 'test_MMS_MO'
    logging.info('{0}: START'.format(prefix))

    text_editor = self.initM('phone_num')

    if text_editor is None:
      logging.info('{0}: Text editor load unsucceed.'.format(prefix))
      self.fail('{0}: Text editor load unsucceed.'.format(prefix))
    else:
      wait_el_xpath_click(self.driver, path(app, 'add_attach_path'))
      wait_el_xpath_click(self.driver, path(app, 'attach_subject_path'))
      et_subject = wait_el_xpath(self.driver, path(app, 'et_subject_path'))
      action(et_subject, Commands.SEND_KEYS, path(app, 'default_subject'))
      action(text_editor, Commands.CLICK)
      action(text_editor, Commands.SEND_KEYS, path(app, 'default_msg'))
      btn_send_mms = wait_el_xpath(self.driver, path(app, 'btn_send_mms_path'))
      action(btn_send_mms, Commands.CLICK)
      logging.info('{0}: Send a MMS to reference phone.'.format(prefix))
      sleep(10)
      # wait_el_xpath_click(self.driver, path(app, 'navigate_up_path'))
      self.driver.back()
      logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()