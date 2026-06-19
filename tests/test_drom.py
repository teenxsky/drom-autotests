import allure
import pytest
from base_test import BaseTest

from ui.pages.listing_page import ListingPage
from ui.pages.main_page import MainPage


@allure.epic('drom.ru')
@allure.feature('Поиск и фильтрация объявлений о продаже авто')
class TestDrom(BaseTest):
    """
    10 автотестов для drom.ru.

    Покрываемый функционал: главная страница, список объявлений, карточки
    (заголовок и цена), фильтрация по цене, открытие объявления, пагинация,
    листинг по марке, навигация по меню.
    """

    @pytest.mark.UI
    @allure.title('TC-01. Главная страница открывается, шапка видна')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_main_page_loads(self, main_page: MainPage) -> None:
        main_page.open_main()
        assert main_page.is_header_visible(), 'Шапка сайта не отображается'
        assert 'Дром' in main_page.get_title(), (
            f'Неожиданный заголовок страницы: {main_page.get_title()!r}'
        )

    @pytest.mark.UI
    @allure.title('TC-02. Список объявлений содержит карточки')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_listing_has_cards(self, listing_page: ListingPage) -> None:
        listing_page.open_all()
        assert listing_page.cards_count() > 0, 'На странице нет карточек объявлений'

    @pytest.mark.UI
    @allure.title('TC-03. У первой карточки есть заголовок и цена')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_first_card_has_title_and_price(self, listing_page: ListingPage) -> None:
        listing_page.open_all()
        assert listing_page.first_title() != '', 'Заголовок первой карточки пуст'
        assert listing_page.first_price() != '', 'Цена первой карточки пуста'

    @pytest.mark.UI
    @allure.title('TC-04. У всех карточек страницы отображается цена')
    @allure.severity(allure.severity_level.NORMAL)
    def test_all_cards_have_price(self, listing_page: ListingPage) -> None:
        listing_page.open_all()
        assert listing_page.all_cards_have_price(), 'Не у всех карточек на странице есть цена'

    @pytest.mark.UI
    @allure.title('TC-05. Фильтр по минимальной цене отражается в URL')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_filter_min_price(self, listing_page: ListingPage) -> None:
        listing_page.open_all()
        listing_page.set_min_price(500000)
        listing_page.apply_filters()
        listing_page.wait_url_contains('minprice=500000')
        assert 'minprice=500000' in listing_page.get_url()
        assert listing_page.cards_count() > 0, 'После фильтра нет объявлений'

    @pytest.mark.UI
    @allure.title('TC-06. Фильтр по диапазону цены отражается в URL')
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_price_range(self, listing_page: ListingPage) -> None:
        listing_page.open_all()
        listing_page.set_min_price(300000)
        listing_page.set_max_price(900000)
        listing_page.apply_filters()
        listing_page.wait_url_contains('maxprice=900000')
        url = listing_page.get_url()
        assert 'minprice=300000' in url and 'maxprice=900000' in url, (
            f'Параметры цены не отражены в URL: {url}'
        )

    @pytest.mark.UI
    @allure.title('TC-07. Открытие карточки объявления')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_advertisement(self, listing_page: ListingPage) -> None:
        listing_page.open_all()
        ad = listing_page.open_first_ad()
        ad.wait_url_contains('.html')
        assert ad.has_title(), 'Заголовок объявления пуст'

    @pytest.mark.UI
    @allure.title('TC-08. Пагинация: переход на вторую страницу')
    @allure.severity(allure.severity_level.NORMAL)
    def test_pagination_second_page(self, listing_page: ListingPage) -> None:
        listing_page.open_all()
        listing_page.go_to_page_2()
        listing_page.wait_url_contains('page2')
        assert 'page2' in listing_page.get_url(), 'Не выполнен переход на 2-ю страницу'
        assert listing_page.cards_count() > 0, 'На второй странице нет карточек'

    @pytest.mark.UI
    @allure.title('TC-09. Листинг по марке содержит объявления этой марки')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_brand_listing(self, listing_page: ListingPage) -> None:
        listing_page.open_brand('toyota')
        assert 'toyota' in listing_page.get_url(), 'URL не соответствует марке'
        titles = listing_page.get_titles()[:5]
        assert titles, 'Нет объявлений по марке'
        assert all('Toyota' in t for t in titles), f'Среди заголовков есть не-Toyota: {titles}'

    @pytest.mark.UI
    @allure.title('TC-10. Навигация в раздел «Отзывы» через меню')
    @allure.severity(allure.severity_level.MINOR)
    def test_menu_navigation_reviews(self, main_page: MainPage) -> None:
        main_page.open_main()
        main_page.go_to_reviews()
        main_page.wait_url_contains('/reviews/')
        assert '/reviews/' in main_page.get_url(), 'Переход в раздел «Отзывы» не выполнен'
