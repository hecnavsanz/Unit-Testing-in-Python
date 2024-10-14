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

# get the Selenium menu element by class name
print("Getting the Selenium elements by CLASS ...")
menu_element = driver.find_element(by=By.CLASS_NAME, value="dropdown-menu")
# get the Selenium menu elements by tag name
menu_elements = menu_element.find_elements(by=By.TAG_NAME, value="li")
for element in menu_elements:
    print("Element")
    print("Element text =", element.get_attribute("textContent"))
    print("Element tag name =", element.tag_name)
    print("Element location =", element.location)
    print("Element size =", element.size)
    print("Element is displayed =", element.is_displayed())
    print("Element is enabled =", element.is_enabled())
    print("Element is selected =", element.is_selected())
    menu_element_link = element.find_element(by=By.TAG_NAME, value="a")
    # print the href attribute of the link
    print("Element link href =", menu_element_link.get_attribute("href"))

# close the browser session
print("Closing the browser session ...")
driver.quit()
