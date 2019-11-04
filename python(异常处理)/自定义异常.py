class Error(BaseException):
    def __init__(self, massage, parameter):
        self.massage = massage
        self.parameter = parameter


if __name__ == "__main__":
    try:
        # 知识点：主动抛出异常，就是实例化一个异常类
        accept = input("please input: ")
        if len(accept) < 5:
            raise Error(len(accept), 5)
    except Error as obj:
        print("输入的长度是%s,长度最少是%s" % (obj.massage,obj.parameter))

    else:
        print("The end of the")

    try:
        # 知识点：主动抛出异常，就是实例化一个异常类
        accept = input("please input: ")
        if type(accept) is not str:
            raise Error(type(accept), str)
    except Error as obj:
        print("输入的类型是%s,要输入的类型是%s" % (obj.massage, obj.parameter))
    else:
        print("The end of the")
    finally:
        print('我都会执行。。。')