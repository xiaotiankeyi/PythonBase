# 游标定位
with open("variables.txt", 'r', ) as n:
    """返回当前指针所在文件的位置....."""
    print("当前指针位置为{}".format(n.tell()))

    """移动seek()"""
    n.seek(33, 0)
    print("当前指针位置为{}".format(n.tell()))

    print("======1", n.read())

    """指针返回开头"""
    n.seek(0, 0)
    print("=======当前指针位置为{}==============".format(n.tell()))

    """返回开头后再次读取"""
    print("======2", n.read())

"""
注意事项:
    1、移动seek((),(0, 1, 2))第二个参数中其中1,2选项只对'br'模式有效
    2、seek()支持者GBK编码
"""
