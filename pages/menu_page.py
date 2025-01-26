import action
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from utilities.logger import Logger


class Menu_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    menu = "//*[@id='body']/header/div[3]/section/div[1]/p" # Каталог
    menu_1 = "//*[@id='main-menu-dest']/li[2]/a" # Каталог Компьютеры и софт
    con_sec = "//*[@id='content']/section/h1" # Компьютеры и софт
    menu_2 = "//*[@id='content']/section/div[1]/ul/li[3]/a" # Каталог ноутбуки
    laptop = "//*[@id='content']/section/h1" # Ноутбуки
    price_range = "//a[@class='catalog-filters-title haschild open']" #Диапазон цен
    min_price = "//*[@id='i_from']"  # минимальная цена
    max_price = "//*[@id='i_to']"  # максимальная цена
    menu_3 = "//*[@id='content']/section/div[2]/div/div[1]/div[1]/a" # каталог ноутбуки Lenovo
    noun_len = "//*[@id='content']/section/h1" # Ноутбуки Lenovo
    # screen_diagonal = "//a[@class='catalog-filters-title haschild open']" # Диагональ экрана
    # screen = "//label[@for='chk-feature-1423-3086']"


    # Getters

    def get_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_menu_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_1)))

    def get_con_sec(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.con_sec)))

    def get_menu_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_2)))

    def get_laptop(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop)))

    def get_menu_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_3)))

    def get_noun_len(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.noun_len)))

    def get_price_range(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_range)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))




    # Action


    def clic_menu(self):
        self.get_menu().click()
        print("clic Каталог")

    def clic_menu_1(self):
        self.get_menu_1().click()
        print("clic Компьютеры и софт")

    def clic_menu_2(self):
        self.get_menu_2().click()
        print("clic Ноутбуки")

    def clic_menu_3(self):
        self.get_menu_3().click()
        print("clic Lenovo")

    def input_min_price(self, min_price):
        self.get_min_price().click()
        self.get_min_price().send_keys(Keys.CONTROL + "a")
        self.get_min_price().send_keys(Keys.DELETE)
        self.get_min_price().send_keys(min_price)
        print(f"Ввод: {min_price}")

    def input_max_price(self, max_price):
        self.get_max_price().click()
        self.get_max_price().send_keys(Keys.CONTROL + "a")
        self.get_max_price().send_keys(Keys.DELETE)
        self.get_max_price().send_keys(max_price)
        print(f"Ввод: {max_price}")

    # def clic_screen_1(self):
    #     self.get_screen_1().click()
    #     print("clic screen 13,3")




    # Methods

    def select_menu(self):
        with allure.step("Select menu"):
            Logger.add_start_step(method="select_menu")
            self.get_current_url()
            self.clic_menu()
            Logger.add_end_step(url=self.driver.current_url, method="select_menu")

    def select_menu_1(self):
        with allure.step("Select menu 1"):
            Logger.add_start_step(method="select_menu_1")
            self.get_current_url()
            self.clic_menu_1()
            self.assert_word(self.get_con_sec(),'Компьютеры и софт')
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_1")

    def select_menu_2(self):
        with allure.step("Select menu 2"):
            Logger.add_start_step(method="select_menu_2")
            self.get_current_url()
            self.clic_menu_2()
            self.assert_word(self.get_laptop(), 'Ноутбуки')
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_2")


    def select_menu_3(self):
        with allure.step("Select menu 3"):
            Logger.add_start_step(method="select_menu_3")
            self.clic_menu_3()
            self.assert_word(self.get_noun_len(), "Ноутбуки Lenovo")
            self.assert_word(self.get_price_range(), 'Диапазон цен')
            self.input_min_price("30000")
            self.input_max_price("400000")
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_3")


















