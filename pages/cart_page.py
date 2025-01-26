from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators



    shopping = "//*[@id='body']/header/div[1]/section/div[3]/div[2]/div/button"
    lenovo_nout = "//*[@id='content']/section[1]/div[3]/div/ul/li/div[3]/a"
    cart_lenovo = "//*[@id='content']/section/div[4]/div/div[2]/div/div[2]/div[1]/div[2]/h1"
    cart_price_lenovo = "//*[@id='content']/section/div[4]/div/div[2]/div/div[2]/div[4]/p/span[1]"
    alread_shopping = "//*[@id='content']/section/div[4]/div/div[2]/div/div[2]/div[6]/button"
    empty_shopping = "//*[@id='body']/header/div[1]/section/div[3]/div[2]/div/div[2]/a"


 #Getters


    def get_shopping(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.shopping)))

    def get_lenovo_nout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.lenovo_nout)))

    def get_cart_lenovo(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_lenovo)))

    def get_cart_price_lenovo(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_price_lenovo)))

    def get_alread_shopping(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.alread_shopping)))

    def get_empty_shopping(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.empty_shopping)))



    # Action


    def clic_shopping(self):
        self.get_shopping().click()
        print("clic Перейти в корзину")

    def clic_lenovo_nout(self):
        self.get_lenovo_nout().click()
        print("clic Ноутбук в корзине")

    def clic_alread_shopping(self):
        self.get_alread_shopping().click()
        print("clic уже в корзине")

    def clic_empty_shopping(self):
        self.get_empty_shopping().click()
        print("clic очистить корзину")


    #Methods



    def shopping_cart(self):
        with allure.step("Shopping cart"):
            Logger.add_start_step(method="shopping_cart")
            self.clic_shopping()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="shopping_cart")

    def lenovo_nout_cart(self):
        with allure.step("Lenovo nout cart"):
            Logger.add_start_step(method="lenovo_nout_cart")
            self.clic_lenovo_nout()
            self.get_current_url()
            self.assert_word(self.get_cart_lenovo(), 'Ноутбук Lenovo IdeaPad 3 15IAU7 15.6" Intel Core i3 1215U 82RK00TQPS')
            self.assert_word(self.get_cart_price_lenovo(), '37 440')
            Logger.add_end_step(url=self.driver.current_url, method="lenovo_nout_cart")

    def alread_shopping_cart(self):
        with allure.step("Alread shopping"):
            Logger.add_start_step(method="alread_shopping_cart")
            self.clic_alread_shopping()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="alread_shopping_cart")

    def empty_shopping_cart(self):
        with allure.step("Empty shopping"):
            Logger.add_start_step(method="empty_shopping_cart")
            self.clic_empty_shopping()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="empty_shopping_cart")




