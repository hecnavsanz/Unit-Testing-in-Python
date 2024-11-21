from selenium import webdriver


# start the browser session
print("Starting the browser session...")
options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

# navigate to the page
print("Navigating to the page...")
driver.get("http://localhost:10081/web-apps/events/index.html")

# get the title of the page
print("Getting the title of the page...")
title = driver.title
print("Page title =", title)

# close the browser session
print("Closing the browser session...")
driver.quit()
