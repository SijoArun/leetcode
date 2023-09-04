from appium.webdriver.common.mobileby import MobileBy
from viewpage.base_view import baseView
from selenium.common.exceptions import TimeoutException

class echoviewscreen(baseView):
    Message_input = (MobileBy.ACCESSIBILITY_ID, 'messageInput')
    Message_save = (MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn')


    def sendmessage(self,message):

        self.wait_for(self.Message_input).send_keys(message)
        self.wait_for(self.Message_save).click()

    def getsavemessage(self):
        try:
            return self.wait_for(self.Saved_message).text
        except TimeoutException:
            return None

    def nav_back(self):
        self.driver.back()
        from viewpage.homeview import homeviewscreen
        return homeviewscreen.instance(self.driver)


class echoviewscreenIos(echoviewscreen):
    Saved_message = (MobileBy.ACCESSIBILITY_ID, 'savedMessage')

class echoviewscreenAndroid(echoviewscreen):
    Saved_message = (MobileBy.XPATH, '//android.widget.TextView[@content-desc != ""]')

echoviewscreen._IOS=echoviewscreenIos
echoviewscreen._ANDROID=echoviewscreenAndroid