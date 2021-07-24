"""调用上级目录模块......"""

"""调用py_module目录下的Mathematical模块......."""

import sys
import os
import importlib


"""推荐这种方法....os和sys的结合,在终端上也能执行"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from python_module.import_module.Mathematical import count, subtraction

t = count(3, 43)
print(t)

f = subtraction(2, 4)
print(f)
print(sys.path)

'''动态导入模块'''
accept = importlib.import_module("Mathematical")

t = accept.count(3, 43)
print(t)

f = accept.subtraction(2, 4)
print(f)
print(sys.path)