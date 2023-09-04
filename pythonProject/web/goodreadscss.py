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
    print(driver.find_element(By.CSS_SELECTOR,"div.sellingPointBoxRight").text)
    print(driver.find_element(By.CSS_SELECTOR,"div[class*='BoxRight']").text)
    print(driver.find_element(By.CSS_SELECTOR,"div[class^='sellingPointBoxRi']").text)
    print(driver.find_element(By.CSS_SELECTOR,"div[class$='PointBoxRight']").text)

    print(driver.find_element(By.CSS_SELECTOR,"a[class^='gr-hyper'][href='/user/sign_in']").text)
    print(driver.find_element(By.CSS_SELECTOR, "a[class^='gr-hyperlink'],a[href='/user/sign_in']").text)

    time.sleep(5)

except Exception as e:
    print("Exception in automation",e)

finally:
    driver.quit()