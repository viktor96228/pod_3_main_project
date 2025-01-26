from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class login_page(Base):

    url = 'https://just.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы(Селекторы)

    authorization = "//span[@class='bold']"
    name = "//input[@class='required'][1]"
    password = "//input[@class='required'][2]"
    enter = "//input[@class='orange-button bold']"
    main_word = "//*[text()='Здравствуйте, ']"




    # Геттеры

    def get_authorization(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.authorization)))

    def get_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Действия

    def clic_authorization(self):
        self.get_authorization().click()
        print("clic Authorization")

    def input_name(self, name):
        self.get_name().send_keys(name)
        print("input Name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input Password")

    def clic_enter(self):
        self.get_enter().click()
        print("clic Enter")

    # Методы

    def authorizations(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.clic_authorization()
            self.input_name("vievpi@mail.ru")
            self.input_password("standart@user")
            self.clic_enter()
            self.assert_word(self.get_main_word(), "Здравствуйте, vievpi@mail.ru")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")







