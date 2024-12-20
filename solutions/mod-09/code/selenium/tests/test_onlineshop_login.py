# Generated by Selenium IDE
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

class TestOnlineshoplogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.driver.implicitly_wait(2)

  def teardown_method(self, method):
    self.driver.quit()

  def test_onlineshoplogin(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(1202, 1008)
    self.driver.find_element(By.LINK_TEXT, "none").click()
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("test")
    self.driver.find_element(By.NAME, "password").send_keys("Pytest-TDD.Labs_4ALL")
    self.driver.find_element(By.CSS_SELECTOR, ".is-link").click()

