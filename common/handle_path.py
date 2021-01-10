"""
Name：   68
Time：   2020/12/14 9:15
E—mail： liubo3398@163.com
"""
"""此模块专门用于处理项目中的绝对路径"""
import os


# 该项目的根目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件目录路径
CONF_PATH = os.path.join(BASE_PATH, 'conf')
# 数据文件目录路径
DATAS_PATH = os.path.join(BASE_PATH, 'datas')
# 日志文件目录路径
LOGS_PATH = os.path.join(BASE_PATH, 'logs')
# 测试报告文件路径
REPORTS_PATH = os.path.join(BASE_PATH, 'reports')
# 测试脚本文件路径
TESTCASES_PATH = os.path.join(BASE_PATH, 'testcases')
