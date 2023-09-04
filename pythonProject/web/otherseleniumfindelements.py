import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()

try:
    driver.get("https://www.actitime.com/")
    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    '''wait.until(EC.visibility_of_element_located(By.LINK_TEXT,"Try Free"))'''
    ele=driver.find_elements(By.LINK_TEXT,"Try Free")
    ele[1].click()
    time.sleep(5)
    wait.until(EC.url_to_be("https://www.actitime.com/free-online-trial"))
    driver.find_element(By.ID,"FirstName").send_keys("first name")
    driver.find_element(By.ID, "LastName").send_keys("Last name")
    driver.find_element(By.ID, "Email").send_keys("email@gmail.com")
    driver.find_element(By.ID, "Company").send_keys("company name")
    time.sleep(5)


finally:
    driver.quit()