from selenium.webdriver.common.by import By


class FunctionalPageLocators:
    CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    BUNS = (By.XPATH, ".//h1[text()='Соберите бургер']")

    ORDERS_FEED = (By.XPATH, ".//p[text()='Лента Заказов']")
    SECTION_ORDERS_FEED = (By.XPATH, ".//h1[text()='Лента заказов']")

    INGREDIENT = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")
    DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    CLOSE = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified')]")
    # OPEN_POPUP = (By.XPATH, ".//section[starts-with(@class, 'Modal_modal_opened')]")

    BASKET = (By.XPATH, ".//li[contains(@class, 'BurgerConstructor_basket']")

    PLACE_AN_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
    PREPARES_ORDER = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")
