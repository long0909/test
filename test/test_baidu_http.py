import unittest
from utils.config import Config, REPORT_PATH, DATA_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
from data.get_data import GetData
from utils.mail import Email


class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/case.xlsx'
    json = DATA_PATH + '/ep.json'


    def setUp(self):
        self.client = HTTPClient()
        self.data = GetData()


    def test_baidu_http(self):
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            with self.subTest(i=i):
                data = self.data.get_request_data(i)
                logger.debug(data)
                res = self.client.send(data)  # assertHTTPCode(res, [1902])
                logger.debug(res.text)
                self.assertIn('"code":1100', res.text)

if __name__ == '__main__':
    report = REPORT_PATH + 'report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='接口html报告')
        runner.run(TestBaiDuHTTP('test_baidu_http'))

    e = Email(title='测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='longlisha@ishumei.com',
              server='smtp.qq.com',
              sender='1165019260@qq.com',
              password='ftumewnlwrqffhcb',
              path=report
              )
    # e.send()