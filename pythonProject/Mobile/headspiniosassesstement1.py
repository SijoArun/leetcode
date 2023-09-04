import time
from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

#CURR_DIR=path.dirname(path.abspath(__file__))
#APP=path.join(CURR_DIR,"TheApp.app.zip")
APPIUM='https://dev-us-pao-0.headspin.io:7044/v0/1f7e749a3421489fa8e618610b3e2740/wd/hub'

CAPS = {
    "deviceName": "iPhone 12 Mini",
    "udid": "00008101-001C54882ED0001E",
    "automationName": "xcuitest",
    "platformVersion": "14.2",
    "platformName": "ios",
    "headspin:capture": "true",
    "bundleId": "io.cloudgrey.the-app"
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

loginscreen=(MobileBy.ACCESSIBILITY_ID,'Login Screen')
username=(MobileBy.ACCESSIBILITY_ID, 'username')
password=(MobileBy.ACCESSIBILITY_ID, 'password')
loginbutton=(MobileBy.XPATH, '(//XCUIElementTypeOther[@name="loginBtn"])[2]')
message=(MobileBy.ACCESSIBILITY_ID, 'Invalid login credentials, please try again')
button=(MobileBy.ACCESSIBILITY_ID, 'OK')
loginmessagefield=(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="You are logged in as alice"]')
logoutmessage=(MobileBy.XPATH, '(//XCUIElementTypeOther[@name="Logout"])[2]')
assertmessage1="Invalid login credentials, please try again"
assertmessage2="You are logged in as alice"

def loginvalidation(uname,pword,username,password,loginbutton):
    username = wait.until(EC.presence_of_element_located(username))
    count=len(username.text)
    while(count>1):
        username.send_keys('\ue003')
        count=count-1
    username.send_keys(uname)
    password = wait.until(EC.presence_of_element_located(password))
    count1 = len(password.text)
    while (count1 > 1):
        password.send_keys('\ue003')
        count1 = count1-1
    password.send_keys(pword)
    loginbutton1 = wait.until(EC.presence_of_element_located(loginbutton))
    loginbutton1.click()


try:
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located(loginscreen)).click()
    time.sleep(2)
    loginvalidation("aaa", "aaa", username, password, loginbutton)
    wait.until(EC.alert_is_present())
    driver.switch_to.alert
    loginmessage = wait.until(EC.presence_of_element_located(message)).text
    print(loginmessage)
    assert assertmessage1 == loginmessage
    wait.until(EC.presence_of_element_located(button)).click()
    loginvalidation("alice", "mypassword", username, password, loginbutton)
    loginmessage1 = wait.until(EC.presence_of_element_located(loginmessagefield)).text
    print(loginmessage1)
    assert assertmessage2 == loginmessage1
    wait.until(EC.presence_of_element_located(logoutmessage)).click()
    userelement = wait.until(EC.presence_of_element_located(username))
    assert userelement is not None
    time.sleep(10)

except ValueError as e:
    print(f"Caught ValueError: {e}")
except KeyError as e:
    print(f"Caught KeyError: {e}")
except Exception as e:
    print(f"Caught exception: {e}")



finally:
    driver.quit()