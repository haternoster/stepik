from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class CataloguePageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GET_BASKET_AMOUNT = (By.CSS_SELECTOR, ".basket-mini")
    GET_ITEM_PRICE = (By.CSS_SELECTOR, ".price_color")