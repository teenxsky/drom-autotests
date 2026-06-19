import os
from collections.abc import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.ad_page import AdPage
from ui.pages.base_page import BasePage
from ui.pages.listing_page import ListingPage
from ui.pages.main_page import MainPage

BASE_URL = 'https://www.drom.ru/'


@pytest.fixture
def base_page(driver: webdriver.Chrome) -> BasePage:
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver: webdriver.Chrome) -> MainPage:
    return MainPage(driver=driver)


@pytest.fixture
def listing_page(driver: webdriver.Chrome) -> ListingPage:
    return ListingPage(driver=driver)


@pytest.fixture
def ad_page(driver: webdriver.Chrome) -> AdPage:
    return AdPage(driver=driver)


def get_driver() -> webdriver.Chrome:
    options = Options()

    if os.getenv('HEADLESS') == '1':
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--lang=ru-RU')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    )

    if os.getenv('USE_SELENIUM_MANAGER') == '1':
        browser = webdriver.Chrome(options=options)
    else:
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)

    return browser


@pytest.fixture(scope='function')
def driver() -> Generator[WebDriver]:
    browser = get_driver()
    yield browser
    browser.quit()
