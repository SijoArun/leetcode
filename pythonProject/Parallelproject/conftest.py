import time
import pytest as pytest
from appium import webdriver
from os import path
from viewpage.homeview import homeviewscreen
from viewpage.base_view import baseView


CURR_DIR=path.dirname(path.abspath(__file__))
IOS_APP=path.join(CURR_DIR,"..","Mobile","TheApp.app.zip")
ANDROID_APP=path.join(CURR_DIR,"..","Mobile","TheApp.apk")
APPIUMS=['http://localhost:4700','http://localhost:4701']

IOS_CAPS = [{
    'platformName': 'iOS',
    'platformVersion': '16.4',
    'deviceName': 'iPhone 14 Pro Max',
    'automationName': 'XCUITest',
    'app': IOS_APP,
    "appium:wdaLocalPort": 8100,
    "appium:systemPort": 8200
},
{
    'platformName': 'iOS',
    'platformVersion': '16.4',
    'deviceName': 'iPhone 14',
    'automationName': 'XCUITest',
    'app': IOS_APP,
    "appium:wdaLocalPort": 8101,
    "appium:systemPort": 8201
}
]

ANDROID_CAPS = [{
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'app': ANDROID_APP,
},
{
    'platformName': 'Android',
    'deviceName': 'emulator-5556',
    'automationName': 'UiAutomator2',
    'app': ANDROID_APP,
}

]


def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='ios')

@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError('--platform value must be ios or android')
    return plat

@pytest.fixture
def worker_num(worker_id):
    if worker_id == 'master':
        worker_id = 'gw0'
    return int(worker_id[2:])

@pytest.fixture
def server(worker_num):
    if worker_num >= len(APPIUMS):
        raise Exception("Worker id is more than server")
    return APPIUMS[worker_num]

@pytest.fixture
def caps(platform,worker_num):
    cap_set = IOS_CAPS if platform == 'ios' else ANDROID_CAPS
    if worker_num >= len(cap_set):
        raise Exception("Worker id is more than capability")
    return cap_set[worker_num]


@pytest.fixture
def driver(server,caps,platform):


    driver = webdriver.Remote(
    command_executor=server,
    desired_capabilities=caps
    )
    driver._platform = platform
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    return homeviewscreen.instance(driver)