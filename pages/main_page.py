import allure
from pages.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):

    @allure.step("Кликнуть на кнопку заказать вверху страницы")
    def click_but_up_order(self):
        self.click_on_element(MainLocators.BUT_ORDER_UP)

    @allure.step("Кликнуть на кнопку заказать внизу страницы")
    def click_but_down_order(self):
        self.scroll_to_element(MainLocators.BUT_ORDER_DOWN)
        self.click_on_element(MainLocators.BUT_ORDER_DOWN)

    @allure.step("Кликнуть на логотип яндекс")
    def click_on_logo_yandex(self):
        self.click_on_element(MainLocators.LOGO_YANDEX)

    @allure.step("Кликнуть на логотип самокат")
    def click_on_logo_scooter(self):
        self.click_on_element(MainLocators.LOGO_SCOOTER)

    @allure.step("Подождать видимость кнопки Войти")
    def wait_but_sign_up(self):
        self.wait_for_element(MainLocators.BUT_SIGN_UP)

    @allure.step("Кликнуть на вопрос")
    def click_on_question(self, question_number):
        question_locator = MainLocators.question_number(question_number)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Сравнить ответ на вопрос")
    def check_answer(self, answer_text):
        actual_text = self.get_text_on_element(MainLocators.ANSWER)
        return actual_text == answer_text
