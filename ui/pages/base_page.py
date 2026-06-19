import allure
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CLICK_RETRY = 5
DEFAULT_TIMEOUT = 20


class BasePage(object):
    """
    Базовая логика, применимая ко всем страницам (BasePage из лекции).

    Общие методы (find, click, wait) построены на явных ожиданиях
    (Explicit Wait). Sleep не используется - это антипаттерн.
    """

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def wait(self, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    # ждём появления элемента в DOM-дереве
    def find(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    # ждём, пока элемент станет видимым
    def find_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def find_all(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    # ждём, пока элемент станет видимым и активным.
    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                element = self.wait().until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except (StaleElementReferenceException,
                    ElementClickInterceptedException,
                    TimeoutException):
                if i == CLICK_RETRY - 1:
                    raise

    def type(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)
        return element

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def wait_url_contains(self, fragment, timeout=DEFAULT_TIMEOUT):
        return self.wait(timeout).until(EC.url_contains(fragment))

    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            return self.find_visible(locator, timeout).is_displayed()
        except TimeoutException:
            return False

    @allure.step("Сделать скриншот: {name}")
    def attach_screenshot(self, name="screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
