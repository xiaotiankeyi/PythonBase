import logging
import os

BASE_BIR = os.path.dirname(os.path.dirname(__file__))


def logger():
    # 实例化操作对象
    logger = logging.getLogger()

    # 制定日志输出方式

    handle = logging.FileHandler(
        BASE_BIR + "/output_log" + "/log_record.dat",
        "w+")

    # 制定日志输出格式
    output = logging.Formatter(
        "%(asctime)s\\%(module)s\\%(levelname)s\\%(levelno)s\\%(threadName)s:%(thread)d\\%(filename)s:%(lineno)d: "
        "%(message)s", datefmt='%Y-%m-%d %H:%M:%S %p')
    # 输出方式绑定输出格式
    handle.setFormatter(output)

    logger.addHandler(handle)
    logger.setLevel('DEBUG')

    return logger


if __name__ == "__main__":
    logger = logger()
    logger.info('测试输出')
