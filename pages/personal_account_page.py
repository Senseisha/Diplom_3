import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.personal_account_page_locators import PersonalAccountPageLocators


class PersonalAccount(BasePage):
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть на элемент "Личный кабинет"')
    def click_on_order_to_account(self):
        self.click_on_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Подождать перехода на страницу профиля')
    def wait_for_entry(self):
        self.wait_for_element(PersonalAccountPageLocators.PROFILE)

    @allure.step('Кликнуть на элемент "История заказов"')
    def click_on_order_history(self):
        self.click_on_element(PersonalAccountPageLocators.CLICK_ORDER_HISTORY)

    @allure.step('Подождать перехода в раздел "История заказов"')
    def wait_to_go_to_order_history_section(self):
        self.wait_for_element(PersonalAccountPageLocators.ORDER_HISTORY)

    @allure.step('Кликнуть на элемент "Выход"')
    def click_on_exit(self):
        self.click_on_element(PersonalAccountPageLocators.EXIT)

    @allure.step('Дождаться перехода на главную страницу')
    def wait_to_go_to_main_page(self):
        self.wait_for_element(MainPageLocators.ORDER_TEXT)




