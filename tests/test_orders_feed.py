import allure
import pytest
from pages.orders_feed_page import OrdersFeedPage
from locators.orders_feed_page_locators import OrdersFeedPageLocators


class TestOrdersFeed:
    @allure.title('Тест успешного открытия окна с деталями при клике на заказ')
    def test_success_open_popup(self, driver, login_user):
        open_popup = OrdersFeedPage(driver)
        open_popup.main_page_loading_wait()
        open_popup.click_on_orders_feed()
        open_popup.click_on_order()
        assert open_popup.wait_for_popup_with_details().is_displayed() is True

    @allure.title('Тест проверки успешного отображения заказов пользователя на странице "Лента заказов"')
    def test_display_user_orders(self, driver, login_user):
        user_orders = OrdersFeedPage(driver)
        user_orders.main_page_loading_wait()
        user_orders.drag_and_drop_ingredient()
        user_orders.click_on_button_ordering()

        user_orders.wait_for_order_number()
        order_id = user_orders.get_order_number_text()
        user_orders.close_popup()

        user_orders.click_on_order_to_account()
        user_orders.wait_for_entry_to_profile()
        user_orders.click_on_order_history()
        order_id_in_order_history = user_orders.is_order_id_in_history_list(order_id)

        user_orders.click_on_orders_feed()
        order_id_in_orders_feed = user_orders.is_order_id_in_feed_list(order_id)

        assert order_id_in_order_history and order_id_in_orders_feed

    @allure.title('Тест проверки увеличения счетчика при создании нового заказа')
    @pytest.mark.parametrize('counter', [OrdersFeedPageLocators.ALL_TIME_COUNTER, OrdersFeedPageLocators.TODAY_COUNTER])
    def test_counter_increase(self, driver, counter, login_user):
        orders = OrdersFeedPage(driver)
        orders.main_page_loading_wait()

        orders.click_on_orders_feed()
        initial_count = orders.get_initial_count(counter)

        orders.click_on_constructor()
        orders.drag_and_drop_ingredient()
        orders.click_on_button_ordering()

        orders.wait_for_order_number()
        orders.close_popup()

        orders.click_on_orders_feed()
        current_count = orders.get_initial_count(counter)

        assert int(current_count) > int(initial_count)

    @allure.title('Тест проверки появления номера заказа в разделе "В работе" после оформления')
    def test_appearance_of_the_order_number(self, driver, login_user):
        orders = OrdersFeedPage(driver)
        orders.main_page_loading_wait()
        orders.drag_and_drop_ingredient()
        orders.click_on_button_ordering()

        orders.wait_for_order_number()
        order_id = orders.get_order_number_text()
        orders.close_popup()

        orders.click_on_orders_feed()
        order_in_progress = orders.get_text_order_number_in_progress(order_id)
        assert order_in_progress









