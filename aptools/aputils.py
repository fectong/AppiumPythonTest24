# -*- coding:utf-8 -*-
'''
  Appium Webdriver utils.
  Easy to use appium webdriver method.
'''

import os
import sys
import time
import unittest
import configparser
import logging

from time import sleep
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from configparser import NoOptionError, NoSectionError
from .apconstants import Commands

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

cfg = configparser.ConfigParser()
cfg.read(PATH('../conf/element.ini'))

if not(os.path.isdir(PATH('../logs'))):
  os.mkdir(PATH('../logs'))
  if not(os.access(PATH('../logs'), os.W_OK)):
    logging.info('Path {0} cannot be written.'.format(PATH('../logs')))

timestr = time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))
logging.basicConfig(
  level=logging.INFO,
  format="[%(asctime)s] %(levelname)s- %(message)s",
  filename=PATH("../logs/"+timestr+".log"),
  filemode = 'a'
)

def keycode(key):
  return{
    Commands.ENTER: 66,
    Commands.HOME: 3,
    Commands.BACK: 4,
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

def path(section, option):
  try:
    path = cfg.get(section, option)
    return path
  except KeyError:
    logging.debug("KeyError, config file does not have key named {0}.".format(option))
    return None
  except NoSectionError:
    logging.debug("NoSectionError, config file does not have section named {0}.".format(section))
    return None
  except NoOptionError:
    logging.debug("NoOptionError, config file does not have option named {0}.".format(option))
    return None

def value(element, value):
  try:
    return{
      Commands.TEXT: element.text,
      Commands.TAG_NAME: element.tag_name
    }.get(value, "Please confirm if the element has this {0}.".format(value))
  except AttributeError as ae:
    print('AttributeError: {0}'.format(ae))
  except KeyError as ke:
    print('KeyError: {0}'.format(ke))

def action(element, action, keys = None):
  try:
    return{
      Commands.CLICK: element.click(),
      Commands.CLEAR: element.clear(),
      Commands.SEND_KEYS: element.send_keys(keys)
    }.get(action, "Please confirm if the element has this {0}.".format(action))
  except AttributeError as ae:
    print('AttributeError: {0}'.format(ae))
  except KeyError as ke:
    print('KeyError: {0}'.format(ke))


"""
WebDriverWait
"""
def wait_el_xpath(driver, element, timeout=8):
  try:
    return WebDriverWait(driver, timeout).until(lambda x: x.find_element_by_xpath(element))
  except TimeoutException:
    logging.debug("TIMEOUT, Please confirm if the xPath({0}) is exist.".format(element))
    return None
  except WebDriverException:
    logging.debug("WebDriverException, Please confirm if the xPath({0}) is correct.".format(element))
    return None

def wait_els_xpath(driver, elements, timeout=8):
  try:
    return WebDriverWait(driver, timeout).until(lambda x: x.find_elements_by_xpath(elements))
  except TimeoutException:
    logging.debug("TIMEOUT, Please confirm if the xPath({0}) is exist.".format(elements))
    return None
  except WebDriverException:
    logging.debug("WebDriverException, Please confirm if the xPath({0}) is correct.".format(elements))
    return None

def wait_el_xpath_click(driver, element, timeout=8):
  try:
    action(wait_el_xpath(driver, element, timeout), Commands.CLICK)
    return True
  except TimeoutException:
    logging.debug("TIMEOUT, Please confirm if the xPath({0}) is exist.".format(element))
    return False
  except WebDriverException:
    logging.debug("WebDriverException, Please confirm if the xPath({0}) is correct.".format(element))
    return False

def wait_el_id(driver, element, timeout=8):
  try:
    return WebDriverWait(driver, timeout).until(lambda x: x.find_element_by_id(element))
  except TimeoutException:
    logging.debug("TIMEOUT, Please confirm if the id({0}) is exist.".format(element))
    return None
  except WebDriverException:
    logging.debug("WebDriverException, Please confirm if the xPath({0}) is correct.".format(element))
    return None

def wait_els_id(driver, elements, timeout=8):
  try:
    return WebDriverWait(driver, timeout).until(lambda x: x.find_elements_by_id(elements))
  except TimeoutException:
    logging.debug("TIMEOUT, Please confirm if the id({0}) is exist.".format(elements))
    return None
  except WebDriverException:
    logging.debug("WebDriverException, Please confirm if the xPath({0}) is correct.".format(elements))
    return None

def wait_el_id_click(driver, element, timeout=8):
  try:
    action(wait_el_id(driver, element, timeout), Commands.CLICK)
    return True
  except TimeoutException:
    logging.debug("TIMEOUT, Please confirm if the id({0}) is exist.".format(element))
    return False
  except WebDriverException:
    logging.debug("WebDriverException, Please confirm if the xPath({0}) is correct.".format(element))
    return False

def wait_time(func):
  def inner(*args):
    time.sleep(0.5)
    f = func(*args)
    time.sleep(0.5)
    return f
  return inner

@wait_time
def screenshot(driver):
  filename = ''.join(PATH("../logs/"+str(time.time())+".png"))
  return driver.get_screenshot_as_file(filename)

# Swipe: Left Right Up Down
class MobileSwipe():
  def __init__(self):
    pass

  def swipe_up(self, driver, time=500):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height*2/3, width/2, height*1/3, time)

  def swipe_down(self, driver, time=500):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height*1/3, width/2, height*2/3, time)

  def swipe_left(self, driver, time=500):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width*3/4, height/2, width*1/4, height/2, time)

  def swipe_right(self, driver, time=500):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width*1/4, height/2, width*3/4, height/2, time)


if __name__ == "__main__":
  MobileSwipe()