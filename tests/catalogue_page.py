import math

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from locators import CataloguePageLocators

from .base_page import BasePage


class CatalogPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*CataloguePageLocators.ADD_BUTTON)
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_basket_amount(self):
        basket_price = self.browser.find_element(*CataloguePageLocators.GET_BASKET_AMOUNT)
        return basket_price.get_attribute('innerHTML')

    def get_item_price(self):
        item_price = self.browser.find_element(*CataloguePageLocators.GET_ITEM_PRICE)
        return item_price.get_attribute('innerHTML')






