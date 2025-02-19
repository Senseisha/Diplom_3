import allure
from curl import *
from pages.personal_account_page import PersonalAccount


class TestPersonalAccount:
    @allure.title('Тест успешного перехода в Личный кабинет')
    def test_successful_transition(self, driver, transition_to_personal_account):
        personal_acc = PersonalAccount(driver)
        current_url = personal_acc.get_current_url()
        assert current_url == auth_endpoint

    @allure.title('Тест успешного перехода в раздел истории заказов')
    def test_successful_transition_to_order_history(self, driver, login_user):
        section_order_history = PersonalAccount(driver)
        section_order_history.click_on_order_to_account()
        section_order_history.click_on_order_history()
        section_order_history.wait_to_go_to_order_history_section()
        current_url = section_order_history.get_current_url()
        assert current_url == order_history

    @allure.title('Тест успешного выхода из аккаунта')
    def test_successful_exit(self, driver, login_user):
        exit_from_acc = PersonalAccount(driver)
        exit_from_acc.click_on_order_to_account()
        exit_from_acc.click_on_button_exit()
        exit_from_acc.wait_to_go_to_main_page()
        current_url = exit_from_acc.get_current_url()
        assert current_url == auth_endpoint
