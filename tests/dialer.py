# -*- coding:utf-8 -*-
"""
06. MO ViLTE: Establish an outgoing IR94 Video over LTE call and stay connected to the reference device for three minutes.
07. Make MO Call: Establish an outgoing VoLTE call and stay connected to the reference device for three minutes.
11. Receive MT Call: Receive an incoming VoLTE call from the reference device and stay for three minutes.
19. VoLTE to ViLTE to VoLTE: Establish an outgoing VoLTE call to the reference device, upgrade to IR94 after 15 seconds, stay connected on the video call for three minutes, downgrade to VoLTE, then end the call after 15 seconds of audio calling.
"""

import os
import sys
import unittest
import time

from appium.webdriver.common.touch_action import TouchAction

sys.path.append("..")
from server import appium_server
from tools.mobile import get_devices
from tools.constants import Commands, C_Dialer
from tools.utils import action, logging, wait_el_id, wait_el_id_click

class Dialer(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    devices = get_devices()
    self.flag = False
    if len(devices) >= 2:
      self.flag = True
      self.Odriver = appium_server.my_webdriver(C_Dialer.APP, port=4723, system_port=8200, device_name=devices[0], newCommandTimeout=180)
      self.Tdriver = appium_server.my_webdriver(C_Dialer.APP, port=4725, system_port=8201, device_name=devices[1], newCommandTimeout=180)

  @classmethod
  def setUp(self):
    if not self.flag:
       logging.info('test_dialer: There is only one device, can not take a interacted call test.')
       self.fail('test_dialer: There is only one device, can not take a interacted call test.')

    if self.Odriver == None or self.Tdriver == None:
      self.fail('Camera: Get webdriver unsucceed.')

    self.Odriver.launch_app()
    self.Tdriver.launch_app()

  def test_MOViLTE(self):
    pass

  def test_MOVoLTE(self):
    prefix = C_Dialer.PREFIX
    logging.info('{0}_MOVoLTE: START'.format(prefix))
    wait_el_id_click(self.Odriver, C_Dialer.ID_BTN_FLOAT)
    
    for n in C_Dialer.REF_PHONE_NUM:
      wait_el_id_click(self.Odriver, C_Dialer.number(self, n))
    time.sleep(10)

    btn_call = wait_el_id(self.Odriver, C_Dialer.ID_BTN_DIALPAD_FLOAT, 10)
    if btn_call is None:
      self.fail('{0}: Wait to long for the call.'.format(prefix))
    action(btn_call, Commands.CLICK)

    btn_swipe_to_answer = wait_el_id(self.Tdriver, C_Dialer.ID_SWIPE_TO_ANSWER, 10)
    width = self.Tdriver.get_window_size()['width']
    height = self.Tdriver.get_window_size()['height']
    TouchAction(self.Tdriver).press(btn_swipe_to_answer).move_to(x=width/2, y=height/3)

    call_time = C_Dialer.CALL_TIME
    timeout = time.time() + 60*call_time
    logging.info('{0}: Play for {1} miuntes'.format(prefix, call_time))
    while time.time() < timeout:
      if (int(timeout-time.time()))%20 == 0:
        self.Odriver.get_window_size()
        self.Tdriver.get_window_size()
        logging.info('{0}: In Call'.format(prefix))
        time.sleep(5)

    wait_el_id_click(self.Odriver, C_Dialer.ID_BTN_END_CALL)

    logging.info('{0}_MOVoLTE: END'.format(prefix))

  def test_MTVoLTE(self):
    pass

  def test_Vo2Vi2Vo(self):
    pass

  @classmethod
  def tearDown(self):
    self.Odriver.close_app()
    self.Tdriver.close_app()

  @classmethod
  def tearDownClass(self):
    self.Odriver.quit()
    self.Tdriver.quit()