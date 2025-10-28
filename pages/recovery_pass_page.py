import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.recovery_pass_page_locators import PasswordPageLocators


class RecoveryPasswordPage(BasePage):
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть на элемент "Войти в аккаунт"')
    def click_on_order_to_account(self):
        self.click_on_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Подождать видимости элемента "Вход"')
    def wait_for_entry(self):
        self.wait_for_element(MainPageLocators.ORDER_TEXT)

    @allure.step('Кликнуть на "Восстановить пароль"')
    def click_on_recovery_password(self):
        self.click_on_element(PasswordPageLocators.PASSWORD_RECOVERY)

    @allure.step('Подождать видимости элемента "Восстановление пароля"')
    def wait_for_entry(self):
        self.wait_for_element(MainPageLocators.ORDER_TEXT)

    @allure.step('Заполнить поле Email')
    def send_field_email(self, email):
        self.send_keys_to_input(PasswordPageLocators.EMAIL, email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_on_button_restore(self):
        self.click_on_element(PasswordPageLocators.RESTORE)

    @allure.step('Подождать видимости элемента "Пароль"')
    def wait_for_password(self):
        self.wait_for_element(PasswordPageLocators.RECOVERY_PASSWORD)

    @allure.step('Кликнуть на кнопку "показать/скрыть пароль"')
    def click_on_button_eye(self):
        self.check_element_is_invisible(MainPageLocators.OVERLAY)
        self.click_on_element(PasswordPageLocators.EYE_BUTTON)

    @allure.step('Подождать пока поле станет активным')
    def wait_for_activate(self):
        return self.wait_for_element(PasswordPageLocators.INPUT_ACTIVE).is_displayed()
