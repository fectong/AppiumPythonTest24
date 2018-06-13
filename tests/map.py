# -*- coding:utf-8 -*-
"""
03. Launch Maps: Launch Google maps, apply several map overlays, then quit.
"""
import os
import sys
import unittest

from time import sleep

sys.path.append("..")
from server import appium_server
from tools.constants import Commands, C_Maps
from tools.utils import action, value, logging, wait_el_xpath, wait_el_xpath_click, wait_els_xpath


class GoogleMaps(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.driver = appium_server.my_webdriver(C_Maps.APP, no_reset=True)

  @classmethod
  def setUp(self):
    if self.driver == None:
      self.fail('GoogleMaps: Get webdriver unsucceed.')

  def test_multi_layers_no_reset(self):
    prefix = C_Maps.PREFIX
    logging.info('{0}: START'.format(prefix))
    sleep(3)
    if wait_el_xpath_click(self.driver, C_Maps.PATH_PAGE_SKIP, 3):
      logging.info('{0}:Launch Google Maps 1st time.'.format(prefix))
    else:
      logging.info('{0}: No need to initialize Google Maps.'.format(prefix))

    sleep(8)
    if wait_el_xpath_click(self.driver, C_Maps.PATH_BTN_COMPASS):

      map_list = [
        wait_el_xpath(self.driver, C_Maps.PATH_MAP_TYPE_DEFAULT),     # type_default
        wait_el_xpath(self.driver, C_Maps.PATH_MAP_TYPE_SATELLITE),   # type_satellite
        wait_el_xpath(self.driver, C_Maps.PATH_MAP_TYPE_TERRAIN)      # type_terrain
      ]
      details_list = [
        wait_el_xpath(self.driver, C_Maps.PATH_MAP_TYPE_TRANSIT),     # type_transit
        wait_el_xpath(self.driver, C_Maps.PATH_MAP_TYPE_TRAFFIC),     # type_traffic
        wait_el_xpath(self.driver, C_Maps.PATH_MAP_TYPE_BICYCLING)    # type_bicycling
      ]

      for m in map_list:
        action(m, Commands.CLICK)
        sleep(3)
        for d in details_list:
          action(d, Commands.CLICK)
          logging.info('{0}: {1} - {2}'.format(prefix, value(m, Commands.TEXT), value(d, Commands.TEXT)))
          sleep(3)
      wait_el_xpath_click(self.driver, C_Maps.PATH_BTN_CLOSE_COMPASS)
    else:
      nav_menu = wait_el_xpath(self.driver, C_Maps.PATH_NAV_MENU)
      if not nav_menu:
        logging.info('{0}: Navgiate menu load unsucceed.'.format(prefix))
        self.fail('{0}: Navgiate menu load unsucceed.'.format(prefix))
      else:
        action(nav_menu, Commands.CLICK)
        traffic_types = wait_els_xpath(self.driver, C_Maps.PATH_NAV_TYPES, 10)

        for type in traffic_types:
          logging.info('{0}: {1}'.format(prefix, value(type, Commands.TEXT)))
          action(type, Commands.CLICK)
          sleep(6)
          action(nav_menu, Commands.CLICK)

        action(traffic_types[0], Commands.CLICK)

        sleep(5)

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDown(self):
    self.driver.close_app()

  @classmethod
  def tearDownClass(self):
    self.driver.quit()
