import time

from selenium import webdriver


# options for the browser
options = webdriver.ChromeOptions()
# available browser versions: stable, beta, dev (must be installed the related browser executable)
# options.browser_version = 'stable'
# available page load strategies: normal, eager, none
options.page_load_strategy = 'normal'
# platform name: linux, mac, windows, any
options.platform_name = 'windows'

# browserName set by default when new Options class instance is created
print("Using browser:", options.to_capabilities()['browserName'])

# accept insecure certificates (not trusted) will cause an error that can be ignored:
#   CertVerifyProcBuiltin for localhost failed: ... ERROR: No matching issuer found
# if not accepted then the error will crash the browser session:
#   handshake failed; returned -1, SSL error code 1, net_error -202 ... Privacy error
# options.accept_insecure_certs = True
# alternative to the previous option is to use browser cmd-line switches:
options.add_argument('--ignore-certificate-errors')

# set the browser profile (use chrome://version to get the Profile directory)
options.add_argument('--profile-directory=Profile 4')
# alternative to the previous option is to use browser cmd-line switches:
# options.add_argument('--user-data-dir=' + 'C:/Users/hecto/AppData/Local/Google/Chrome/User Data/Profile 3')

# start the browser session
print("Starting the browser session ...")
driver = webdriver.Chrome(options=options)

# navigate to the page (HTTPS)
print("HTTPS - Navigating to the page...")
driver.get("https://localhost:10082/web-apps/events/index.html")

time.sleep(10)

# get the title of the page
print("Getting the title of the page...")
title = driver.title
print("Page title =", title)

# close the browser session
print("Closing the browser session ...")
driver.quit()
