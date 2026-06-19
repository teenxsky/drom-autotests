import allure

from ui.locators.main_page_locators import MainPageLocators
from ui.pages.base_page import BasePage

MAIN_URL = 'https://www.drom.ru/'


class MainPage(BasePage):
    locators = MainPageLocators()

    @allure.step('Открыть главную страницу drom.ru')
    def open_main(self) -> None:
        self.open(MAIN_URL)

    @allure.step('Проверить, что шапка сайта отображается')
    def is_header_visible(self) -> bool:
        return self.is_visible(self.locators.HEADER)

    @allure.step('Перейти в раздел «Отзывы» через верхнее меню')
    def go_to_reviews(self) -> None:
        self.click(self.locators.MENU_REVIEWS)

    @allure.step('Перейти в раздел «Каталог» через верхнее меню')
    def go_to_catalog(self) -> None:
        self.click(self.locators.MENU_CATALOG)
