import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from utils.config import Config
from utils.log import logger


class TestBaiDui(unittest.TestCase):
    URL = Config().get('URL')

    locator_kw = (By.ID, 'APjFqb')
    locator_result = (By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium 灰蓝')
        self.driver.find_element(*self.locator_kw).send_keys(Keys.ENTER)
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('python')
        self.driver.find_element(*self.locator_kw).send_keys(Keys.ENTER)
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)


if __name__ == '__main__':
    unittest.main()
