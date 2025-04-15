from data import *
from pages.main_page import MainPage

class TestTransfer:

    def test_click_logo_scooter(self, driver):
        logo_scooter = MainPage(driver)
        logo_scooter.click_but_up_order()
        logo_scooter.click_on_logo_scooter()
        current_url = driver.current_url

        assert current_url == main_site

    def test_click_logo_yandex(self, driver):
        logo_yandex = MainPage(driver)
        logo_yandex.click_on_logo_yandex()
        driver.switch_to.window(driver.window_handles[1])
        logo_yandex.wait_but_sign_up()
        current_url = driver.current_url

        assert current_url == dzen_url
