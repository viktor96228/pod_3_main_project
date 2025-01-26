import action
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from utilities.logger import Logger


class Note_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    popylar = "//*[@id='by_popular']/span"
    novelty = "//*[@id='by_popular']/ul/li[4]"
    nout = "//*[@id='content']/section/div[2]/div/div[4]/div[1]/div[2]/div[2]/div[3]/a"
    lenoo = "//*[@id='content']/section/div[4]/div/div[2]/div/div[2]/div[1]/div[2]/h1"
    price_lenoo = "//*[@id='content']/section/div[4]/div/div[2]/div/div[2]/div[4]/p/span[1]"
    basket = "//*[@id='content']/section/div[4]/div/div[2]/div/div[2]/div[6]/button"


    # Getters


    def get_popylar(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.popylar)))

    def get_novelty(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.novelty)))

    def get_nout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.nout)))

    def get_lenoo(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.lenoo)))

    def get_price_lenoo(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_lenoo)))

    def get_basket(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket)))


    # Action

    def clic_popylar(self):
        self.get_popylar().click()
        print("clic Сортировать")

    def clic_novelty(self):
        self.get_novelty().click()
        print("clic Сортировать по новизне")

    def clic_nout(self):
        self.get_nout().click()
        print('Clic Ноутбук lenovo')

    def clic_basket(self):
        self.get_basket().click()
        print("clic Корзина")


    # Methods

    def select_popylar(self):
        with allure.step("Select popylar"):
            Logger.add_start_step(method="select_popylar")
            self.get_current_url()
            self.clic_popylar()
            Logger.add_end_step(url=self.driver.current_url, method="select_popylar")

    def select_novelty(self):
        with allure.step("Select novelty"):
            Logger.add_start_step(method="select_novelty")
            self.get_current_url()
            self.clic_novelty()
            Logger.add_end_step(url=self.driver.current_url, method="select_novelty")

    def select_nout(self):
        with allure.step("Select nout"):
            Logger.add_start_step(method="select_nout")
            self.clic_nout()
            self.get_current_url()
            self.assert_word(self.get_lenoo(), 'Ноутбук Lenovo IdeaPad 3 15IAU7 15.6" Intel Core i3 1215U 82RK00TQPS')
            self.assert_word(self.get_price_lenoo(), '37 440')
            Logger.add_end_step(url=self.driver.current_url, method="select_nout")

    def select_basket(self):
        with allure.step("Select basket"):
            Logger.add_start_step(method="select_basket")
            self.clic_basket()
            Logger.add_end_step(url=self.driver.current_url, method="select_basket")









