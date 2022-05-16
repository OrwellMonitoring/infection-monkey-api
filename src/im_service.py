from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from fastapi import HTTPException

from conf import config

import os


driver_options = Options()
#driver_options.add_argument("--headless")

class InfectionMonkeyService:
    BASE_URL = config.INFECTION_MONKEY_URL
    REGISTER_URL = BASE_URL + "/register"
    LOGIN_URL = BASE_URL + "/login"
    LANDING_PAGE_URL = BASE_URL + "/landing-page"
    CONFIG_URL = BASE_URL + "/configure"
    RUN_URL = BASE_URL + "/run-monkey"
    MAP_URL = BASE_URL + "/infection/map"
    RESTART_URL = BASE_URL + "/start-over"

    def _open(self):
        driver = webdriver.Firefox(options=driver_options)
        driver.accept_untrusted_certs = True
        driver.get(self.BASE_URL)
        page = driver.find_element(by=By.TAG_NAME, value="h1")

        if (driver.current_url == self.REGISTER_URL or driver.current_url == self.LOGIN_URL):
            self._login(driver)

        return driver

    def _login(self, driver):
        original_url = driver.current_url
        driver.find_element(by=By.XPATH, value="//input[@type='text']").send_keys(config.INFECTION_MONKEY_USER)
        driver.find_element(by=By.XPATH, value="//input[@type='password']").send_keys(config.INFECTION_MONKEY_PASSWORD)
        driver.find_element(by=By.TAG_NAME, value="button").click()

    def _load_conf(self, driver, path):
        driver.get(CONFIG_URL)
        driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Import config')]").click()
        driver.find_element(by=By.ID, value="importConfigFileSelector").send_keys(os.getcwd()+config.INFECTION_MONKEY_CONFIG)

        try:
            driver.find_element(by=By.CLASS_NAME, value="alert-success")
        except:
            raise HTTPException(status_code=400)


    def run_island(self):
        with self._open() as driver:
            driver.get(self.RUN_URL)
            driver.find_element(by=By.XPATH, value="//*[contains(text(), 'From Island')]").click()

    def kill(self):
        with self._open() as driver:
            driver.get(MAP_URL)
            driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Kill All Monkeys')]").click()
                

im = InfectionMonkeyService()
im.run_island()