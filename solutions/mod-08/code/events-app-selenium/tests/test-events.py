import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class TestSimpletest:

    @pytest.fixture
    def setup_driver(self):
        driver = webdriver.Chrome()
        WebDriverWait(driver, timeout=5)
        yield driver

    @pytest.fixture()
    def teardown(self, setup_driver):
        setup_driver.quit()

    def test_simpletest(self, setup_driver):

        # Open /web-apps/events-modular/index.html
        setup_driver.get("http://localhost:18001/web-apps/events-modular/index.html")
        # set window size
        setup_driver.set_window_size(1200, 1200)

        time.sleep(3)

        # Click in the Navbar Dropdown menu
        setup_driver.find_element(By.ID, "navbarDropdown").click()

        # Click in the Create Event element
        setup_driver.find_element(By.LINK_TEXT, "Create Event").click()

        # Click inside the description element
        setup_driver.find_element(By.NAME, "ce-description").click()

        # Write "test event" in the description element (text field)
        setup_driver.find_element(By.NAME, "ce-description").send_keys("test event")

        # Click in the private option
        setup_driver.find_element(By.ID, "private").click()

        # Click in the event date calendar
        setup_driver.find_element(By.NAME, "ce-date").click()

        # Select the date
        setup_driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > .day:nth-child(5)").click()

        # Submit the event
        setup_driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

        # Close the popup window with the JSON event summary
        setup_driver.find_element(By.CSS_SELECTOR, "#eventModal .btn").click()

        time.sleep(2)

        # Click in the Navbar Dropdown menu
        setup_driver.find_element(By.ID, "navbarDropdown").click()

        # Click in the List Events element
        setup_driver.find_element(By.LINK_TEXT, "List Events").click()

        # Click in the About element
        setup_driver.find_element(By.ID, "aboutMenuItem").click()

        # Mouse over the About element
        element = setup_driver.find_element(By.ID, "aboutMenuItem")
        actions = ActionChains(setup_driver)
        actions.move_to_element(element).perform()

        # Mouse out the About element
        element = setup_driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(setup_driver)
        actions.move_to_element_with_offset(element, 0, 0).perform()

        # Click on the About Modal close button
        setup_driver.find_element(By.CSS_SELECTOR, "#aboutModal .btn").click()

        # Click in the Home menu
        setup_driver.find_element(By.LINK_TEXT, "Home").click()

        time.sleep(1)

        # Click in the Navbar Dropdown menu
        setup_driver.find_element(By.ID, "navbarDropdown").click()

        # Click in the List Events element
        setup_driver.find_element(By.LINK_TEXT, "List Events").click()

        # Click in the Delete button
        setup_driver.find_element(By.CSS_SELECTOR, ".btn-sm").click()
        # Mouse over the confirmation popup
        element = setup_driver.find_element(By.CSS_SELECTOR, ".btn-sm")
        actions = ActionChains(setup_driver)
        actions.move_to_element(element).perform()
        # Mouse out the confirmation popup and click on cancel
        element = setup_driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(setup_driver)
        actions.move_to_element_with_offset(element, 0, 0).perform()

        # Click on the delete button
        setup_driver.find_element(By.CSS_SELECTOR, "#deleteConfirmModal .btn-secondary").click()

        setup_driver.find_element(By.CSS_SELECTOR, ".btn-sm").click()

        element = setup_driver.find_element(By.CSS_SELECTOR, ".btn-sm")
        actions = ActionChains(setup_driver)
        actions.move_to_element(element).perform()

        element = setup_driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(setup_driver)
        actions.move_to_element_with_offset(element, 0, 0).perform()

        setup_driver.find_element(By.ID, "confirmDeleteBtn").click()

        time.sleep(1)

        setup_driver.find_element(By.ID, "navbarDropdown").click()

        setup_driver.find_element(By.LINK_TEXT, "List Events").click()
