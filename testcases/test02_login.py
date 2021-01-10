"""登录接口"""
import unittest
import requests
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATAS_PATH
from common.handle_log import my_log
from common.handle_conf import d1


@ddt
class TestLogin(unittest.TestCase):
    # 读取excel测试数据
    word = HandleExcel(DATAS_PATH + '/data.xlsx', 'login')
    cases = word.read_excel()
    # 配置文件获取基本地址
    base_url = d1.get('url', 'base_url')
    headers = eval(d1.get('headers', 'headers'))

    @list_data(cases)
    def test_01(self, item):
        # 准备数据（方法、url、参数、请求头、预期结果、title）
        method = item['method']
        url = self.base_url + item['url']
        params = eval(item['data'])
        headers = self.headers
        expected = eval(item['expected'])
        title = item['title']
        # row = item['case_id']+1

        # 获取实际结果
        response = requests.request(method=method, url=url, json=params, headers=headers)
        print(response.json())
        # 断言
        try:
            self.assertEqual(expected['code'], response.json()['code'])
            self.assertEqual(expected['msg'], response.json()['msg'])
        except AssertionError as e:
            # 数据回写（会很影响速度，如果没有要求，不写）
            # write = HandleExcel(workname=DATAS_PATH+'/data.xlsx', sheetname='login')
            # write.write_excel(row=row, column=8, value='不通过')
            # 日志
            my_log.error(f'{title}-用例执行失败')
            # my_log.exception(e)
            raise e
        else:
            # # 数据回写（会很影响速度，如果没有要求，不写）
            # write = HandleExcel(workname=DATAS_PATH+'/data.xlsx', sheetname='login')
            # write.write_excel(row=row, column=8, value='通过')
            # 日志
            my_log.info(f'{title}-用例执行通过')