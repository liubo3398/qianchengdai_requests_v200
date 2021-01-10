"""注册接口"""
import unittest
import requests
import random
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATAS_PATH
from common.handle_log import my_log
from common.handle_conf import d1
from common.handle_mysql import HandleDB



@ddt
class TestRegister(unittest.TestCase):
    # 读取excel测试数据
    word = HandleExcel(DATAS_PATH + '/data.xlsx', 'register')
    cases = word.read_excel()
    # 配置文件获取基本地址
    base_url = d1.get('url', 'base_url')
    # 获取headers（配置文件中获取的是str，需要eval()转换一下）
    headers = eval(d1.get('headers', 'headers'))
    # 实例化操作数据库的方法
    db = HandleDB()

    @list_data(cases)
    def test_01(self, item):
        # 准备数据（方法、url、参数、请求头、预期结果、title）
        method = item['method']
        url = self.base_url + item['url']

        # 动态处理参数
        params = eval(item['data'].replace('#mobile_phone#', self.randow_phone()))

        headers = self.headers
        expected = eval(item['expected'])
        title = item['title']
        row = item['case_id'] + 1

        # 获取实际结果
        response = requests.request(method=method, url=url, json=params, headers=headers)
        print('预期结果：', expected)
        print('实际结果：', response)

        # 断言
        try:
            self.assertEqual(expected['code'], response.json()['code'])
            self.assertEqual(expected['msg'], response.json()['msg'])
        except AssertionError as e:
            # 数据回写（会很影响速度，如果没有要求，不写）
            write = HandleExcel(workname=DATAS_PATH + '/data.xlsx', sheetname='register')
            write.write_excel(row=row, column=8, value='不通过')
            # 日志
            my_log.error(f'{title}-用例执行失败')
            print(expected)
            print(response.json())
            raise e
        else:
            # 数据回写（会很影响速度，如果没有要求，不写）
            write = HandleExcel(workname=DATAS_PATH + '/data.xlsx', sheetname='register')
            write.write_excel(row=row, column=8, value='通过')
            # 日志
            my_log.info(f'{title}-用例执行通过')

    def randow_phone(self):
        """封装随机生成手机号的方法,数据库检查是否注册过"""
        # while True:
        #     b = (176, 175, 174, 170, 171, 172, 173, 177)
        #     sql = 'select mobile_phone from futureloan.member;'
        #     db_phone = self.db.find_all(sql)
        #     print(db_phone)
        #     random_phone = random.randint(17600000000, 17699999999)
        #     print(random_phone)
        #
        #     if random_phone in db_phone:
        #         continue
        #     else:
        #         break
        # return random_phone
        return str(random.randint(17600000000, 17699999999))


if __name__ == '__main__':
    a = TestRegister().randow_phone()