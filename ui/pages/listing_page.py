import allure
from selenium.webdriver.common.keys import Keys

from ui.locators.listing_page_locators import ListingPageLocators
from ui.pages.ad_page import AdPage
from ui.pages.base_page import BasePage

ALL_URL = "https://auto.drom.ru/all/"
BRAND_URL = "https://auto.drom.ru/{brand}/"


class ListingPage(BasePage):
    locators = ListingPageLocators()

    @allure.step("Открыть список всех объявлений")
    def open_all(self):
        self.open(ALL_URL)
        self._ensure_loaded()

    @allure.step("Открыть объявления марки: {brand}")
    def open_brand(self, brand):
        self.open(BRAND_URL.format(brand=brand))
        self._ensure_loaded()

    def _ensure_loaded(self, attempts=4):
        # Drom при частых запросах может ответить 429 Too Many Requests или страницей c проверкой
        # Поэтому здесь бэкофф для соблюдения rate-limit сервера
        import time
        for i in range(attempts):
            try:
                self.find_all(self.locators.CARDS, timeout=8)
                return
            except Exception:
                if i == attempts - 1:
                    raise
                time.sleep(8 * (i + 1))
                self.driver.refresh()

    @allure.step("Получить карточки объявлений")
    def get_cards(self):
        return self.find_all(self.locators.CARDS)

    @allure.step("Получить количество карточек")
    def cards_count(self):
        return len(self.get_cards())

    @allure.step("Получить заголовки объявлений")
    def get_titles(self):
        return [e.text.strip() for e in self.find_all(self.locators.CARD_TITLES)]

    @allure.step("Получить заголовок первой карточки")
    def first_title(self):
        return self.find_all(self.locators.CARD_TITLES)[0].text.strip()

    @allure.step("Получить цену первой карточки")
    def first_price(self):
        return self.find_all(self.locators.CARD_PRICES)[0].text.strip()

    @allure.step("Проверить, что у всех карточек есть цена")
    def all_cards_have_price(self):
        return len(self.find_all(self.locators.CARD_PRICES)) == self.cards_count()

    @allure.step("Задать минимальную цену: {value}")
    def set_min_price(self, value):
        self.type(self.locators.PRICE_FROM, str(value))

    @allure.step("Задать максимальную цену: {value}")
    def set_max_price(self, value):
        self.type(self.locators.PRICE_TO, str(value))

    @allure.step("Нажать кнопку «Показать»")
    def apply_filters(self):
        self.click(self.locators.SUBMIT_BUTTON)

    @allure.step("Открыть первое объявление из списка")
    def open_first_ad(self):
        self.find_all(self.locators.CARD_TITLES)[0].click()
        return AdPage(self.driver)

    @allure.step("Перейти на вторую страницу списка")
    def go_to_page_2(self):
        self.click(self.locators.PAGE_LINK_2)
