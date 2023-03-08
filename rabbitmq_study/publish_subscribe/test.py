import os
import sys

# print('33', os.getcwd())
# pathlist = os.listdir(os.getcwd())
# print(pathlist)
# pathfile = [val for val in pathlist if val.endswith("log")][0]
# print(pathfile)


queueObj = [1, 2, 3]
routing = ["info", "warning", "error"]

for x, y in zip(queueObj, routing):
    print(x, y)