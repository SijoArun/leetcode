import time
from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
CURR_DIR=path.dirname(path.abspath(__file__))
APP=path.join(CURR_DIR,"TheApp.app.zip")
APPIUM='http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '16.4',
    'deviceName': 'iPhone 14 Pro Max',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'List Demo'))).click()
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Altocumulus')))

    scroll=ActionBuilder(driver)
    finger=scroll.add_pointer_input(POINTER_TOUCH,"finger")
    finger.create_pointer_move(duration=0,x=100,y=500)
    finger.create_pointer_down(button=MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=0, y=-500,origin="pointer")
    finger.create_pointer_down(button=MouseButton.LEFT)
    scroll.perform()
    time.sleep(20)
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Stratocumulus')))


finally:
    driver.quit()