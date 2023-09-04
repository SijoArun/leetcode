from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class baseView(object):

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver, 5)

    def wait_for(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

