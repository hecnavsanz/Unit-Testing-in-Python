from behave import fixture
from behave import use_fixture
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@fixture
def driver(context):
    driver = webdriver.Chrome()
    WebDriverWait(driver, timeout=10)
    context.driver = driver
    yield
    context.driver.quit()


def before_scenario(context, scenario):
    use_fixture(driver, context)
