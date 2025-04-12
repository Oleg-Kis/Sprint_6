from selenium.webdriver.common.by import By

class MainLocators:
    BUT_ORDER_UP = (By.CLASS_NAME, "Button_Button__ra12g")  # кнопка Заказать в шапке
    BUT_ORDER_DOWN = (By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM')]")  # кнопка Заказать в футере
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # логотип Самокат
    LOGO_YANDEX = (By.XPATH, ".//a[@rel='noopener noreferrer']")  # логотип Яндекс
