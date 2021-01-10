"""
运行入口
"""
import time
import unittest
from unittestreport import TestRunner
from common.handle_path import TESTCASES_PATH

suite = unittest.defaultTestLoader.discover(TESTCASES_PATH)


run = TestRunner(suite=suite,
                 # filename=f"report_{time.strftime('%Y-%m-%d_%H-%M-%S')}.html",
                 filename="report.html",
                 report_dir=r"./reports",
                 title='qcd_测试报告',
                 tester='刘波',
                 desc="前程贷接口自动化测试生产的报告",
                 templates=1
                 )

run.run()

# &&&&&&&&&&&&&&&&&&&&&&&&发送测试报告到邮箱&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
run.send_email(host='smtp.163.com',  # smtp服务器地址
               port=465,  # smtp端口
               user='liubo3398@163.com',  # 邮箱账号
               password='EKDMKWPHGLQMTHVM',  # 邮箱密码（需要在邮箱中先开启smtp服务，获取这个密码）
               to_addrs='1119889127@qq.com'  # 需要发送的邮箱，多个账号用list
)
# &&&&&&&&&&&&&&&&&&&&&&&&发送测试报告到邮箱&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
run.dingtalk_notice()
run.weixin_notice()