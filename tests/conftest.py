import pytest
import requests
from selenium import webdriver
from curl import *
from pages.recovery_pass_page import RecoveryPasswordPage
from pages.personal_account_page import PersonalAccount
from pages.functional_page import FunctionalPage
from generator import register_new_user


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


# Фикстура создания пользователя через API
@pytest.fixture()
def create_and_delete_user(generate_users_data):
    email = generate_users_data['email']
    password = generate_users_data['password']
    response = requests.post(f'{UrlForCreate.BASE_URL}{UrlForCreate.CREATE_URL}', data=generate_users_data)
    access_token = response.json().get('accessToken')
    yield [email, password]
    requests.delete(f'{UrlForCreate.BASE_URL}{UrlForCreate.DELETE_URL}', headers={
        "Authorization": access_token})


# Фикстура перехода в личный кабинет
@pytest.fixture
def transition_to_personal_account(driver):
    driver = PersonalAccount(driver)
    driver.main_page_loading_wait()
    driver.click_on_order_to_account()
    return driver


# Фикстура логина пользователя
@pytest.fixture
def login_user(driver, create_and_delete_user, transition_to_personal_account):
    email = create_and_delete_user[0]
    password = create_and_delete_user[1]
    login = PersonalAccount(driver)
    login.send_email(email)
    login.send_password(password)
    login.click_on_enter()
    login.main_page_loading_wait()
    return login


# Фикстура для проверки функционала (окно с деталями)
@pytest.fixture
def popup_with_details(driver):
    driver = FunctionalPage(driver)
    driver.main_page_loading_wait()
    driver.click_on_ingredient()
    driver.wait_for_window_with_details()
    return driver


@pytest.fixture
def generate_users_data():
    create_users_body = register_new_user()
    return create_users_body
