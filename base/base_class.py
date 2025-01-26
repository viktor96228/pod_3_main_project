import datetime

from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver



    """Methon get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Methon assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good - " + value_word)

    """Methon Screenshot"""

    def get_scteenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'scteenshot' + now_date + '.png'
        self.driver.save_screenshot(f"./Screen/{name_screenshot}")

    """Methon assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")




