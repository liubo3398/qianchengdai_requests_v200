"""
投资接口

前置条件：
    1.登录接口获取token；（类前置）
    2.新增并审核项目才能投资（方法前置）

难点：
    1.测试数据中需要审核失败的项目怎么做？
        a.可以在类前置中获取一个审核失败的loan_id;
        b.在方法前置审核项目时判断一下测试数据中的某个字段，然后去审核成功或者失败；

"""
import unittest
import os
import requests
from jsonpath import jsonpath
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATAS_PATH
from common.handle_conf import d1
from common.handle_log import my_log
from common.tools import replace_data
from testcases.fixture import BaseTest



@ddt
class TestInvest(unittest.TestCase, BaseTest):
    # 读取测试数据
    read = HandleExcel(os.path.join(DATAS_PATH, 'data.xlsx'), 'invest')
    cases = read.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        # 登录接口获取token（类前置）
        cls.login_admin()

    def setUp(self) -> None:
        # 新增并审核项目才能投资（方法前置）
        # 新增项目
        self.add_project()
        # 审核项目
        self.audit_project()

    @list_data(cases)
    def test_01(self, item):
        # 准备数据
        method = item['method']
        url = d1.get('url', 'base_url')+item['url']
        params = eval(replace_data(item['data'], TestInvest))
        expected = eval(item['expected'])

        # 发送请求，获取实际结果
        res = requests.request(method=method, url=url, json=params, headers=self.headers)

        # 断言
        try:
            self.assertEqual(expected['code'], res.json()['code'])
            self.assertEqual(expected['msg'], res.json()['msg'])
        except AssertionError as e:
            my_log.error(f'用例执行--{item["title"]}--失败')
            raise e
        else:
            my_log.info(f'用例执行--{item["title"]}--成功')

