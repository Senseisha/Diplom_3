from selenium.webdriver.common.by import By


class MainPageLocators:
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_modal__P3_V5')]")
    ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    ORDER_TEXT = (By.XPATH, ".//h2[text()='Вход']")

