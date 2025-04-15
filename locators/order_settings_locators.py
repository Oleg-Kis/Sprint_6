from selenium.webdriver.common.by import By

class OrderSettingsLocators:
    WHEN = (By.XPATH, ".//input[contains(@placeholder, 'Когда')]")  # поле Когда привезти самоткат
    TIME_RENT = (By.CLASS_NAME, "Dropdown-root")  # поле Срок аренды
    ONE_DAY = (By.XPATH, ".//div[@role='option' and text()='сутки']")  # Сутки в выпадающем списке срок аренды
    BUT_ORDER = (By.XPATH, ".//button[contains(@class, 'Middle') and (text()='Заказать')]")  # кнопка Заказать под формой
    BUT_YES = (By.XPATH, ".//button[text()='Да']")  # кнопка Да в попапе
    DATE_ACTIV = (By.XPATH, ".//div[contains(@class,'day--selected')]") #активная дата в выпадающем списке
    TEXT_POPUP_ORDER = (By.XPATH, ".//button[text()='Посмотреть статус']") #кнопка Посмотреть статус на попапе оформленного заказа
