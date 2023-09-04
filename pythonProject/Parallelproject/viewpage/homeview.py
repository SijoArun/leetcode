from appium.webdriver.common.mobileby import MobileBy
from viewpage.base_view import baseView
from viewpage.echoview import echoviewscreen

class homeviewscreen(baseView):


    ECHO_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Echo Box')


    def nav_to_echobox(self):

        self.wait_for(self.ECHO_ITEM).click()
        return echoviewscreen.instance(self.driver)



