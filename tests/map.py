# -*- coding:utf-8 -*-
"""
03. Launch Maps: Launch Google maps, apply several map overlays, then quit.
"""
import os
import unittest
from time import sleep
from appium import webdriver
from conf import appium_config
from common.utils import get_path, logging, wait_el_xpath, wait_el_xpath_click, wait_els_xpath


class GoogleMaps(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(app_name='GoogleMaps', no_reset=True)

  def test_multi_layers_no_reset(self):
    app = 'map'
    prefix = 'test_multi_layers_no_reset'
    logging.info('{0}: START'.format(prefix))
    sleep(3)
    if wait_el_xpath_click(self.driver, get_path(app, 'page_skip_path')):
      logging.info('{0}: Need re-launch to initialize Google Maps.'.format(prefix))
      sleep(8)
      self.driver.close_app()
      self.driver.launch_app()
    else:
      logging.info('{0}: No need to initialize Google Maps.'.format(prefix))

    if wait_el_xpath_click(self.driver, get_path(app, 'btn_compass_path')):
      type_default = wait_el_xpath(self.driver, get_path(app, 'map_type_default_path'))
      type_satellite = wait_el_xpath(self.driver, get_path(app, 'map_type_satellite_path'))
      type_terrain = wait_el_xpath(self.driver, get_path(app, 'map_type_terrain_path'))
      type_transit = wait_el_xpath(self.driver, get_path(app, 'map_type_transit_path'))
      type_traffic = wait_el_xpath(self.driver, get_path(app, 'map_type_traffic_path'))
      type_bicycling = wait_el_xpath(self.driver, get_path(app, 'map_type_bicycling_path'))

      map_list = [
        type_default,
        type_satellite,
        type_terrain
      ]
      details_list = [
        type_transit,
        type_traffic,
        type_bicycling
      ]

      for m in map_list:
        m.click()
        sleep(2)
        for d in details_list:
          d.click()
          logging.info('{0}: {1} - {2}'.format(prefix, m.text, d.text))
          sleep(2)
      wait_el_xpath_click(self.driver, get_path(app, 'btn_close_compass_path'))
    else:
      nav_menu = wait_el_xpath(self.driver, get_path(app, 'nav_menu_path'))
      nav_menu.click()
      traffic_types = wait_els_xpath(self.driver, get_path(app, 'nav_types_path'))

      for type in traffic_types:
        logging.info('{0}: {1}'.format(prefix, type.text))
        type.click()
        sleep(6)
        nav_menu.click()
      
      traffic_types[0].click()
      sleep(5)

    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()
