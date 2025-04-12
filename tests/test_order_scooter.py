from pages.main_page import MainPage

class TestOrderScooter:

    def test_order_up_button(self, driver):
        test_order = MainPage(driver)
        test_order.click_but_up_order()
        test_order.