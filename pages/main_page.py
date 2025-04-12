from pages.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):

    def click_but_up_order(self):
        self.click_on_element(MainLocators.BUT_ORDER_UP)

    def click_but_down_order(self):
        self.scroll_to_element(MainLocators.BUT_ORDER_DOWN)
        self.click_on_element(MainLocators.BUT_ORDER_DOWN)

    def click_on_logo_yandex(self):
        self.click_on_element(MainLocators.LOGO_YANDEX)

    def click_on_logo_scooter(self):
        self.click_on_element(MainLocators.LOGO_SCOOTER)

    def check_text_answer(self):
        self.
