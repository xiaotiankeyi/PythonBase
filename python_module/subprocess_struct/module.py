import subprocess
import struct

'''platform模块用于访问平台相关属性'''
import platform

print(platform.version())
print(platform.system())
print(platform.machine())
print(platform.node())
print(platform.platform())
print(platform.processor())

for i in range(1, 10):
    for j in range(1, i+1):
        print('%d * %d = %d\t' % (j, i,(i*j)), end='')
    print("")