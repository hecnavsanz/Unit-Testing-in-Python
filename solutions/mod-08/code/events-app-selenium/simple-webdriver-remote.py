import time

from selenium import webdriver


# start the browser session
print("Starting the browser session...")
options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor="http://10.20.0.100:4444/wd/hub", options=options)

time.sleep(30)

# navigate to the page
print("Navigating to the page...")
driver.get("http://10.20.0.201/web-apps/events/index.html")

# get the title of the page
print("Getting the title of the page...")
title = driver.title
print("Page title =", title)

time.sleep(10)

# close the browser session
print("Closing the browser session...")
driver.quit()
