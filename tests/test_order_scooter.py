from helper import generate_reg_data
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.order_settings_page import OrderSettingsPage
from data import *


class TestOrderScooter:

    def test_order_up_button(self, driver):
        name, last_name, city, number = generate_reg_data()
        test_order = MainPage(driver)
        test_order.click_but_up_order()
        test_order = OrderPage(driver)
        test_order.fill_order_form(name, last_name, city, number)
        test_order.fill_subway_station(metro)
        test_order.click_on_next()
        test_order = OrderSettingsPage(driver)
        test_order.date_deliver()
        test_order.click_active_date()
        test_order.time_rent()
        test_order.click_but_order()
        test_order.click_yes_on_popup()
        popup_text = test_order.get_text_popup_order()

        assert popup_text == popup_text_order

    def test_order_down_button(self, driver):
        name, last_name, city, number = generate_reg_data()
        test_order = MainPage(driver)
        test_order.click_but_down_order()
        test_order = OrderPage(driver)
        test_order.fill_order_form(name, last_name, city, number)
        test_order.fill_subway_station(metro)
        test_order.click_on_next()
        test_order = OrderSettingsPage(driver)
        test_order.date_deliver()
        test_order.click_active_date()
        test_order.time_rent()
        test_order.click_but_order()
        test_order.click_yes_on_popup()
        popup_text = test_order.get_text_popup_order()

        assert popup_text == popup_text_order
