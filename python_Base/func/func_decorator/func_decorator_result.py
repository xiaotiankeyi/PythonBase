# 装饰器返回值
import time

"""装饰器的框架"""


def timmer(func):  # 第一步,目前形参是test
    def wrapper():
        # print(func)
        start_time = time.time()  # 第五步
        ret = func()  # 第六步,运行test
        stop_time = time.time()  # 第九步
        print("运行的时间是%s " % (stop_time - start_time))  # 第十步
        return ret  # "我是test的返回值"

    return wrapper  # 第二步,返回wrapper地址


"""@表示语法堂,@后面加上装饰器>>>>相当于test = timmer(function)"""


# @timmer
def function():
    time.sleep(2)  # 第七步
    print("test函数运行完毕")  # 第八步
    return "我是test的返回值"

function = timmer(function)

print(function())  # 运行wrapper


