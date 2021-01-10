"""
工具模块，用于存放一些小工具
"""
import re
from common.handle_conf import d1


def replace_data(data, cls):
    """
    批量替换测试数据中的数据
    :param data:需替换的数据（str）
    :param cls:测试类
    :return:替换后的数据
    """
    while re.search('#(.+?)#', data):
        # search：匹配并返回第一个符合规则的匹配对象
        res = re.search('#(.+?)#', data)
        # 获取需要替换的数据
        old = res.group()
        # 获取新数据属性名
        attr = res.group(1)
        try:
            # 根据属性名获取类属性
            new = str(getattr(cls, attr))
        except AttributeError:
            # 如果类属性没有，就去配置文件找
            new = d1.get('login', attr)
        # 替换
        data = data.replace(old, new)
    return data
