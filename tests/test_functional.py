import allure
from curl import *
from pages.functional_page import FunctionalPage


class TestMainFunctional:
    @allure.title('Тест успешного перехода в раздел "Лента заказов"')
    def test_successful_transition_to_orders_feed(self, driver):
        orders_feed = FunctionalPage(driver)
        orders_feed.main_page_loading_wait()
        orders_feed.click_on_orders_feed()
        orders_feed.wait_for_orders_feed()
        assert driver.current_url == feed_orders

    @allure.title('Тест успешного перехода в раздел "Конструктор"')
    def test_successful_transition_to_constructor(self, driver):
        constructor = FunctionalPage(driver)
        constructor.main_page_loading_wait()
        constructor.click_on_orders_feed()
        constructor.click_on_constructor()
        constructor.wait_for_section_constructor()
        assert driver.current_url == main_site + '/'

    @allure.title('Тест успешного появления окна с деталями при клике на ингредиент')
    def test_appears_window_with_details(self, driver):
        details_window = FunctionalPage(driver)
        details_window.main_page_loading_wait()
        details_window.click_on_ingredient()
        details_window.wait_for_window_with_details()

        assert details_window.get_details_window_text('Детали ингредиента')
