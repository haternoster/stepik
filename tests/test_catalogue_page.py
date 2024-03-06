import time
from .catalogue_page import CatalogPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = CatalogPage(browser, link)
    page.open()
    item_price = page.get_item_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    basket_sum = page.get_basket_amount()
    assert item_price in basket_sum, "Стоимость корзины не совпадает с ценой товара"
