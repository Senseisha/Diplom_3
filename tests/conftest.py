import pytest
import requests
from selenium import webdriver
from curl import *
from data import Credentials
from pages.recovery_pass_page import RecoveryPasswordPage
from pages.personal_account_page import PersonalAccount
from pages.functional_page import FunctionalPage
from generator import register_new_user

# @pytest.fixture(params=["chrome"])
# @pytest.fixture(params=["firefox"])
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    yield driver
    driver.quit()


# Фикстура перехода на страницу восстановления пароля по кнопке "Восстановить пароль"
@pytest.fixture
def recovery_password(driver):
    driver = RecoveryPasswordPage(driver)
    driver.main_page_loading_wait()
    driver.click_on_order_to_account()
    driver.wait_for_entry()
    driver.click_on_recovery_password()
    return driver


# Фикстура ввода почты и клика по кнопке "Восстановить"
@pytest.fixture
def filling_email_field(recovery_password):
    email_field = RecoveryPasswordPage(driver)
    email_field.send_field_email(Credentials.email)
    email_field.click_on_button_restore()
    email_field.wait_for_password()


@pytest.fixture
def transition_to_personal_account(driver):
    driver = PersonalAccount(driver)
    driver.main_page_loading_wait()
    driver.click_on_order_to_account()
    # driver.wait_for_entry()
    return driver


# Фикстура для проверки функционала (окно с деталями)
@pytest.fixture
def popup_with_details(driver):
    driver = FunctionalPage(driver)
    driver.main_page_loading_wait()
    driver.click_on_ingredient()
    driver.wait_for_window_with_details()
    return driver


"Фикстура с добавлением ингредиентов в корзину"


# @pytest.fixture(driver)
# def drag_drop(self):
#     self.main_page_loading_wait()
#     ingredient = self.find_element_with_wait(locator = ing_locator)
#     basket = self.find_element_with_wait(locator = basket_locator)
#     self.drag_and_dropElement(sourse = ingredient, target = basket)

@pytest.fixture
def generate_users_data():
    create_users_body = register_new_user()
    return create_users_body


@pytest.fixture()
def create_login_delete_user(generate_users_data):
    email = generate_users_data['email']
    password = generate_users_data['password']
    response = requests.post(f'{UrlForCreateAndLogin.BASE_URL}{UrlForCreateAndLogin.CREATE_URL}', data=body)
    # UserMethods().create_user(generate_users_data)
    user_login = requests.post(f'{UrlForCreateAndLogin.BASE_URL}{UrlForCreateAndLogin.LOGIN_URL}', data=payload)
    # user_login = UserMethods().login_user(email, password)
    user_token = user_login.json().get('accessToken')
    yield [user_login, user_token]

    delete_user = requests.delete(f'{UrlForCreateAndLogin.BASE_URL}{UrlForCreateAndLogin.DELETE_URL}', headers={
        "Authorization": access_token})
    # UserMethods().delete_user(user_token)


@pytest.fixture
def revert_user():
    credentials = {
        'email': Credentials.email,
        'password': Credentials.password
    }

    response = requests.post(auth_endpoint, json=credentials)
    token = response.json().get('token')

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    update_data = {
        'user': default_user_url
    }
    requests.patch(user_update_endpoint, json=update_data, headers=headers)
    yield
