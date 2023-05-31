import unittest
from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.file_reader import ExcelReader
from utils.mail import Email

class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')
    data = {
        "accessKey": "4Ky6AV4hE0pWLeG1bXNw",
        "type": "ZHIBO_QQ_AD",
        "appId": "audio",
        "data": {
            "text": "什么",
            "tokenId": "username69764",
            "btId": "kkk321",
            "channel": "default",
            "passThrough": {
                "comment": "123"
            }
        }
    }


    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='POST')

    def test_baidu_http(self):

        res = self.client.send(self.data)
        # assertHTTPCode(res, [1902])
        logger.debug(res.text)
        self.assertIn('"code":1100', res.text)


if __name__ == '__main__':
    report = REPORT_PATH + 'report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='接口html报告')
        runner.run(TestBaiDuHTTP('test_baidu_http'))

    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='longlisha@ishumei.com',
              server='smtp.qq.com',
              sender='1165019260@qq.com',
              password='ftumewnlwrqffhcb',
              path=report
              )
    e.send()