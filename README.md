# 自动化测试 Appium-Python-Client

## 1 配置 JAVA JDK 环境变量

---

``` CMD

  改为自己电脑 JDK 的安装位置

  JAVA_HOME:
    C:\Program Files\Java\jdk1.8.0_144

  JRE_HOME:
    %JAVA_HOME%\jre

  CLASSPATH:
    .;%JAVA_HOME%\lib;%JRE_HOME%\lib
  PATH:
    %JAVA_HOME%
    %JAVA_HOME%\bin
```

### 检查 JAVA JDK

``` CMD
java -version
```

## 2 配置 Android SDK 环境变量

---

``` CMD
ANDROID_HOME:
  改为自己电脑 SDK 的安装位置
  D:\Android\sdk
ANDROID_SWT:
  %ANDROID_HOME%\tools\lib\x86
PATH:
  %ANDROID_HOME%\tools
  %ANDROID_HOME%\platform-tools
```

### 检查 Android SDK

``` CMD
adb version
```

## 3 安装 Python 3.X.X

---

安装时会提示是否添加到系统变量,手动添加则按照以下设置

``` CMD
PATH:
  改为自己电脑 Python 的安装位置
  C:\Users\xxx\AppData\Local\Programs\Python\Python36-32
```

### 检查 Python

``` CMD
python --version
```

## 4 安装 Appium

---

选择一种安装方式:

### 1. [官网](https://appium.io/downloads.html)下载 [Appium](https://github.com/appium/appium-desktop/releases) 桌面端安装

### 2. 通过 NodeJS 安装

``` CMD
  npm install -g appium
  npm install -g appium-doctor
```

## 5 安装 Python 必要包和框架

---

### 1. 安装更新pip

``` CMD
  python -m pip install -U pip
```

### 2. 使用pip

``` CMD
  提示出错,尝试重新安装或更新 pip
  python -m pip install --upgrade pip --force-reinstall
```

### 3. 安装所需框架

``` CMD
  pip install requests
  pip install selenium
  pip install Appium-Python-Client

  # 使用 RobotFramework 就装
  pip install robotframework
  pip install robotframework-appiumlibrary
```

### 最终检查

``` CMD
# 此条必须使用 nodejs 安装 appium-doctor 才能使用
appium-doctor
```

## 6 示例代码

---

### 1. bluetooth.py

> 打开 设置 - 蓝牙 - 点击Switch按钮

``` python
# -*- coding: utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class AppTest(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    desired_caps = {
      'platformName': 'Android',              # 测试平台
      'platformVersion': '8.1.0',             # 测试手机的 Android 版本
      'deviceName': '9190aeba',               # 连接设备到电脑使用 adb devices 时所显示的字符串
      'appPackage': 'com.android.settings',   # 所要测试的应用的包名
      'appActivity': '.Settings',             # 测试应用的启动 Activity
      'automationName': 'UiAutomator2'        # 默认不配置, 此条会使用 UiAutomator 而不是 UiAutomator2 会导致在高版本 Android 中无法处理点击事件
    }
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 127.0.0.1:4723 与 Appium Server 端设置一致

  def test_bluetooth(self):
    key_bluetooth = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath("//*[contains(@text, 'Bluetooth')]"))
    key_bluetooth.click()
    key_switch = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath("//*[contains(@resource-id, 'id/switch_widget')]"))
    key_switch.click()

  @classmethod
  def tearDownClass(self):
    self.driver.quit()

if __name__ == "__main__":
  unittest.main()
```

### 2. bluetooth.robot

> 打开 设置 - 蓝牙 - 开启蓝牙 - 菜单 - 刷新

``` robotframework
*** Settings ***
Suite Setup       Open Settings App
Suite Teardown    Close Application
Library           AppiumLibrary

*** Test Cases ***
Test Case 1: Turn On Bluetooth
    [Tags]    Bluetooth Test
    Turn On Bluetooth

Test Case 2: Refresh Bluetooth
    [Tags]    Bluetooth Test
    Refresh Bluetooth Device List

*** Keywords ***
Open Settings App
    Open Application    http://127.0.0.1:4723/wd/hub    platformName=Android    platformVersion=7.1.2    deviceName=85a2a821 appPackage=com.android.settings    appActivity=.Settings
    Sleep    2s
    Open Bluetooth Setting Page

Open Bluetooth Setting Page
    Log    Click the "Bluetooth" Label
    Wait Until Page Contains Element    xpath=//*[contains(@text, 'Bluetooth')]    10    Can NOT find "Bluetooth" label
    Click Element    xpath=//*[contains(@text, 'Bluetooth')]

Turn On Bluetooth
    Wait Until Page Contains Element    xpath=//*[contains(@resource-id, 'id/switch_widget')]
    Sleep    1s
    ${wifi_status} =    Get Element Attribute    xpath=//*[contains(@resource-id, 'id/switch_widget')]    text
    Run Keyword If    '${wifi_status}' != 'ON'    Click Element    xpath=//*[contains(@resource-id, 'id/switch_widget')]

Refresh Bluetooth Device List
    Click Element    xpath=//*[contains(@content-desc, 'More options')]
    Sleep    2s
    Wait Until Page Contains Element    xpath=//*[contains(@text, 'Refresh')]    20    Can NOT find "Refresh"
    ${count}    Get Matching Xpath Count    xpath=//*[contains(@text, 'Refresh')]
    Run Keyword If    ${count} > 0    Click Element    xpath=//*[contains(@text, 'Refresh')]
```

## 7. 模板介绍

1. 启动时配置的 WebDriver 在 [appium_config.py](./conf/appium_config.py) 之中

2. 各测试按照测试应用进行分类, 处于 ./tests 目录

3. 运行:

   ```CMD
   python ./test24.py
   ```