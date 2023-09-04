import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()

try:
    #driver = webdriver.Remote(command_executor="http://localhost:9515",options=options,
    #                          desired_capabilities=capabilities)



    driver.get("https://the-internet.herokuapp.com/")
    wait = WebDriverWait(driver, 10)
    time.sleep(3)
    elementAdd=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Add/Remove Elements")))
    elementAdd.click()
    elementAdd1 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@onclick='addElement()']")))
    print(elementAdd1)
    elementAdd1.click()
    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@onclick='deleteElement()']")))
    print(len(elements))
    elementAdd1 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@onclick='addElement()']")))
    print(elementAdd1)
    elementAdd1.click()
    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@onclick='deleteElement()']")))
    print(len(elements))
    time.sleep(30)

finally:
    driver.quit()