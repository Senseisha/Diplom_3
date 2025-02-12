main_site = 'https://stellarburgers.nomoreparties.site'
auth_endpoint = f'{main_site}/login'
forgot_pass = f'{main_site}/forgot-password'
reset_password = f'{main_site}/reset-password'
profile_endpoint = f'{main_site}/account/profile'
order_history = f'{main_site}/order-history'
feed_orders = f'{main_site}/feed'


class UrlForCreateAndLogin:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    CREATE_URL = 'api/auth/register'
    LOGIN_URL = 'api/auth/login'
    DELETE_URL = 'api/auth/user'
