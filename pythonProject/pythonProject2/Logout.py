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

class Logout(Loginscreenview):
    Logout = (MobileBy.XPATH, '//android.widget.TextView[@text="Logout"]')
    LoginText = (MobileBy.XPATH, '//android.widget.TextView[@text="Login"]')


    def assertlogout(self,wait):
        wait.until(EC.presence_of_element_located(self.Logout)).click()
        logintext = wait.until(EC.presence_of_element_located(self.LoginText))
        assert logintext.text == 'Login'



