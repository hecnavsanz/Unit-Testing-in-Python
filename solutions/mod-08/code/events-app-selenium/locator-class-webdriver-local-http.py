from selenium import webdriver
from selenium.webdriver.common.by import By

# options for the browser
options = webdriver.ChromeOptions()

# start the browser session
print("Starting the browser session ...")
driver = webdriver.Chrome(options=options)

# navigate to the page (HTTP)
print("HTTP - Navigating to the page...")
driver.get("http://localhost:10081/web-apps/events/index.html")

# get the Selenium elements by class name
print("Getting the Selenium elements by CLASS ...")
elements = driver.find_elements(by=By.CLASS_NAME, value="btn")
for element in elements:
    print("Element")
    print("Element text =", element.get_attribute("textContent"))
    print("Element tag name =", element.tag_name)
    print("Element location =", element.location)
    print("Element size =", element.size)
    print("Element is displayed =", element.is_displayed())
    print("Element is enabled =", element.is_enabled())
    print("Element is selected =", element.is_selected())

# close the browser session
print("Closing the browser session ...")
driver.quit()
