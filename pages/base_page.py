import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Проверить наличие элемента на странице")
    def check_element_existence(self, locator):
        return bool(len(self.driver.find_elements(*locator)))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Заполнить поле ввода")
    def send_keys_to_input(self, locator, value, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(value)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.driver.find_element(*locator).text
        return element

    @allure.step("Подождать пока элемент не станет невидимым")
    def wait_for_element_hide(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Проверить, что элемент невидим")
    def check_element_is_invisible(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетащить элемент в корзину")
    def drag_drop(self, first_locator, second_locator):
        draggable = self.driver.find_element(*first_locator)
        droppable = self.driver.find_element(*second_locator)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()
