import time

from selenium import webdriver


# options for the browser
options = webdriver.ChromeOptions()
# available browser versions: stable, beta, dev (must be installed the related browser executable)
options.browser_version = '130.0.6723.119'
# available page load strategies: normal, eager, none
options.page_load_strategy = 'none'
# platform name: linux, mac, windows, any
options.platform_name = 'windows'

# browserName set by default when new Options class instance is created
print("Using browser:", options.to_capabilities()['browserName'])

# start the browser session
print("Starting the browser session ...")
driver = webdriver.Chrome(options=options)

# navigate to the page (HTTP)
print("HTTP - Navigating to the page...")
driver.get("http://localhost:10081/web-apps/events/index.html")

# get the title of the page
print("Getting the title of the page...")
title = driver.title
print("Page title =", title)

time.sleep(10)

# close the browser session
print("Closing the browser session ...")
driver.quit()
