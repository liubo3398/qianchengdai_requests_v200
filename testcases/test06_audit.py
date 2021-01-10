"""项目审核接口"""
import unittest
import requests
import os
from jsonpath import jsonpath
from unittestreport import ddt, list_data
from common.handle_conf import d1
from common.handle_excel import HandleExcel
from common.handle_path import DATAS_PATH
from common.handle_log import my_log
from common.handle_mysql import HandleDB
from common.tools import replace_data
from testcases.fixture import BaseTest


@ddt
class TestAudit(unittest.TestCase, BaseTest):
    # 导入excel测试数据
    read = HandleExcel(os.path.join(DATAS_PATH, 'data.xlsx'), 'audit')
    cases = read.read_excel()
    # 实例化操作数据库的方法
    db = HandleDB()

    @classmethod
    def setUpClass(cls):
        # 管理员登录接口，获取token
        cls.login_admin()

    def setUp(self):
        # 每次审核前都得新建一哥项目
        # 新增项目接口，获取loan_id
        self.add_project()

    @list_data(cases)
    def test_01(self, item):
        # 准备数据
        method = item['method']
        url = d1.get('url', 'base_url')+item['url']

        # 动态变更参数,字符串替换参数
        params = eval(replace_data(item['data'], TestAudit))

        headers = self.headers
        expected = eval(item['expected'])

        # 获取实际结果
        res = requests.request(method=method, url=url, json=params, headers=headers)
        print('预期结果：', expected)
        print('实际结果：', res.json())

        # 断言
        try:
            self.assertEqual(expected['code'], res.json()['code'])
            self.assertEqual(expected['msg'], res.json()['msg'])

        except AssertionError as e:
            my_log.error(f'用例执行--{item["title"]}--失败')
            raise e
        else:
            my_log.info(f'用例执行--{item["title"]}--成功')

