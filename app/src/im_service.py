from selenium import webdriver
from selenium.webdriver.common.by import By

from fastapi import HTTPException

from src.conf import config

import os
import time
import logging
import sys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
#options.add_argument("--headless")

logging.basicConfig(filename='app.log', filemode='w', format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')



class InfectionMonkeyService:
    BASE_URL = config.INFECTION_MONKEY_URL
    REGISTER_URL = BASE_URL + "/register"
    LOGIN_URL = BASE_URL + "/login"
    LANDING_PAGE_URL = BASE_URL + "/landing-page"
    CONFIG_URL = BASE_URL + "/configure"
    RUN_URL = BASE_URL + "/run-monkey"
    MAP_URL = BASE_URL + "/infection/map"
    RESTART_URL = BASE_URL + "/start-over"


    def _wait_load(self, driver):
        logging.getLogger().info("Waiting for page to load.")
        ready = False
        while (not ready):
            page_state = driver.execute_script('return document.readyState;')
            ready = (page_state == 'complete')

    def _open(self):
        logging.getLogger().info("Opening driver.")
        driver = webdriver.Remote(f"http://browser:{config.BROWSER_PORT}/wd/hub", options=options)
        driver.get(self.BASE_URL)

        if (driver.current_url == self.REGISTER_URL or driver.current_url == self.LOGIN_URL):
            self._login(driver)

        if (driver.current_url == self.LANDING_PAGE_URL):
            driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Custom')]").click()

        return driver

    def _login(self, driver):
        self._wait_load(driver)

        logging.getLogger().info("Attempting Login...")
        original_url = driver.current_url
        driver.find_element(by=By.XPATH, value="//input[@type='text']").send_keys(config.INFECTION_MONKEY_USER)
        driver.find_element(by=By.XPATH, value="//input[@type='password']").send_keys(config.INFECTION_MONKEY_PASSWORD)
        driver.find_element(by=By.TAG_NAME, value="button").click()

        while (original_url == driver.current_url):
            if (driver.find_elements(by=By.CLASS_NAME, value="alert-danger")):
                driver.quit()
                raise HTTPException(status_code=401)
            else:
                time.sleep(1)

    def _load_conf(self, driver, path):
        self._wait_load(driver)

        logging.getLogger().info(f"Loading config {path}.")
        driver.get(self.CONFIG_URL)

        file_dir = config.INFECTION_MONKEY_CONFIG + path

        if not os.path.exists(file_dir):
            driver.quit()
            raise HTTPException(status_code=404)

        driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Import config')]").click()
        driver.find_element(by=By.ID, value="importConfigFileSelector").send_keys(os.path.abspath(file_dir))
        driver.find_element(by=By.CLASS_NAME, value="btn-success").click()

    def run_island(self, path):
        with self._open() as driver:
            logging.getLogger().info("Staring Island run.")
            self._load_conf(driver, path)
            driver.get(self.RUN_URL)
            self._wait_load(driver)
            driver.find_element(by=By.XPATH, value="//*[contains(text(), 'From Island')]").click()

    def kill(self):
        with self._open() as driver:
            logging.getLogger().info("Sending kill signal to all monkeys...")
            driver.get(self.MAP_URL)
            driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Kill All Monkeys')]").click()
            driver.find_elements(by=By.CLASS_NAME, value="btn-lg")[0].click()

    def reset(self):
        with self._open() as driver:
            driver.get(self.RESTART_URL)
            driver.find_element(by=By.CLASS_NAME, value="btn-danger").click()
            driver.find_elements(by=By.CLASS_NAME, value="btn-lg")[1].click()

                