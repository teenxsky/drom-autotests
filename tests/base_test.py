import pytest
from selenium.webdriver.remote.webdriver import WebDriver


class BaseTest:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
