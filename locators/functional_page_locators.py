from selenium.webdriver.common.by import By


class FunctionalPageLocators:
    CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    BUNS = (By.XPATH, ".//h1[text()='Соберите бургер']")

    ORDERS_FEED = (By.XPATH, ".//p[text()='Лента Заказов']")
    SECTION_ORDERS_FEED = (By.XPATH, ".//h1[text()='Лента заказов']")

    INGREDIENT = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")
    DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    DETAILS_TEXT = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_modified')]")
    # DETAILS_TEXT = (By.XPATH, ".//div[contains(@class,'Modal_modal__container')]")

    CLOSE = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified']")
    BASKET = (By.XPATH, ".//li[contains(@class, 'BurgerConstructor_basket']")

    PLACE_AN_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
    PREPARES_ORDER = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")
