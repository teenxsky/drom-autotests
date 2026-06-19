from selenium.webdriver.common.by import By


class AdPageLocators:
    # h1 присутствует на странице объявления
    TITLE = (By.XPATH, "//h1")
    # блок с ценой на странице объявления
    PRICE = (By.CSS_SELECTOR, "[data-ftid='component_price'], .price-block__price")
