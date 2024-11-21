import subprocess
from selenium import webdriver


# download the ChromeDriver binary from:
# https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json
# very important the version of the ChromeDriver binary must match the version of the Chrome browser installed
# PS> (Get-Item "C:\Program Files\Google\Chrome\Application\chrome.exe").VersionInfo

# start the browser session
print("Starting the browser session...")
service = webdriver.ChromeService(port=12345,
                                  log_output=subprocess.STDOUT,
                                  service_args=['--log-level=DEBUG'],  # --explicitly-allowed-ports=6666" (remove "X started debugging ...")
                                  executable_path="C:/Users/hecto/Documents/UTP/ChromeDrivers/chromedriver-win64/chromedriver.exe")
# log levels: ALL, DEBUG, INFO, WARNING, SEVERE, and OFF
# log to file:
#   service_args=['--append-log', '--readable-timestamp']
#   log_output='chromedriver-' + datetime.now().strftime("%y%m%d_%H%M%S") + '.log'
driver = webdriver.Chrome(service=service)

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
