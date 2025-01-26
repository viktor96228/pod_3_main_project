from base.base_class import Base
from utilities.logger import Logger
import allure

class Finish_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators



    #Getters


    # Action


    #Methods

    def finish(self):
        with allure.step("Select finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.assert_url('https://just.ru/catalog/')
            self.get_scteenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")
