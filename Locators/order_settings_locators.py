from selenium.webdriver.common.by import By

class OrderSettingsLocators:
    WHEN = (By.XPATH, ".//input[contains(@placeholder, 'Когда')]")  # поле Когда привезти самоткат
    TIME_RENT = (By.NAME, "aria-haspopup")  # поле Срок аренды
    ONE_DAY = (By.XPATH, ".//div[@role='option' and text()='сутки']")  # Сутки в выпадающем списке срок аренды
    BUT_ORDER = (
    By.XPATH, ".//button[contains(@class, 'Middle') and (text()='Заказать')]")  # кнопка Заказать под формой
    BUT_YES = (By.XPATH, ".//button[text()='Да']")  # кнопка Да в попапе
