from selenium.webdriver.common.by import By


class PasswordPageLocators:
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")

    PASSWORD_RECOVERY = (By.LINK_TEXT, "Восстановить пароль")
    PASSWORD_RECOVERY_TEXT = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    RESTORE = (By.XPATH, ".//button[text()='Восстановить']")
    RECOVERY_PASSWORD = (By.XPATH, ".//input[@type='password']")
    EYE_BUTTON = (By.CLASS_NAME, "input__icon-action")
    # EYE_BUTTON = (By.XPATH, ".//svg[@xmlns='http://www.w3.org/2000/svg']")
    # EYE_BUTTON = (By.CLASS_NAME, "[contains(@class, 'input__icon input__icon-action')]")
    # INPUT_ACTIVE = (By.CLASS_NAME, "[contains(@class, 'input_status_active')]")
    INPUT_ACTIVE = (By.CLASS_NAME, "input_status_active")
