import time
import allure
from unittest import result

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.finish_page import Finish_page
from pages.login_page import login_page
from pages.menu_page import Menu_page
from pages.note_page import Note_page



@allure.description("Test product")
def test_product(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Старт тест Авторизации")
    login = login_page(driver)
    login.authorizations()
    print("Финиш тест Авторизации")
    time.sleep(10)
    print("Старт тест Каталог")
    mp = Menu_page(driver)
    mp.select_menu()
    mp.select_menu_1()
    mp.select_menu_2()
    mp.select_menu_3()
    # mp.clic_screen_1()
    print("Финиш тест Каталог")
    time.sleep(3)
    print("Старт тест выбор прдукта")
    np = Note_page(driver)
    np.select_popylar()
    np.select_novelty()
    np.select_nout()
    np.select_basket()
    print("Финиш тест выбор продукта")

    time.sleep(5)
    print("тест Корзина")

    cp = Cart_page(driver)
    cp.shopping_cart()
    cp.lenovo_nout_cart()
    cp.alread_shopping_cart()
    cp.empty_shopping_cart()
    print("Финиш")

    f = Finish_page(driver)
    f.finish()

    # assert Cart_page.get_cart_lenovo(self) == Note_page.get_lenoo(self)
    # assert Cart_page.get_cart_price_lenovo(self) == Note_page.get_price_lenoo(self)



    time.sleep(10)
    driver.quit()



