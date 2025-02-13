import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.functional_page_locators import FunctionalPageLocators


class FunctionalPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть на раздел "Лента заказов"')
    def click_on_orders_feed(self):
        self.click_on_element(FunctionalPageLocators.ORDERS_FEED)

    @allure.step('Дождаться перехода в раздел "Лента заказов"')
    def wait_for_orders_feed(self):
        self.wait_for_element(FunctionalPageLocators.SECTION_ORDERS_FEED)

    @allure.step('Кликнуть на раздел "Конструктор"')
    def click_on_constructor(self):
        self.click_on_element(FunctionalPageLocators.CONSTRUCTOR)

    @allure.step('Дождаться перехода в раздел "Конструктор"')
    def wait_for_section_constructor(self):
        self.wait_for_element(FunctionalPageLocators.BUNS)

    @allure.step('Кликнуть на ингредиент')
    def click_on_ingredient(self):
        self.click_on_element(FunctionalPageLocators.INGREDIENT)

    @allure.step('Дождаться появления окна с деталями')
    def wait_for_window_with_details(self):
        self.wait_for_element(FunctionalPageLocators.DETAILS)

    @allure.step('Получить текст окна с деталями')
    def get_details_popup_text(self, expected_text):
        actual_text = self.get_text_on_element(FunctionalPageLocators.DETAILS)
        return actual_text == expected_text

    @allure.step('Нажать на крестик на окне с деталями')
    def click_on_cross_button(self):
        self.click_on_element(FunctionalPageLocators.CLOSE)

    @allure.step('Проверить невидимость окна с деталями')
    def check_popup_is_invisible(self):
        return self.check_element_is_invisible(FunctionalPageLocators.DETAILS)

    @allure.step('Добавить ингредиент в корзину')
    def drag_and_drop_ingredient(self):
        self.drag_drop(FunctionalPageLocators.INGREDIENT, FunctionalPageLocators.BASKET)



