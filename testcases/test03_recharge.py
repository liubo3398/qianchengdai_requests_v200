"""充值接口"""

import unittest
import requests
import os
from jsonpath import jsonpath
from unittestreport import ddt,list_data
from common.handle_conf import d1
from common.handle_excel import HandleExcel
from common.handle_path import DATAS_PATH
from common.handle_log import my_log
from common.handle_mysql import HandleDB
from common.tools import replace_data
from testcases.fixture import BaseTest


@ddt
class TestCharge(unittest.TestCase, BaseTest):
    # 导入excel测试数据
    read = HandleExcel(os.path.join(DATAS_PATH, 'data.xlsx'), 'recharge')
    cases = read.read_excel()
    # 实例化操作数据库的方法
    db = HandleDB()

    @classmethod
    def setUpClass(cls):
        # 登录接口，获取token
        cls.login_admin()

    @list_data(cases)
    def test_01(self, item):
        # 准备数据
        method = item['method']
        url = d1.get('url', 'base_url')+item['url']

        # 动态变更参数,字符串替换参数
        # params = eval(item['data'].replace('#member_id#', self.member_id))
        params = eval(replace_data(item['data'], TestCharge))

        headers = self.headers
        expected = eval(item['expected'])

        # ------------------数据库获取充值前的金额---------------------------
        sql = f'select leave_amount from futureloan.member where mobile_phone={d1.get("login", "mobile_phone")};'
        exc_sql = self.db.find_one(sql)[0]

        # 获取实际结果
        res = requests.request(method=method, url=url, json=params, headers=headers)
        print('预期结果：', expected)
        print('实际结果：', res.json())
        # ------------------数据库获取充值后的金额---------------------------
        res_sql = self.db.find_one(sql)[0]
        print('充值前金额：', exc_sql)
        print('充值后金额：', res_sql)

        # 断言
        try:
            self.assertEqual(expected['code'], res.json()['code'])
            self.assertEqual(expected['msg'], res.json()['msg'])
            # ------------------断言数据库充值金额------------------
            if item['check_sql'] == 1:
                self.assertEqual(float(params['amount']), float(res_sql)-float(exc_sql))

        except AssertionError as e:
            my_log.error(f'用例执行--{item["title"]}--失败')
            raise e
        else:
            my_log.info(f'用例执行--{item["title"]}--成功')
