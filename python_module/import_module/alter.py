"""同级目录下的调用"""

from python_module.import_module import Mathematical

w = Mathematical.count(3, 9)
print(w)

from python_module.import_module.Mathematical import count, subtraction

t = count(3, 9)
print(t)

e = subtraction(9, 12)
print(e)

import sys

print(sys.path)
