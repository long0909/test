import requests
from utils.log import logger
import json
#
# METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']
#
# class UnSupportMethodException(Exception):
#     """当传入的method的参数不是支持的类型时抛出此异常。"""
#     pass

class HTTPClient:

    def __init__(self, headers=None, cookies=None):
        """headers: 字典。 例：headers={'Content_Type':'text/html'}，cookies也是字典。"""
        # self.url = url
        self.session = requests.session()
        # self.method = method.upper()
        # if self.method not in METHODS:
        #     raise UnSupportMethodException('不支持的method:{0}，请检查传入参数！'.format(self.method))

        self.set_headers(headers)
        self.set_cookies(cookies)

    def set_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, json=None, data=None, url=None, method=None):

        # logger.debug(method)
        if type(data) == str:
            data = eval(data)
        method = method.upper()
        # logger.debug(method)

        if method == 'GET':
            response = self.session.request(method=method, url=url, params=data)
        elif method == 'POST':
            if json:
                response = self.session.request(method=method, url=url, json=json)
            else:
                response = self.session.request(method=method, url=url, data=data)
        else:
            response = None

        response.encoding = 'utf-8'
        logger.debug('{0} {1}'.format(method, url))
        logger.debug('请求成功: {0}\n{1}'.format(response, response.text))
        return response