from pages.base_page import BasePage
from locators.order_settings_locators import OrderSettingsLocators
from data import *

class OrderSettings(BasePage):

    def date_deliver(self):
        self.send_keys_to_input(OrderSettingsLocators.WHEN, tomorrow)

    def time_rent(self):
        self.click_on_element(OrderSettingsLocators.TIME_RENT)
        self.click_on_element(OrderSettingsLocators.ONE_DAY)

    def click_but_order(self):
        self.click_on_element(OrderSettingsLocators.BUT_ORDER)

    def click_yes_on_popup(self):
        self.click_on_element(OrderSettingsLocators.BUT_YES)