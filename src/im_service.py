from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from conf import config

driver_options = Options()
driver_options.add_argument("--headless")

class InfectionMonkeyService:
    BASE_URL = config.INFECTION_MONKEY_URL
    REGISTER_URL = BASE_URL + "/register"
    LOGIN_URL = BASE_URL + ""

    def open(self):
        return webdriver.Firefox(options=driver_options)

    def register(self, username, password):
        with self.open() as driver:
            print(config.INFECTION_MONKEY_URL)

            driver.get(self.REGISTER_URL)

    def user_state(self):
        with self.open() as driver:
            driver.get(self.BASE_URL)
            page = driver.find_element(by=By.TAG_NAME, value="h1")
            
            if page.text == "Login":
                

im = InfectionMonkeyService()
im.user_state()