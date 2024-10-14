import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # start the browser session
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    # close the browser session
    chrome_driver.close()
    chrome_driver.quit()


def test_simple_webdriver_local(driver):
    # navigate to the page
    driver.get("http://localhost:10081/web-apps/events/index.html")

    # get the title of the page
    title = driver.title

    assert title == "Events Application"
