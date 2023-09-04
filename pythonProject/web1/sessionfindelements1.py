import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Form Authentication")
    els=driver.find_elements(By.CSS_SELECTOR,"a")
    print(f"Element list are {len.els}")

    els1 = driver.find_elements(By.CSS_SELECTOR, "foo")
    print(f"Element list are {len.els1}")


finally:
    driver.quit()