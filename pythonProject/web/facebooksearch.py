import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()

try:
    driver.get("https://www.facebook.com/")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("gm@2gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='pass' and @type='password']").send_keys("Test1234")
    time.sleep(1)

    time.sleep(5)

except Exception as e:
    print("Exception in automation",e)

finally:
    driver.quit()