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

class TestOnlineshoplogout():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://10.20.0.100:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_onlineshoplogout(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(1188, 1008)
    self.driver.find_element(By.LINK_TEXT, "test").click()
    self.driver.close()
  
