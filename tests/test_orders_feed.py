import allure
import pytest

from pages.orders_feed_page import OrdersFeedPage
from locators.orders_feed_page_locators import OrdersFeedPageLocators


class TestOrdersFeed:
    @allure.title('Тест успешного открытия окна с деталями при клике на заказ')
    def test_success_open_popup(self, driver):
        open_popup = OrdersFeedPage(driver)
        # "залогиниться"
        open_popup.main_page_loading_wait()
        open_popup.click_on_orders_feed()
        open_popup.click_on_order()
        assert open_popup.wait_for_popup_with_details().is_displayed() is True

    @allure.title('Тест проверки успешного отображения заказов пользователя на странице "Лента заказов"')
    def test_display_user_orders(self, driver):
        user_orders = OrdersFeedPage(driver)
        "залогиниться"
        user_orders.main_page_loading_wait()
        user_orders.drag_and_drop_ingredient()
        user_orders.click_on_button_ordering()
        # user_orders.get_ordering_popup_text()
        "получить номер заказа"
        user_orders.close_popup()
        user_orders.click_on_order_to_account()
        user_orders.wait_for_entry()
        user_orders.click_on_order_history()
        "проверка есть ли айди в истории"
        user_orders.click_on_orders_feed()
        "проверка есть ли айди в ленте заказов"
        # assert

    @allure.title('Тест проверки увеличения счетчика при создании нового заказа')
    @pytest.mark.parametrize('counter', [OrdersFeedPageLocators.ALL_TIME_COUNTER, OrdersFeedPageLocators.TODAY_COUNTER])
    def test_counter_increase(self, driver, counter):
        increase_counter = OrdersFeedPage(driver)
        "залогиниться"
        increase_counter.main_page_loading_wait()
        increase_counter.click_on_orders_feed()
        initial_count = increase_counter.get_initial_count(counter)
        increase_counter.click_on_constructor()
        increase_counter.drag_and_drop_ingredient()
        increase_counter.click_on_button_ordering()
        # increase_counter.get_ordering_popup_text()
        increase_counter.close_popup()
        increase_counter.click_on_orders_feed()
        current_count = increase_counter.get_initial_count(counter)
        assert current_count > initial_count

    @allure.title('Тест проверки появления номера заказа в разделе "В работе" после оформления')
    def test_appearance_of_the_order_number(self, driver):
        in_progress = OrdersFeedPage(driver)
        "залогиниться"
        in_progress.main_page_loading_wait()
        in_progress.drag_and_drop_ingredient()
        in_progress.click_on_button_ordering()
        # in_progress.get_ordering_popup_text()
        order_number = "получить айди заказа"
        in_progress.close_popup()
        in_progress.click_on_orders_feed()
        number_of_order = "получить номер заказа"
        order_in_progress = in_progress.get_text_order_number_in_progress()
        assert order_number == order_in_progress









