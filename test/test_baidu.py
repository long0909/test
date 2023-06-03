import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utils.config import Config, DATA_PATH, DRIVER_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.log import logger
from utils.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, 'APjFqb')
    locator_result = (By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']")

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_kw).send_keys(Keys.ENTER)
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + 'case.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestBaiDu('test_search'))
        e = Email(title='百度搜索测试报告',
                  message='这是今天的测试报告，请查收！',
                  receiver='longlisha@ishumei.com',
                  server='smtp.qq.com',
                  sender='1165019260@qq.com',
                  password='ftumewnlwrqffhcb',
                  path=report
                  )
        e.send()