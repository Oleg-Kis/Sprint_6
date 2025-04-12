from selenium.webdriver.common.by import By

class OrderLocators:
    NAME = (By.XPATH, ".//input[@placeholder='* Имя']") #поле Имя
    LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']") #поле Фамилия
    ADRESS = (By.XPATH, ".//input[contains(@placeholder, 'Адрес')]") #поле Адрес
    SUBWAY = (By.XPATH, ".//input[@placeholder='* Станция метро']") #поле Метро
    PHONE = (By.XPATH, ".//input[contains(@placeholder, 'Телефон')]") #поле Телефон
    BUT_NEXT = (By.XPATH, ".//button[text()='Далее']") #кнопка Далее