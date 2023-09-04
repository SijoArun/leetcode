import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()

try:
    wait=WebDriverWait(driver,10)
    driver.get("https://the-internet.herokuapp.com/")
    ele1=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Form Authentication")))
    ele1.click()
    username=wait.until(EC.presence_of_element_located((By.ID,"username")))
    username.send_keys('tomsmith')
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR,"button[class='radius']").click()
    logout=wait.until(EC.presence_of_element_located((By.XPATH,"//i[@class='icon-2x icon-signout']")))
    assert "Logout" in logout.text

finally:
    driver.quit()