import allure
from curl import *
from pages.personal_account_page import PersonalAccount


class TestPersonalAccount:
    @allure.title('Тест успешного перехода в Личный кабинет')
    def test_successful_transition(self, driver, transition_to_personal_account):
        #залогиниться через фикстуру
        # personal_account = PersonalAccount(driver)
        # personal_account.main_page_loading_wait()
        # personal_account.click_on_order_to_account()
        # personal_account.wait_for_entry()
        assert driver.current_url == profile_endpoint

    @allure.title('Тест успешного перехода в раздел истории заказов')
    def test_successful_transition_to_order_history(self, driver, transition_to_personal_account):
        section_order_history = PersonalAccount(driver)
        section_order_history.click_on_order_history()
        section_order_history.wait_to_go_to_order_history_section()
        assert driver.current_url == order_history

    @allure.title('Тест успешного выхода из аккаунта')
    def test_successful_exit(self, driver, transition_to_personal_account):
        exit_from_acc = PersonalAccount(driver)
        exit_from_acc.click_on_exit()
        exit_from_acc.wait_to_go_to_main_page()
        assert driver.current_url == main_site

