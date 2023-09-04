import time
from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from appium import webdriver
from Loginscreenview import Loginscreenview


class ValidLogin(Loginscreenview):
    username = (MobileBy.ACCESSIBILITY_ID, 'username')
    password = (MobileBy.ACCESSIBILITY_ID, 'password')
    loginbutton = (MobileBy.ACCESSIBILITY_ID, 'loginBtn')


    def validlogin(self,wait):
        username = wait.until(EC.presence_of_element_located(self.username))
        username.send_keys('alice')
        password = wait.until(EC.presence_of_element_located(self.password))
        password.send_keys('mypassword')
        loginbutton = wait.until(EC.presence_of_element_located(self.loginbutton))
        loginbutton.click()



