from selenium.webdriver.common.by import By


class ListingPageLocators:
    # карточки объявлений и их элементы.
    CARDS = (By.CSS_SELECTOR, "[data-ftid='bulls-list_bull']")
    CARD_TITLES = (By.CSS_SELECTOR, "a[data-ftid='bull_title']")
    CARD_PRICES = (By.CSS_SELECTOR, "[data-ftid='bull_price']")

    # фильтр по цене
    PRICE_FROM = (By.CSS_SELECTOR, "[data-ftid='sales__filter_price-from']")
    PRICE_TO = (By.CSS_SELECTOR, "[data-ftid='sales__filter_price-to']")

    # кнопка 'Показать' (поиск по тексту) и пагинация (выбор по тексту)
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(.,'Показать')]")
    PAGE_LINK_2 = (By.XPATH, "//a[@data-ftid='component_pagination-item'][normalize-space()='2']")
