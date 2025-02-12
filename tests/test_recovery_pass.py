import allure
from curl import *
from data import Credentials
from pages.recovery_pass_page import RecoveryPasswordPage


class TestRecoveryPassword:
    @allure.title('Тест успешного перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_success_entry_with_button_recover_password(self, driver, recovery_password):
        assert driver.current_url == forgot_pass

    @allure.title('Тест успешного ввода почты и клика по кнопке "Восстановить"')
    def test_success_send_email(self, driver, recovery_password):
        recovery = RecoveryPasswordPage(driver)
        recovery.send_field_email(Credentials.email)
        recovery.click_on_button_restore()
        recovery.wait_for_password()
        assert driver.current_url == reset_password

    @allure.title('Тест успешной активации поля с паролем кликом по кнопке показать/скрыть пароль')
    def test_activate_field(self, driver, recovery_password):
        activate_field = RecoveryPasswordPage(driver)
        activate_field.send_field_email(Credentials.email)
        activate_field.click_on_button_restore()
        activate_field.wait_for_password()
        activate_field.click_on_button_eye()
        assert activate_field.wait_for_activate is True
