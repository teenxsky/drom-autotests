import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

CLICK_RETRY = 5
DEFAULT_TIMEOUT = 20


class BasePage:
    """
    Базовая логика, применимая ко всем страницам (BasePage из лекции).

    Общие методы (find, click, wait) построены на явных ожиданиях
    (Explicit Wait). Sleep не используется - это антипаттерн.
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self, url: str) -> None:
        self.driver.get(url)

    def wait(self, timeout: int = DEFAULT_TIMEOUT) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout=timeout)

    # ждём появления элемента в DOM-дереве
    def find(self, locator: tuple[str, str], timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        return self.wait(timeout).until(expected_conditions.presence_of_element_located(locator))

    # ждём, пока элемент станет видимым
    def find_visible(self, locator: tuple[str, str], timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        return self.wait(timeout).until(expected_conditions.visibility_of_element_located(locator))

    def find_all(
        self,
        locator: tuple[str, str],
        timeout: int = DEFAULT_TIMEOUT,
    ) -> list[WebElement]:
        return self.wait(timeout).until(
            expected_conditions.presence_of_all_elements_located(locator),
        )

    # ждём, пока элемент станет видимым и активным.
    def click(self, locator: tuple[str, str]) -> None:
        for i in range(CLICK_RETRY):
            try:
                element = self.wait().until(expected_conditions.element_to_be_clickable(locator))
                element.click()
                return

            except (
                StaleElementReferenceException,
                ElementClickInterceptedException,
                TimeoutException,
            ):
                if i == CLICK_RETRY - 1:
                    raise

    def type(self, locator: tuple[str, str], text: str) -> WebElement:
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

        return element

    def get_url(self) -> str:
        return self.driver.current_url

    def get_title(self) -> str:
        return self.driver.title

    def wait_url_contains(self, fragment: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
        return self.wait(timeout).until(expected_conditions.url_contains(fragment))

    def is_visible(self, locator: tuple[str, str], timeout: int = DEFAULT_TIMEOUT) -> bool:
        try:
            return self.find_visible(locator, timeout).is_displayed()
        except TimeoutException:
            return False

    @allure.step('Сделать скриншот: {name}')
    def attach_screenshot(self, name: str = 'screenshot') -> None:
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
