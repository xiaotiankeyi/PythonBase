#计算 x 的 n 次方，如：3 的 4 次方 为 3*3*3*3=81

def mi(x, n):
    """
    计算x的n次方
    :param x:
    :param y:
    :return:
    """
    if n == 0:
        return 1
    else:
        return x * mi(x, n - 1)

print(mi(2, 8))