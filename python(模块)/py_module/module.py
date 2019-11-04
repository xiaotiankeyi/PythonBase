"""跨目录调用模块"""

"""调用web目录下的division模块"""

"""第一种把整个division调用过来,动态导入模块"""
# from web import division
import importlib, sys, os

# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 把绝对路径写入系统变量
# sys.path.append(base_dir)

accept = importlib.import_module("web.division")

v = accept.accept(3, 6)
print(v)

g = accept.case(5, 67)
print(g)

"""第二种指定调用division模块下的accept,case方法"""
from web.division import accept, case

t = accept(3, 7)
print(t)

d = case(3, 54)
print(d)
