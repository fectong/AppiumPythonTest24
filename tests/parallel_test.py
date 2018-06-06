# -*- coding:utf-8 -*-

import os
import sys
import unittest

from time import sleep

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, C_Settings, C_Memorry
from aptools.aputils import action, value, logging, wait_el_xpath, wait_el_xpath_click


class ParallelTest(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.Odriver = appium_config.my_webdriver(C_Settings.APP, port=4723, device_index=0)
    self.Tdriver = appium_config.my_webdriver(C_Settings.APP, port=4725, device_index=1)

  def test_parallel(self):
    prefix = C_Memorry.PREFIX
    logging.info('{0}: START'.format(prefix))
    sleep(5)
    if wait_el_xpath_click(self.Odriver, C_Settings.PATH_MEMORY):
      sleep(5)
      if wait_el_xpath(self.Odriver, C_Memorry.PATH_DONUT) is not None:
        logging.info('{0}: There is no sd card.'.format(prefix))
        tv_total_memory = wait_el_xpath(self.Odriver, C_Memorry.PATH_TOTAL_MEMORY)
        tv_used = wait_el_xpath(self.Odriver, C_Memorry.PATH_USED)
        logging.info('{0}: {1} {2}'.format(prefix, value(tv_used, Commands.TEXT), value(tv_total_memory, Commands.TEXT)))
      else:
        logging.info('{0}: There is a sd card.')
        tv_used_c = wait_el_xpath(self.Odriver, C_Memorry.PATH_USED_C)
        tv_total_c = wait_el_xpath(self.Odriver, C_Memorry.PATH_TOTAL_C)
        logging.info('{0}: {1} {2}'.format(prefix, value(tv_used_c, Commands.TEXT), value(tv_total_c, Commands.TEXT)))
      sleep(2)
    else:
      self.fail('{0}: Memory load unsucceed.'.format(prefix))
    sleep(3)

    if wait_el_xpath_click(self.Tdriver, C_Settings.PATH_MEMORY):
      sleep(5)
      if wait_el_xpath(self.Tdriver, C_Memorry.PATH_DONUT) is not None:
        logging.info('{0}: There is no sd card.'.format(prefix))
        tv_total_memory = wait_el_xpath(self.Tdriver, C_Memorry.PATH_TOTAL_MEMORY)
        tv_used = wait_el_xpath(self.Tdriver, C_Memorry.PATH_USED)
        logging.info('{0}: {1} {2}'.format(prefix, value(tv_used, Commands.TEXT), value(tv_total_memory, Commands.TEXT)))
      else:
        logging.info('{0}: There is a sd card.')
        tv_used_c = wait_el_xpath(self.Tdriver, C_Memorry.PATH_USED_C)
        tv_total_c = wait_el_xpath(self.Tdriver, C_Memorry.PATH_TOTAL_C)
        logging.info('{0}: {1} {2}'.format(prefix, value(tv_used_c, Commands.TEXT), value(tv_total_c, Commands.TEXT)))
      sleep(2)
    else:
      self.fail('{0}: Memory load unsucceed.'.format(prefix))
    sleep(3)

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.Odriver.quit()
    self.Tdriver.quit()