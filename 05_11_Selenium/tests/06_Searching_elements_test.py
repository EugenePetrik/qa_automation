from locators.header import Header
from locators.user_page import UserPage
from locators.user_login import UserLogin
from locators.breadcrumbs import BreadCrumbs
import yaml

conf = yaml.safe_load(open('configuration.yml'))

email = conf['user']['email']
password = conf['user']['password']


def test_login_user(browser):
    """
    Проверка авторизации пользователя в личный кабинет и выхода из него
    :param browser:
    """

    # Открывам главную страницу:
    browser.open_main_page()

    # Выбираем аккаунт и нажимаем войти:
    browser.wd.find_element(*UserPage.my_account).click()
    browser.wd.find_element(*UserPage.log_in).click()

    # Очищаем поля и вводим данные для авторизации:
    browser.wd.find_element(*UserLogin.email).clear()
    browser.wd.find_element(*UserLogin.email).send_keys(email)
    browser.wd.find_element(*UserLogin.password).clear()
    browser.wd.find_element(*UserLogin.password).send_keys(password)

    # Нажимаем кнопку Login для входа в аккаунт:
    browser.wd.find_element(*UserLogin.login_button).click()

    # Собираем хлебные крошки после Login:
    account_breadcrumb = browser.wd.find_element(
        *BreadCrumbs.account_breadcrumb
    ).text

    # Нажимаем кнопку Logout для выхода из аккаунта:
    browser.wd.find_element(*UserPage.log_out).click()

    # Собираем хлебные крошки после Logout:
    logout_breadcrumb = browser.wd.find_element(
        *BreadCrumbs.logout_breadcrumb
    ).text

    # Подтвержаем выход из аккаунта:
    browser.wd.find_element(*UserPage.continue_button).click()

    # Проверяем хлебные крошки:
    assert logout_breadcrumb == 'Logout'
    assert account_breadcrumb == 'Account'


def test_change_currency(browser):
    """
    Проверка смены валют в Header'е
    :param browser:
    """

    # Открывам главную страницу:
    browser.open_main_page()

    # Нажимаем на кнопку смены валюты и выбираем dollar:
    browser.wd.find_element(*Header.currency_button).click()
    browser.wd.find_element(*Header.currency_dollar).click()
    dollar = browser.wd.find_element(*Header.current_currency).text

    # Нажимаем на кнопку смены валюты и выбираем pounds:
    browser.wd.find_element(*Header.currency_button).click()
    browser.wd.find_element(*Header.currency_pound).click()
    pounds = browser.wd.find_element(*Header.current_currency).text

    # Нажимаем на кнопку смены валюты и выбираем euro:
    browser.wd.find_element(*Header.currency_button).click()
    browser.wd.find_element(*Header.currency_euro).click()
    euro = browser.wd.find_element(*Header.current_currency).text

    # Проверяем, что была выбрана правильная валюта:
    assert dollar == '$' and pounds == '£' and euro == '€'
