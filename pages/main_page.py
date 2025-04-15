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

    def wait_but_sign_up(self):
        self.wait_for_element(MainLocators.BUT_SIGN_UP)

    def click_on_question(self, question_number):
        question_locator = MainLocators.question_number(question_number)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    def check_answer(self, answer_text):
        actual_text = self.get_text_on_element(MainLocators.ANSWER)
        return actual_text == answer_text
