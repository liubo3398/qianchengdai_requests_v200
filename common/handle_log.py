"""
Name：   68
Time：   2020/12/10 10:58
E—mail： liubo3398@163.com
"""
import logging
from common.handle_path import LOGS_PATH


def handle_log(name='68', level='DEBUG', filename=LOGS_PATH+r'\log.log', fh_level='DEBUG', sh_level='DEBUG'):
    # 1、创建日志收集器
    log = logging.getLogger(name)

    # 2、设置收集器的等级DEBUG
    log.setLevel(level)

    # 3、设置输入的渠道以及等级
    # 3.1、输出到文件
    fh = logging.FileHandler(filename, encoding='utf-8')
    fh.setLevel(fh_level)
    log.addHandler(fh)  # 绑定日志收集器

    # 3.2、输出到打印台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)  # 绑定日志收集器

    # 4、设置日志的输出格式
    format = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
    fh.setFormatter(format)  # 设置到文件
    sh.setFormatter(format)  # 设置到打印台

    # 返回日志收集器
    return log


# 实例化日志收集器，防止多次创建，直接调用该对象
my_log = handle_log()

if __name__ == '__main__':
    my_log.debug('这是debug级别日志')
    my_log.info('这是info级别日志')
    my_log.warning('这是warning级别日志')
    my_log.error('这是error级别日志')
    my_log.critical('这是critical级别日志')
