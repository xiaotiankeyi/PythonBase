import sys
import os

sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from mysql.dbUtil import DBUitl
import numpy as np
import pandas as pd

def table_check():
    """数据表检索"""
    df=pd.DataFrame(pd.read_excel(os.path.join(os.path.dirname(__file__), 'o_order.xlsx')))
    # print(type(df))
    # print('行列维度:', df.shape)
    # print('信息:', df.info())
    # print('单列格式:', df['language'].dtype)
    # print('空值检查', df.isnull())
    # print('单列空值检查', df['language'].isnull())
    # print('单列唯一值检查', df['language'].unique())
    # print('查看某列的值:', df['order_amt'].values)
    # print('查看列名:', df.columns)
    # print('查看前十行数据:\n', df.head(10))
    # print('查看后十行数据:\n', df.tail(10))


def table_cleaning():
    """数据表清洗"""
    df=pd.DataFrame(pd.read_excel(os.path.join(os.path.dirname(__file__), 'o_order.xlsx')))
    print("空值处理,0填充:", df.fillna(value=0))




if __name__ == "__main__":
    # table_check()
    table_cleaning()