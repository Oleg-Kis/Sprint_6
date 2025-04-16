import allure
from data import *
from pages.main_page import MainPage

class TestTransfer:

    @allure.title("Переход на сгавную страницу по клику лого самокат")
    def test_click_logo_scooter(self, driver):
        logo_scooter = MainPage(driver)
        logo_scooter.click_but_up_order()
        logo_scooter.click_on_logo_scooter()
        current_url = logo_scooter.get_url()

        assert current_url == main_site

    @allure.title("Переход на сайт Дзен по клику лого Яндекс")
    def test_click_logo_yandex(self, driver):
        logo_yandex = MainPage(driver)
        logo_yandex.click_on_logo_yandex()
        logo_yandex.switch_to_window()
        logo_yandex.wait_but_sign_up()
        current_url = logo_yandex.get_url()

        assert current_url == dzen_url
