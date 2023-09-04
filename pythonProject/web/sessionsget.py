import time

from selenium import webdriver

cef="Chrome()"
driver=webdriver.cef

try:
    driver.get("https://google.com")
    time.sleep(2)
finally:
    driver.quit()