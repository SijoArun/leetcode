import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

elementCount = int(0)

url = "https://the-internet.herokuapp.com/"
# Elements definition
add_Remove = (By.LINK_TEXT, "Add/Remove Elements")
delete_Elements = (By.XPATH, "//button[@onclick='deleteElement()']")
addElement = (By.XPATH, "//button[@onclick='addElement()']")
dynamic_Loading = (By.LINK_TEXT, "Dynamic Loading")
example2 = (By.LINK_TEXT, "Example 2: Element rendered after the fact")
ID = (By.XPATH, "//button[contains(text(),'Start')]")
Hello = (By.XPATH, "//h4[contains(text(),'Hello World!')]")
frame = (By.LINK_TEXT, "Frames")
iframe = (By.LINK_TEXT, "iFrame")
iframe_id = 'mce_0_ifr'
content = (By.XPATH, "//body[@id='tinymce']")
helloText = 'Hello World!'
Texttobesent = "Hello from automation!"


# Element addition method
def elementaddition(elementadd, elementdelete, counte):
    elementadd1 = wait.until(ec.presence_of_element_located(elementadd))
    elementadd1.click()
    elements = wait.until(ec.presence_of_all_elements_located(elementdelete))
    counte += 1
    assert len(elements) == counte
    print("Element count is : ", counte)
    return counte


# Element Deletion method
def elementdeletion(eldelets, countele):
    elementdel = wait.until(ec.presence_of_element_located(eldelets))
    elementdel.click()
    try:
        elements = wait.until(ec.presence_of_all_elements_located(eldelets))
        countele -= 1
        assert len(elements) == countele
        print("Element count is : ", countele)
    except TimeoutException:
        assert countele == 0
        print("Element count is : ", countele)
    return countele


# Main method with try
try:
    # driver = webdriver.Remote(command_executor="http://localhost:9515",
    #                       desired_capabilities=caps)

    driver.get(url)
    wait = WebDriverWait(driver, 10)
    elementAdd = wait.until(ec.presence_of_element_located(add_Remove))
    elementAdd.click()
    try:
        wait.until(ec.presence_of_all_elements_located(delete_Elements))
    except TimeoutException:
        assert elementCount == 0
        print("Element count is : ", elementCount)

    elementCount = elementaddition(addElement, delete_Elements, elementCount)
    elementCount = elementaddition(addElement, delete_Elements, elementCount)
    elementCount = elementdeletion(delete_Elements, elementCount)
    elementdeletion(delete_Elements, 0)

    driver.back()

    dynamicLoading = wait.until(ec.presence_of_element_located(dynamic_Loading))
    dynamicLoading.click()

    Example2 = wait.until(ec.presence_of_element_located(example2))
    Example2.click()

    start = wait.until(ec.presence_of_element_located(ID))
    start.click()

    textValidation = wait.until(ec.presence_of_element_located(Hello)).text
    print(textValidation)
    assert textValidation == helloText

    driver.back()
    driver.back()

    frames = wait.until(ec.presence_of_element_located(frame))
    frames.click()

    iframes = wait.until(ec.presence_of_element_located(iframe))
    iframes.click()

    driver.switch_to.frame(iframe_id)

    contentelement = wait.until(ec.presence_of_element_located(content))
    print(contentelement.text)
    contentelement.clear()
    contentelement.send_keys(Texttobesent)
    print(contentelement.text)
    assert Texttobesent == contentelement.text
    driver.switch_to.default_content()
    driver.back()
    driver.back()
    time.sleep(5)

except ValueError as e:
    print(f"Caught ValueError: {e}")
except KeyError as e:
    print(f"Caught KeyError: {e}")
except Exception as e:
    print(f"Caught exception: {e}")

finally:
    driver.quit()
