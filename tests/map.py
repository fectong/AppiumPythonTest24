# -*- coding:utf-8 -*-
"""
03. Launch Maps: Launch Google maps, apply several map overlays, then quit.
"""
import os
import unittest

from appium import webdriver
from conf import appium_config
from conf.appium_config import cfg, logging
from common.utils import wait_el_xpath, wait_el_xpath_click

class GoogleMaps(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver('GoogleMaps')

  def test_multi_layers(self):
    logging.info('test_multi_layers: START')
    wait_el_xpath_click(self.driver, cfg.get('map', 'page_skip_path'))
    wait_el_xpath_click(self.driver, cfg.get('map', 'btn_compass_path'))
    logging.info(self.driver.current_activity)

    type_default = wait_el_xpath(self.driver, cfg.get('map', 'map_type_default_path'))
    type_satellite = wait_el_xpath(self.driver, cfg.get('map', 'map_type_satellite_path'))
    type_terrain = wait_el_xpath(self.driver, cfg.get('map', 'map_type_terrain_path'))
    type_transit = wait_el_xpath(self.driver, cfg.get('map', 'map_type_transit_path'))
    type_traffic = wait_el_xpath(self.driver, cfg.get('map', 'map_type_traffic_path'))
    type_bicycling = wait_el_xpath(self.driver, cfg.get('map', 'map_type_bicycling_path'))

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
      for d in details_list:
        d.click()

    wait_el_xpath_click(self.driver, cfg.get('map', 'btn_close_compass_path'))
    logging.info('test_multi_layers: END')

  @classmethod
  def tearDownClass(self):
    self.driver.quit()
