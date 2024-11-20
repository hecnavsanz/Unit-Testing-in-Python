# python.exe -m pytest -svv .\test_onlineshop_login_logout.py
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class TestOnlineshopLoginLogout():


  @pytest.fixture(scope="session")
  def options(self):
    c_options = Options()
    c_options.add_argument("--disable-features=DisconnectExtensionMessagePortWhenPageEntersBFCache")
    return c_options


  @pytest.fixture(scope="session")
  def setup(self, options):
    print('starting setup ...')
    c_driver = webdriver.Chrome(options=options)
    c_driver.implicitly_wait(2)
    yield c_driver


  @pytest.fixture(scope="session")
  def teardown(self, setup):
    print('Finishing setup ...')
    setup.quit()


  def test_onlineshoplogin(self, setup):
    print('Testing login feature ...')
    setup.get("http://localhost:8000/")
    setup.set_window_size(1202, 1008)
    setup.find_element(By.NAME, "username").click()
    setup.find_element(By.NAME, "username").send_keys("test")
    setup.find_element(By.NAME, "password").send_keys("Pytest-TDD.Labs_4ALL")
    setup.find_element(By.CSS_SELECTOR, ".is-link").click()


  def test_onlineshoplogout(self, setup):
    print('Testing logout feature ...')
    setup.get("http://localhost:8000/")
    setup.set_window_size(1188, 1008)
    setup.find_element(By.LINK_TEXT, "test").click()
    setup.close()
