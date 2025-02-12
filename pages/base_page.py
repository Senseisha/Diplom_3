import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # @allure.step("Скролл до элемента")
    # def scroll_to_element(self, locator):
    #     element = self.wait_for_element(locator, global_timeout)
    #     self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Заполнить поле ввода")
    def send_keys_to_input(self, locator, value, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(value)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать пока элемент не станет видимым")
    def wait_for_element_hide(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетащить элемент в корзину")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

