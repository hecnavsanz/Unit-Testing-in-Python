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

# get the Selenium GitHub element by ID
print("Getting the Selenium GitHub element by ID ...")
element = driver.find_element(by=By.ID, value="selenium-github")
print("Element text =", element.text)
print("Element tag name =", element.tag_name)
print("Element location =", element.location)
print("Element size =", element.size)
print("Element is displayed =", element.is_displayed())
print("Element is enabled =", element.is_enabled())
print("Element is selected =", element.is_selected())

# close the browser session
print("Closing the browser session ...")
driver.quit()
