from playwright.sync_api import Page
from ui.login_page import LoginPage
from utils.builder import Builder


def test_login_with_valid_user(page: Page, login_page: LoginPage):
    user = Builder.create_user()
    login_page.load()
    login_page.login(user.username, user.password)
    assert login_page.invalid_error_message.inner_text() == "Invalid username or password"