from selenium.webdriver.common.by import By
from .base_page import BasePage
from main_page import MainPage
import pytest

def test_guest_can_go_to_login_page(browser):

    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    




