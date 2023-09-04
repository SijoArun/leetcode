import time

from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

CURR_DIR=path.dirname(path.abspath(__file__))
APP=path.join(CURR_DIR,"TheApp.apk")
APPIUM='https://dev-us-pao-5.headspin.io:7021/v0/1f7e749a3421489fa8e618610b3e2740/wd/hub'

CAPS = {
    "automationName": "uiautomator2",
    "platformName": "android",
    "deviceName": "Pixel 4",
    'app': APP,
    "appPackage": "com.appiumpro.the_app",
    "appActivity": "com.appiumpro.the_app.MainActivity",
    "udid": "98161FFAZ0013A",
    'headspin:capture': True,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

loginscreen=(MobileBy.XPATH,'//android.widget.TextView[@text="Login Screen"]')
username=(MobileBy.ACCESSIBILITY_ID, 'username')
password=(MobileBy.ACCESSIBILITY_ID, 'password')
loginbutton=(MobileBy.ACCESSIBILITY_ID, 'loginBtn')
androidmessage=(MobileBy.XPATH,'//android.widget.TextView[@resource-id="android:id/message"]')
androidbutton=(MobileBy.XPATH,'//android.widget.Button[@resource-id="android:id/button1"]')
loginmessagefield=(MobileBy.XPATH, '//android.widget.TextView[@text="You are logged in as alice"]')
logoutmessage=(MobileBy.XPATH, '//android.widget.TextView[@text="Logout"]')
assertmessage1="Invalid login credentials, please try again"
assertmessage2="You are logged in as alice"


def loginvalidation(uname,pword,username,password,loginbutton):
    username = wait.until(EC.presence_of_element_located(username))
    username.send_keys(uname)
    password = wait.until(EC.presence_of_element_located(password))
    password.send_keys(pword)
    loginbutton = wait.until(EC.presence_of_element_located(loginbutton))
    loginbutton.click()

try:
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located(loginscreen)).click()
    loginvalidation("aaa","aaa",username,password,loginbutton)
    wait.until(EC.alert_is_present())
    driver.switch_to.alert
    loginmessage=wait.until(EC.presence_of_element_located(androidmessage)).text
    print(loginmessage)
    assert assertmessage1 == loginmessage
    wait.until(EC.presence_of_element_located(androidbutton)).click()
    loginvalidation("alice", "mypassword", username, password, loginbutton)
    loginmessage1 = wait.until(EC.presence_of_element_located(loginmessagefield)).text
    print(loginmessage1)
    assert assertmessage2 == loginmessage1
    wait.until(EC.presence_of_element_located(logoutmessage)).click()
    userelement=wait.until(EC.presence_of_element_located(username))
    assert userelement is not None



finally:
    driver.quit()