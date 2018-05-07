# -*- coding:utf-8 -*-
'''
  Appium Webdriver utils.
  Easy to use appium webdriver method.
'''

import os
import sys
import time
import unittest
from time import sleep
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from conf.appium_config import logging

def wait_time(func):
  def inner(*args):
    time.sleep(0.5)
    f = func(*args)
    time.sleep(0.5)
    return f
  return inner

def get_keycode(key):
  return{
    'ENTER': 66,
    'HOME': 3,
    'BACK': 4,
    0: 7,
    1: 8,
    2: 9,
    3: 10,
    4: 11,
    5: 12,
    6: 13,
    7: 14,
    8: 15,
    9: 16
  }.get(key, "Please confirm if the keycode is valid.")

def wait_el_xpath(driver, element):
  return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(element))

def wait_el_xpath_click(driver, element):
  return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(element)).click()

def wait_el_id(driver, element):
  return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(element))

def wait_el_id_click(driver, element):
  return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(element)).click()

@wait_time
def screenshot(driver):
  filename = ''.join("../logs/" + str(time.time()) + ".png")
  return driver.get_screenshot_as_file(filename)

# Swipe: Left Right Up Down
class MobileSwipe():
  def __init__(self):
    pass

  def swipe_up(self, driver, time):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height/4, width/2, height/4*3, time)

  def swipe_down(self, driver, time):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height/4*3, width/2, height/4, time)

  def swipe_down_half(self, driver, time):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height/4*3, width/2, height/4*2, time)

  def swipe_left(self, driver, time):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/4*3, height/2, width/4, height/2, time)

  def swipe_right(self, driver, time):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/4, height/2, width/4*3, height/2, time)

if __name__ == "__main__":
  MobileSwipe()
