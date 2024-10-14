import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # start the browser session
    options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Remote(command_executor="http://10.20.0.100:4444/wd/hub", options=options)
    yield chrome_driver
    # close the browser session
    chrome_driver.close()
    chrome_driver.quit()


def test_simple_webdriver_local(driver):

    # navigate to the page
    driver.get("http://10.20.0.201/web-apps/events/index.html")

    # get the title of the page
    title = driver.title

    assert title == "Events Application"
