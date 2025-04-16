import allure
from pages.base_page import BasePage
from locators.order_settings_locators import OrderSettingsLocators
from data import *

class OrderSettingsPage(BasePage):

    @allure.step("Ввести дату")
    def date_deliver(self):
        self.send_keys_to_input(OrderSettingsLocators.WHEN, tomorrow)

    @allure.step("Указать время аренды")
    def time_rent(self):
        self.click_on_element(OrderSettingsLocators.TIME_RENT)
        self.click_on_element(OrderSettingsLocators.ONE_DAY)

    @allure.step("Кликнуть на кнопку Заказать")
    def click_but_order(self):
        self.click_on_element(OrderSettingsLocators.BUT_ORDER)

    @allure.step("Кликнуть на кнопку Да в попапе")
    def click_yes_on_popup(self):
        self.click_on_element(OrderSettingsLocators.BUT_YES)

    @allure.step("Кликнуть на активную дату в выпадающем списке")
    def click_active_date(self):
        self.click_on_element(OrderSettingsLocators.DATE_ACTIV)

    @allure.step("Получить текст в попапе")
    def get_text_popup_order(self):
        return self.get_text_on_element(OrderSettingsLocators.TEXT_POPUP_ORDER)
