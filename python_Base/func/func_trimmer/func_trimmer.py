"""
装饰器概念：
    本质就是函数，功能是为其它函数添加附加功能......
原则：不修改被修饰函数的源代码......
      不修改被修饰函数的调用方式......

      装饰器 = 高阶函数 + 函数的嵌套 + 闭包
      加上返回值 + 参数
"""
import time

"""装饰器的框架"""


def trimmer(func):  # 第一步，目前形参是test
    def wrapper():
        # print(func)
        start_time = time.time()  # 第五步
        func()  # 第六步，运行test
        stop_time = time.time()  # 第九步
        print("运行的时间是%s " % (stop_time - start_time))  # 第十步

    return wrapper  # 第二步，timmer运行完返回wrapper地址


"""@表示语法堂,@后面加上装饰器>>>>相当于test = timmer(test)"""


@trimmer
def function():
    time.sleep(2)  # 第七步
    print("test函数运行完毕")  # 第八步

function()

"""源代码没有被修改，但是调用方式被修改了....."""
# ret = trimmer(function)  #第三步，获取wrapper地址并赋值给ret
# ret()   #第四步，运行函数wrapper

"""源代码没有被修改，调用方式没被修改"""
# test = trimmer(function)
# test()  #运行函数wrapper

