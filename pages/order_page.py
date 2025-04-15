from pages.base_page import BasePage
from locators.order_locators import OrderLocators


class OrderPage(BasePage):

    def fill_order_form(self, name, lastname, adress, phone):
        self.send_keys_to_input(OrderLocators.NAME, name)
        self.send_keys_to_input(OrderLocators.LAST_NAME, lastname)
        self.send_keys_to_input(OrderLocators.ADRESS, adress)
        self.send_keys_to_input(OrderLocators.PHONE, phone)

    def fill_subway_station(self, metro):
        self.click_on_element(OrderLocators.SUBWAY)
        self.send_keys_to_input(OrderLocators.SUBWAY, metro)
        self.click_on_element(OrderLocators.SUBWAY_CLICK)

    def click_on_next(self):
        self.click_on_element(OrderLocators.BUT_NEXT)
