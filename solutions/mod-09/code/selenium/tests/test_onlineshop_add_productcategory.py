
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class TestOnlineshopaddproductcategory():

    @pytest.fixture(scope="session")
    def options(self):
        c_options = Options()
        # to avoid error: The page keeping the extension port is moved into back/forward cache, so the message
        # channel is closed. c_options.add_argument(
        # "--disable-features=DisconnectExtensionMessagePortWhenPageEntersBFCache")
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

    def test_onlineshopaddproductcategory(self, setup):
        setup.get("http://localhost:8000/")
        setup.set_window_size(1289, 1008)

        setup.find_element(By.LINK_TEXT, "none").click()

        setup.find_element(By.NAME, "username").click()
        setup.find_element(By.NAME, "username").send_keys("test")
        setup.find_element(By.NAME, "password").send_keys("Pytest-TDD.Labs_4ALL")
        setup.find_element(By.CSS_SELECTOR, ".is-link").click()

        element = setup.find_element(By.LINK_TEXT, "Products")
        actions = ActionChains(setup)
        actions.move_to_element(element).perform()
        element = setup.find_element(By.LINK_TEXT, "Categories List")
        actions = ActionChains(setup)
        actions.move_to_element(element).perform()
        setup.find_element(By.LINK_TEXT, "Categories List").click()

        setup.find_element(By.LINK_TEXT, "Add").click()
        setup.find_element(By.NAME, "prod_cat_name").click()
        setup.find_element(By.NAME, "prod_cat_name").send_keys("TETE")
        setup.find_element(By.NAME, "prod_cat_code").click()
        setup.find_element(By.NAME, "prod_cat_code").send_keys("TE")
        setup.find_element(By.CSS_SELECTOR, ".is-link").click()

        setup.find_element(By.LINK_TEXT, "test").click()
        setup.close()
