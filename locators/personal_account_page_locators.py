from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    ENTER = (By.XPATH, ".//button[text()='Войти']")
    PROFILE = (By.XPATH, ".//a[text()='Профиль']")
    CLICK_ORDER_HISTORY = (By.LINK_TEXT, 'История заказов')
    ORDER_HISTORY = (By.XPATH, ".//a[contains(@class, 'Account_link_active')]")
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")
