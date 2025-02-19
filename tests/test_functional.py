import allure
import data
from curl import *
from pages.functional_page import FunctionalPage


class TestMainFunctional:
    @allure.title('Тест успешного перехода в раздел "Лента заказов"')
    def test_successful_transition_to_orders_feed(self, driver):
        orders_feed = FunctionalPage(driver)
        orders_feed.main_page_loading_wait()
        orders_feed.click_on_orders_feed()
        orders_feed.wait_for_orders_feed()
        current_url = orders_feed.get_current_url()
        assert current_url == feed_orders

    @allure.title('Тест успешного перехода в раздел "Конструктор"')
    def test_successful_transition_to_constructor(self, driver):
        constructor = FunctionalPage(driver)
        constructor.main_page_loading_wait()
        constructor.click_on_orders_feed()
        constructor.click_on_constructor()
        constructor.wait_for_section_constructor()
        current_url = constructor.get_current_url()
        assert current_url == main_site + '/'

    @allure.title('Тест успешного появления окна с деталями при клике на ингредиент')
    def test_appears_window_with_details(self, driver, popup_with_details):
        details_popup = FunctionalPage(driver)
        assert details_popup.get_details_popup_text() == data.details

    @allure.title('Тест успешного закрытия окна нажатием на крестик')
    def test_close_window(self, driver, popup_with_details):
        close_popup = FunctionalPage(driver)
        close_popup.click_on_cross_button()
        assert close_popup.check_popup_is_invisible() is False

    @allure.title('Тест проверки увеличения каунтера при добавлении ингредиента в заказ')
    def test_count_increase(self, driver):
        counter = FunctionalPage(driver)
        counter.main_page_loading_wait()
        initial_count = counter.get_ingredient_count()
        counter.drag_and_drop_ingredient()
        current_count = counter.get_ingredient_count()
        assert int(initial_count) < int(current_count)

    @allure.title('Тест успешного оформления заказа залогиненным пользователем')
    def test_successful_ordering(self, driver, login_user):
        order = FunctionalPage(driver)
        order.main_page_loading_wait()
        order.drag_and_drop_ingredient()
        order.click_on_button_ordering()
        assert order.get_ordering_popup_text() == data.prepared_order



