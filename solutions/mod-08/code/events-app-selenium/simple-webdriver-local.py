import time

from selenium import webdriver


# start the browser session
print("Starting the browser session...")
driver = webdriver.Chrome()

time.sleep(5)

# navigate to the page
print("Navigating to the page...")
driver.get("http://localhost:10081/selenium/events/index.html")

# get the title of the page
print("Getting the title of the page...")
title = driver.title
print("Page title =", title)

time.sleep(5)

# close the browser session
print("Closing the browser session...")
driver.quit()

# dont use driver.close() bcz it will close the browser window that the driver has focus of
# but will not close the browser session
