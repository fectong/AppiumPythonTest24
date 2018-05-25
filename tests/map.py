# -*- coding:utf-8 -*-
"""
03. Launch Maps: Launch Google maps, apply several map overlays, then quit.
"""
import os
import sys
import unittest

from time import sleep

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, Apps
from aptools.aputils import path, action, value, logging, wait_el_xpath, wait_el_xpath_click, wait_els_xpath


class GoogleMaps(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(app_name=Apps.GOOGLE_MAPS, no_reset=True)

  def test_multi_layers_no_reset(self):
    app = 'map'
    prefix = 'test_multi_layers_no_reset'
    logging.info('{0}: START'.format(prefix))
    sleep(3)
    if wait_el_xpath_click(self.driver, path(app, 'page_skip_path'), 3):
      logging.info('{0}:Launch Google Maps 1st time.'.format(prefix))
    else:
      logging.info('{0}: No need to initialize Google Maps.'.format(prefix))

    sleep(8)
    if wait_el_xpath_click(self.driver, path(app, 'btn_compass_path')):

      map_list = [
        wait_el_xpath(self.driver, path(app, 'map_type_default_path')),     # type_default
        wait_el_xpath(self.driver, path(app, 'map_type_satellite_path')),   # type_satellite
        wait_el_xpath(self.driver, path(app, 'map_type_terrain_path'))      # type_terrain
      ]
      details_list = [
        wait_el_xpath(self.driver, path(app, 'map_type_transit_path')),     # type_transit
        wait_el_xpath(self.driver, path(app, 'map_type_traffic_path')),     # type_traffic
        wait_el_xpath(self.driver, path(app, 'map_type_bicycling_path'))    # type_bicycling
      ]

      for m in map_list:
        action(m, Commands.CLICK)
        sleep(2)
        for d in details_list:
          action(d, Commands.CLICK)
          logging.info('{0}: {1} - {2}'.format(prefix, value(m, Commands.TEXT), value(d, Commands.TEXT)))
          sleep(2)
      wait_el_xpath_click(self.driver, path(app, 'btn_close_compass_path'))
    else:
      nav_menu = wait_el_xpath(self.driver, path(app, 'nav_menu_path'))
      if not nav_menu:
        logging.info('{0}: Navgiate menu load unsucceed.'.format(prefix))
        self.fail('{0}: Navgiate menu load unsucceed.'.format(prefix))
      else:
        action(nav_menu, Commands.CLICK)
        traffic_types = wait_els_xpath(self.driver, path(app, 'nav_types_path'))

        for type in traffic_types:
          logging.info('{0}: {1}'.format(prefix, value(type, Commands.TEXT)))
          action(type, Commands.CLICK)
          sleep(6)
          action(nav_menu, Commands.CLICK)

        action(traffic_types[0], Commands.CLICK)
        
        sleep(5)

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()
