import pytest
from mysql.builder import MySQLBuilder
from mysql.client import MySQLClient
from ui.login_page import LoginPage
from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MySQLClient()
    yield mysql_client
    mysql_client.connection.close()

@pytest.fixture(scope='session')
def mysql_builder(mysql_client) -> MySQLBuilder:
    return MySQLBuilder(mysql_client)