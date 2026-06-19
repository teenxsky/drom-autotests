from selenium.webdriver.common.by import By


class MainPageLocators:
    # data-атрибуты
    HEADER = (By.CSS_SELECTOR, "[data-ftid='component_header']")
    SEARCH_VIN = (By.CSS_SELECTOR, "[data-ftid='autostory-widget_input']")

    # пункты верхнего меню
    MENU_CARS = (
        By.XPATH,
        "//a[@data-ftid='component_header_main-menu-item'][contains(.,'Автомобили')]",
    )
    MENU_REVIEWS = (
        By.XPATH,
        "//a[@data-ftid='component_header_main-menu-item'][contains(.,'Отзывы')]",
    )
    MENU_CATALOG = (
        By.XPATH,
        "//a[@data-ftid='component_header_main-menu-item'][contains(.,'Каталог')]",
    )
