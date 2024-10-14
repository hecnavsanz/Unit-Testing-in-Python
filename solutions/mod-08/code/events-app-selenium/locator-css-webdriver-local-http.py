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

# get the Selenium elements by css locator
print("Getting the Selenium elements by CSS LOCATOR ...")
elements = driver.find_elements(by=By.CSS_SELECTOR, value=".container")
for element in elements:
    print("Element")
    print("Element text =", element.get_attribute("textContent"))
    print("Element tag name =", element.tag_name)
    print("Element location =", element.location)
    print("Element size =", element.size)
    print("Element is displayed =", element.is_displayed())
    print("Element is enabled =", element.is_enabled())
    print("Element is selected =", element.is_selected())
# the text of the element is displayed as it's coded in the HTML file (see the Menu element)

# close the browser session
print("Closing the browser session ...")
driver.quit()
