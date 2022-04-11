'''
critical=50
error =40
warning =30
info = 20
debug =10
'''
"""先定义一个操作实例(logger对象),在定义日志输出方式(Handler对象),在定义日志输出格式(Formatter对象),
在为输出方式绑定输出格式(Handler.setFormatter(Formatter对象)),然后添加到实例中(logger.addHandler(Handler对象+Formatter对象)"""




import logging
def handle():
    # 1、定义logger对象:负责产生日志,然后交给Filter过滤,然后在交给不同的Handler输出
    logger = logging.getLogger(__name__)
    # logger.setLevel("DEBUG")

    # 2、Filter对象:不常用,略

    # 3、Handler对象:接收logger传来的日志,然后控制输出
    h1 = logging.FileHandler('logger.log', 'w', encoding='utf8')  # 打印到文件
    # h2 = output_log.StreamHandler()  # 打印到终端

    # 4、Formatter对象:日志格式
    output_1 = logging.Formatter(
        r"%(asctime)s\%(module)s\%(levelname)s\%(levelno)s\%(threadName)s:%(thread)d\%(filename)s:%(lineno)d: "
        "%(message)s", datefmt='%Y-%m-%d %H:%M:%S %p', )

    output_2 = logging.Formatter('%(asctime)s, %(levelname)s :  %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S %p', )

    # 5、为Handler对象绑定格式
    h1.setFormatter(output_1)
    # h2.setFormatter(output_2)

    # 6、将Handler添加给logger并设置日志级别
    logger.addHandler(h1)
    # logger.addHandler(h2)
    logger.setLevel("DEBUG")  # 设置级别

    return logger


if __name__ == "__main__":
    # 7、测试
    logger = handle()  # 调用函数
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
