import allure

from ui.locators.ad_page_locators import AdPageLocators
from ui.pages.base_page import BasePage


class AdPage(BasePage):
    locators = AdPageLocators()

    @allure.step('Получить заголовок объявления')
    def get_title(self) -> str:
        return self.find_visible(self.locators.TITLE).text.strip()

    @allure.step('Проверить, что заголовок объявления непустой')
    def has_title(self) -> bool:
        return len(self.get_title()) > 0
