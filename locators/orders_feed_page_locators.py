from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:
    ORDER = (By.XPATH, ".//a[starts-with(@class, 'OrderHistory_link')]")
    DETAILS_POPUP = (By.XPATH, ".//p[text()='Cостав']")
    CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")

    ALL_TIME_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']")
    TODAY_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']")

    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[starts-with(@class, 'OrderFeed_orderListReady')]")

