from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_locators import OrderLocators
from data import *


class OrderPage(BasePage):

    def fill_order_form(self, name, lastname, adress, phone):
        self.send_keys_to_input(OrderLocators.NAME, name)
        self.send_keys_to_input(OrderLocators.LAST_NAME, lastname)
        self.send_keys_to_input(OrderLocators.ADRESS, adress)
        self.send_keys_to_input(OrderLocators.PHONE, phone)

    def fill_subway_station(self, subway):
        self.click_on_element(OrderLocators.SUBWAY)
        self.send_keys_to_input(OrderLocators.SUBWAY, subway)
        self.click_on_element(OrderLocators.SUBWAY_CLICK)

    def click_on_next(self):
        self.click_on_element(OrderLocators.BUT_NEXT)
