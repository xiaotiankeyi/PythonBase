from pandas import DataFrame
import pandas as pd
import os
import sys


def dict_create():
    df = DataFrame()
    print(df)

    data = {
        '语文': [90, 98, 87, 90],
        '数学': [92, 87, 90, 98]
    }

    df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
    print(df)
    yuwen_series = df['语文']
    max_yuwen = yuwen_series.max()  # 语文最高分
    print('语文最高分{max_score}'.format(max_score=max_yuwen))

    # 创建出总分列, 由每一行的语文和数学分数相加
    df['总分'] = df['语文'] + df['数学']
    max_sum = df['总分'].max()

    stu_name = df['总分'].idxmax()
    print('{stu}总分最高, {score}'.format(stu=stu_name, score=max_sum))


def list_create():
    data = [
        {'语文': 90, '数学': 92},
        {'语文': 98, '数学': 87},
        {'语文': 87, '数学': 90},
        {'语文': 90, '数学': 98},
    ]

    df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
    df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'], columns=['语文'])
    print(df)


def value_series_create():
    data = {
        '语文': pd.Series([90, 98, 87], index=['小明', '小红', '小刚']),
        '数学': pd.Series([92, 87, 90, 98], index=['小明', '小红', '小刚', '小丽'])
    }

    df = pd.DataFrame(data)
    print(df)


def base_function():
    data = [
        {'语文': 90, '数学': 92},
        {'语文': 98, '数学': 87},
        {'语文': 87, '数学': 90},
        {'语文': 90, '数学': 98},
    ]

    df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
    df.index.name = '姓名'
    df.columns.name = '科目'
    # print(df)
    # print("*" * 20)
    # reversed_df = df.T      # 行与列倒置,行变成列,列变成行
    # print(reversed_df)
    print('行轴标签和列轴标签:', df.axes)
    print('dtypes数据类型:', df.dtypes)
    print('判断是否为空dataframe:', df.empty)
    print('维度大小:', df.ndim)
    print('shape维度元组:', df.shape)
    print('元素的数量:', df.size)
    print('values', df.values)
    print('返回前几条数据:', df.head(2))
    print("*" * 20)
    print('返回后几条数据:', df.tail(1))

    # 对列的操作.....
    print(df["数学"])
    df['总分'] = df['数学'] + df['语文']
    print('添加了新列:', df)
    # del df['语文']
    # df.pop('数学')

    # 对行的基本操作
    print('选择某行,按标签选择:', df.loc['小明'])
    print('选择某行,按整数位置选择:', df.iloc[0])
    print('通过切片操作选择多行:', df[1:3])
    print(type(df[1:3]))
    # 添加行
    df2 = pd.DataFrame([{'语文': 100, '数学': 100}], index=['学霸'])
    df = df.append(df2)
    print(df)
    # 删除行
    df = df.drop('小明')
    print(df)


def save_file():
    data = [
        {'语文': 90, '数学': 92},
        {'语文': 98, '数学': 87},
        {'语文': 87, '数学': 90},
        {'语文': 90, '数学': 98},
    ]

    df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
    df.index.name = '姓名'
    path = os.path.dirname(__file__)
    df.to_csv(os.path.join(path, 'stu.csv'), encoding='gbk')
    df.to_excel(os.path.join(path, 'stu2.xls'), sheet_name='考试成绩')
    
    df.to_json(os.path.join(path, 'stu3.json'), force_ascii=False)
    df = pd.read_json(os.path.join(path, 'stu.data'))
    
    df.to_msgpack(os.path.join(path, 'stu.data'))
    df = pd.read_msgpack(os.path.join(path, 'stu.data'))
    
    df.to_pickle(os.path.join(path, 'stu.data'))
    df = pd.read_pickle(os.path.join(path, 'stu.data'))

    df.to_html(os.path.join(path, 'stu.data'))
    df = pd.read_html(os.path.join(path, 'stu.data'), encoding='utf-8')

if __name__ == "__main__":
    # dict_create()
    # list_create()
    # value_series_create()
    # base_function()
    save_file()
    path = os.path.dirname(__file__)
    print('测试', path)
    print(os.path.join(path, 'stu.csv'))