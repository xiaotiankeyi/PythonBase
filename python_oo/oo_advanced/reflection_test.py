# 反射测试
"""
    反射原理,对getattr的应用,导入其他模块，利用反射查找该模块是否存在某个方法
"""
import os
import sys
import importlib
from python_oo.oo_advanced.oo_reflection import Chinese

i = Chinese(1.65, 62)
if hasattr(i, 'Features'):  # hasattr参数为(实例，查找的函数)
    accept = getattr(i, 'Features')
    print(accept())
else:
    print('不存在，编写其他逻辑')

print("查看来自于那个模块>>>>>", i.__module__)


"""动态导入模块（基于反射当前模块成员）应用"""

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
test = importlib.import_module("oo_exercise.exercise_one")


role = test.Riven("瑞雯")
print(role.__dict__)
