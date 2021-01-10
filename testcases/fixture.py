"""
用例前置的封装
"""
import requests
from jsonpath import jsonpath
from common.handle_conf import d1


class BaseTest:

    @classmethod
    def login_admin(cls):
        # 登录接口，获取token
        url = d1.get('url', 'base_url')+'/member/login'
        params = {"mobile_phone": d1.get('login', 'mobile_phone'),
                  "pwd": d1.get('login', 'pwd')}
        headers = eval(d1.get('headers', 'headers'))
        res = requests.post(url=url, json=params, headers=headers)

        cls.member_id = str(jsonpath(res.json(), '$..id')[0])  # 获取member_id
        cls.token = jsonpath(res.json(), '$..token')[0]  # 获取token
        headers['Authorization'] = 'Bearer ' + cls.token  # 获取含有token的参数头
        cls.headers = headers

    @classmethod
    def add_project(cls):
        # 新增项目接口，获取loan_id
        url = d1.get('url', 'base_url') + '/loan/add'
        params = {"member_id": cls.member_id,
                  "title": "世界这么大，借钱去看看",
                  "amount": 2000.00,
                  "loan_rate": 18.0,
                  "loan_term": 1,
                  "loan_date_type": 1,
                  "bidding_days": 10}
        headers = cls.headers
        res = requests.request(method='post', url=url, json=params, headers=headers)
        loan_id = jsonpath(res.json(), '$..id')[0]  # 获取loan_id
        setattr(BaseTest, 'loan_id', loan_id)  # 设置为类属性

    @classmethod
    def audit_project(cls):
        # 审核接口
        url = d1.get('url', 'base_url') + '/loan/audit'
        params = {"loan_id": cls.loan_id, "approved_or_not": True}
        requests.request(method='patch', url=url, json=params, headers=cls.headers)