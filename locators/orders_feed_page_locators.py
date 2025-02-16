from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:
    ORDER = (By.XPATH, ".//a[starts-with(@class, 'OrderHistory_link')]")
    DETAILS_POPUP = (By.XPATH, ".//p[text()='Cостав']")
    CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER_TEXT = (By.XPATH, ".//h2[starts-with(@class, 'Modal_modal__title_')]")
    ALL_TIME_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following::p")
    TODAY_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following::p")
    ORDER_HISTORY_LIST = (By.XPATH, ".//div[starts-with(@class, 'OrderHistory_orderHistory__')]")
    ORDER_FEED_LIST = (By.XPATH, ".//ul[starts-with(@class, 'OrderFeed_list__')]")


