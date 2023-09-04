import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()

try:
    driver.get("https://www.goodreads.com/")
    time.sleep(2)
    print(driver.find_element(By.XPATH,"//h2[contains(text(),'what to read')]").text)
    print(driver.find_element(By.XPATH,"//h2[starts-with(text(),'Deciding what')]").text)
    print(driver.find_element(By.XPATH, "//h2[starts-with(text(),'Deciding what') and contains(text(),'what to read')]").text)
    print(driver.find_element(By.XPATH,"//*[starts-with(text(),'Deciding what')]").text)
    print(driver.find_element(By.XPATH,"//a[contains(text(),'Sign In') and @class='gr-hyperlink']").text)
    print(driver.find_element(By.XPATH, "//a[contains(text(),'Sign In') or @class='gr-hyperlink']").text)

    time.sleep(5)

except Exception as e:
    print("Exception in automation",e)

finally:
    driver.quit()