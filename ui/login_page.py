
import allure
from playwright.sync_api import Page
from loguru import logger


class SecondTabError(Exception):
    pass


class LocatorNotFoundError(Exception):
    pass


class LoginPage:
    
    URL = "http://localhost:9999"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_button = page.locator("//input[@name='submit']")
        self.username_input = page.locator("//input[@id='username' and @required]")
        self.password_input = page.locator("//input[@id='password' and @required]")
        self.incorrect_error_message = page.locator("//div[@id='flash' and text()='Incorrect username length']")
        self.invalid_error_message = page.locator("//div[@id='flash']")
        self.block_message = page.locator("//div[@id='flash' and text()='Ваша учетная запись заблокирована']")
        self.registartion = page.locator("//a[@href='/reg']")

    def load(self) -> None:
        self.page.goto(self.URL)

    @allure.step('Авторизация')
    def login(self, username, password):
        self.username_input.click()
        self.username_input.fill(username)
        self.password_input.click()
        self.password_input.fill(password)
        self.login_button.click()
        if self.page.url == 'http://localhost:8070/welcome/':
            with allure.step(
                'Авторизация прошла успешно! Выполнен переход на главную страницу.'
            ):
                return 1
        else:
            with allure.step('Авторизация не удалась...'):
                pass
