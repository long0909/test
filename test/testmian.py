import unittest
from utils.config import Config, REPORT_PATH, DATA_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email
from utils.file_reader import ExcelReader
import json

class TestBaiDuHTTP(unittest.TestCase):
    # URL = Config().get('URL')
    excel = DATA_PATH + '/case.xlsx'
    # caseid = ExcelReader(excel).data.get('id')
    # logger.debug(caseid)
    headers = {
        'Token-Id': 'admin_2651d126a178e259614a8e0f281e87ae',
    }



    def setUp(self):
        self.client = HTTPClient()
        print("start")


    def test(self):
        datas = ExcelReader(self.excel).data
        print("===========")
        for d in datas:
            with self.subTest():
                name = d.get('测试点')
                str = d.get('请求数据')
                data = json.loads(str)
                url = d.get('url')
                method = d.get('请求类型')
                code = d.get('预期结果')
                res = self.client.send(data, False, url, method, self.headers)  # assertHTTPCode(res, [1902])
                logger.debug(res.text)
                self.assertIn(code, res.text)
        print(f"用例名称：{name}")
        print("===========")
        r = res.text
        response = json.loads(r)
        print(f"返回结果：{response}")

    def tearDown(self) :
        print("end")

if __name__ == '__main__':
    report = REPORT_PATH + 'report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试报告', description='接口html报告')
        runner.run(TestBaiDuHTTP('test'))

    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='longlisha@ishumei.com',
              server='smtp.qq.com',
              sender='1165019260@qq.com',
              password='ftumewnlwrqffhcb',
              path=report
              )
    # e.send()