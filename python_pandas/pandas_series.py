from pandas import Series


def base():
    # series序列,基于list创建序列
    lst = ['python', 'c++', 'c#', 'java']
    ser = Series(lst)
    print(ser)

    # 指定索引
    ser = Series(lst, index=['a', 'b', 'c', 'd'])
    print(ser)
    print("使用索引:", ser['c'])

    # 基于dict创建索引
    score_dict = {
        'python': 100,
        'c++': 99,
        'c#': 98,
        'java': 97
    }

    ser = Series(score_dict)
    ser['java'] = 100
    print(ser)
    print(ser.index)
    print(ser[0])
    print(ser[1:])

    # series转为字典和列表和转文件
    score_dict = {
        'c++': 99,
        'python': 100,
        'c#': 98,
        'java': 97
    }
    ser = Series(score_dict)

    print('转list:', ser.tolist())
    print('转dict:', ser.to_dict())
    ser.to_excel('./data.xls')


def pandas_func():
    # pandas基本数据类型---series基本功能

    lst = ['python', 'c++', 'c#', 'java']
    ser = Series(lst, index=['a', 'b', 'c', 'd'])

    print('返回行轴标签列表:', ser.axes)
    print('返回对象数据类型:', ser.dtype)
    print('如果系列为空,则返回True:', ser.empty)
    print('返回底层数据的维度:', ser.ndim)
    print('返回系列的大小:', ser.size)
    print('系列作为ndarray返回', ser.values, type(ser.values))
    print('返回前n个数据:', ser.head(2))
    print('返回后n个数据:', ser.tail(1))


if __name__ == "__main__":
    pandas_func()