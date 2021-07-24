"""同级目录下的调用"""

import Mathematical

w = Mathematical.count(3, 9)
print(w)

from Mathematical import count, subtraction

t = count(3, 9)
print(t)

e = subtraction(9, 12)
print(e)

import sys

print(sys.path)
