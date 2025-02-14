import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.personal_account_page_locators import PersonalAccountPageLocators
from locators.functional_page_locators import FunctionalPageLocators
from locators.orders_feed_page_locators import OrdersFeedPageLocators


class OrdersFeedPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть на раздел "Лента заказов"')
    def click_on_orders_feed(self):
        self.click_on_element(FunctionalPageLocators.ORDERS_FEED)

    @allure.step('Кликнуть на заказ')
    def click_on_order(self):
        self.click_on_element(OrdersFeedPageLocators.ORDER)

    @allure.step('Дождаться появления окна с деталями')
    def wait_for_popup_with_details(self):
        self.wait_for_element(OrdersFeedPageLocators.DETAILS_POPUP)

    @allure.step('Добавить ингредиент в корзину')
    def drag_and_drop_ingredient(self):
        return self.drag_drop(FunctionalPageLocators.INGREDIENT, FunctionalPageLocators.BASKET)

    @allure.step('Кликнуть на элемент "Оформить заказ"')
    def click_on_button_ordering(self):
        self.click_on_element(FunctionalPageLocators.PLACE_AN_ORDER)

    @allure.step('Получить текст об успешном оформлении заказа')
    def get_ordering_popup_text(self, expected_text):
        return self.get_text_on_element(FunctionalPageLocators.PREPARES_ORDER)

    @allure.step('Кликнуть на закрытие попапа с номером заказа')
    def close_popup(self):
        self.click_on_element(OrdersFeedPageLocators.CLOSE_BUTTON)

    @allure.step('Кликнуть на элемент "Личный кабинет"')
    def click_on_order_to_account(self):
        self.click_on_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Подождать перехода на страницу профиля')
    def wait_for_entry(self):
        self.wait_for_element(PersonalAccountPageLocators.PROFILE)

    @allure.step('Кликнуть на элемент "История заказов"')
    def click_on_order_history(self):
        self.click_on_element(PersonalAccountPageLocators.CLICK_ORDER_HISTORY)

    @allure.step('Получить текст oб исходном количестве заказов')
    def get_initial_count(self, locator):
        return self.get_text_on_element(locator)

    @allure.step('Кликнуть на раздел "Конструктор"')
    def click_on_constructor(self):
        self.click_on_element(FunctionalPageLocators.CONSTRUCTOR)

    @allure.step('Получить номер заказа "В работе"')
    def get_text_order_number_in_progress(self):
        return self.get_text_on_element(OrdersFeedPageLocators.ORDER_NUMBER_IN_PROGRESS)
