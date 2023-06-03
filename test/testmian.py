import unittest
from utils.config import Config, REPORT_PATH, DATA_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email
from utils.file_reader import ExcelReader
import json

class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/ceshi.xlsx'


    data = {
    "accessKey":"4Ky6AV4hE0pWLeG1bXNw",
    "type":"ZHIBO",
    "appId":"default",
    "data":{
        "lang":"auto",
        "channel":"SIGNATURE",
        "nickname":"羊驼驼",
        "phone":"",
        "text":"བོད་ཀྱི་སྐད་ཡིག།",
        "tokenId":"5708049"
    }
}


    def setUp(self):
        self.client = HTTPClient()

    def test_baidu_http(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                str = d.get('请求数据')
                data = json.loads(str)
                url = d.get('url')
                method = d.get('请求类型')
                code = d.get('预期结果')
                res = self.client.send(data, False, url, method)  # assertHTTPCode(res, [1902])
                logger.debug(res.text)
                self.assertIn(code, res.text)

if __name__ == '__main__':
    report = REPORT_PATH + 'report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试报告', description='接口html报告')
        runner.run(TestBaiDuHTTP('test_baidu_http'))

    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='longlisha@ishumei.com',
              server='smtp.qq.com',
              sender='1165019260@qq.com',
              password='ftumewnlwrqffhcb',
              path=report
              )
    # e.send()