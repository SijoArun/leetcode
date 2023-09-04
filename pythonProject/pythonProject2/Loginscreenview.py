import time
from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from main import driver


class Loginscreenview(object):
    Login=(MobileBy.XPATH,'//android.widget.TextView[@text="Login Screen"]')

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver, 5)

    def clicklogin(self,wait):
        wait.until(EC.presence_of_element_located(self.Login)).click()






