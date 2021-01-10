"""正则表达式"""
import unittest
import re


class TestData(unittest.TestCase):
    code = 0
    msg = 'Ok'

    def asd(self):
        self.abc = 123


d1 = "{'code': #code#, 'msg': '#msg#}"
def replace_data(data, cls):
    while re.search('#(.+?)#', data):
        # search：匹配并返回第一个符合规则的匹配对象
        res = re.search('#(.+?)#', data)
        # 获取需要替换的数据
        old = res.group()
        # 获取新数据属性名
        attr = res.group(1)
        # 根据属性名获取类属性
        new = str(getattr(cls, attr))
        # 替换
        data = data.replace(old, 123)
    return data

print(getattr(TestData, 'msg'))

