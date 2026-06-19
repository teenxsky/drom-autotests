import allure

from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators

MAIN_URL = "https://www.drom.ru/"


class MainPage(BasePage):
    locators = MainPageLocators()

    @allure.step("Открыть главную страницу drom.ru")
    def open_main(self):
        self.open(MAIN_URL)

    @allure.step("Проверить, что шапка сайта отображается")
    def is_header_visible(self):
        return self.is_visible(self.locators.HEADER)

    @allure.step("Перейти в раздел «Отзывы» через верхнее меню")
    def go_to_reviews(self):
        self.click(self.locators.MENU_REVIEWS)

    @allure.step("Перейти в раздел «Каталог» через верхнее меню")
    def go_to_catalog(self):
        self.click(self.locators.MENU_CATALOG)
