"""
Name：   68
Time：   2020/12/11 15:37
E—mail： liubo3398@163.com
"""
from configparser import ConfigParser
from common.handle_path import CONF_PATH


class HandleConf(ConfigParser):

    def __init__(self, conf_file):
        """
        封装操作配置文件的方法
        :param conf_file: 配置文件的名字
        """
        super().__init__()
        self.read(conf_file, encoding='utf-8')


# 有几个配置文件，创建几个实例化对象
d1 = HandleConf(CONF_PATH+'/data.ini')
d2 = HandleConf(CONF_PATH+'/data2.ini')


if __name__ == '__main__':
    print(d1.get('url', 'base_url'))
    # print(d2.get('mysql', 'port'))
