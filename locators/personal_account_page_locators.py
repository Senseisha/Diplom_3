from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    PROFILE = (By.XPATH, ".//a[text()='Профиль']")
    CLICK_ORDER_HISTORY = (By.XPATH, ".//a[@href='/account/order-history']")
    ORDER_HISTORY = (By.XPATH, "[contains(@class, 'OrderHistory_orderHistory']")
    EXIT = (By.XPATH, ".//button[text()='Выход']")