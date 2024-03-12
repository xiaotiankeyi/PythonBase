# import datetime
# import time
import os

# # print(datetime.datetime.now())

# class Solution:
#     def twoSum(self, nums: list[int], target: int):
#         # for i in range(0,len(nums)):
#         #     for j in nums:
#         #         if nums.index(j) != i:
#         #             if nums[i] + j == target:
#         #                 return [i, nums.index(j)]
#         hashmap = {}
#         for index, num in enumerate(nums):
#             another_num = target - num
#             if another_num in hashmap:
#                 return [hashmap[another_num], index]
#             hashmap[num] = index
#         return None


# list1 = [3,2,3,4,5,7,8]

# obj = Solution()
# val = obj.twoSum(list1, 9)
# # print(val)

# import keyword
# # print(f"查看Python保留关键字长度为{len(keyword.kwlist)},值为:", keyword.kwlist)

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode):
#         # print(l1)
#         # print(l1.val[::-1])
#         l1.val.reverse()
#         val1 = ''.join(str(i) for i in l1.val)

#         l2.val.reverse()
#         val2 = ''.join(str(i) for i in l2.val)

#         restlu = int(val1) + int(val2)

#         return [int(i) for i in str(restlu)[::-1]]


# l1 = ListNode(val=[3,4,5,2,6,7])
# l2 = ListNode(val=[3,6,7,2,8])
# obj = Solution()
# val = obj.addTwoNumbers(l1, l2)
# # print(val)

# # 斐波那契数列
# a = 0
# b = 1
# while b < 10:
#     # print(b)
#     a, b = b, a+b

# i = 0
# l = 1
# while l <= 100:
#     i = l + i
#     l += 1
# # print("1到100的和为:", i)

# num = 0
# for i in range(1, 101):
#     num = i + num
# # print("1到100的和为:", num)


# list_db = [1, 3, 4, 5, 32, 33]
# value = iter(list_db)
# # print(type(value))
# # print('第一个值:', next(value))
# # print('第二个值:', next(value))

# # Python函数传递不可变类型
# def change(a):
#     # print(id(a))   # 指向的是同一个对象
#     a=10
#     # print(id(a))   # 一个新对象

# a=1
# # print(id(a))
# change(a)


# # Python传递可变类型实例
# def changeme(mylist):
#    "修改传入的列表"
#    mylist.append([1,2,3,4])
# #    print ("函数内取值: ", mylist)
#    return

# # 调用changeme函数
# mylist = [10,20,30]
# changeme(mylist)
# # print ("函数外取值: ", mylist)

# # 实现3X4的数组矩阵列表
# data_list = [[ j for j in range(i*4-3, i*4+1)] for i in range(1, 4)]
# # print(data_list)

# def data_list_func():
#     # 展示了3X4的矩阵列表实现
#     stop = 4
#     start = 1
#     data = []
#     for i in range(1, 4):
#         value = []
#         for j in range(start, i*stop+1):
#             value.append(j)
#         data.append(value)
#         start += stop
#     print(data)

# # data_list_func()
# import cProfile

# # cProfile.run("data_list")
# # cProfile.run("data_list_func()")

# # 把3X4矩阵装换为4X3的矩阵列表
# db_list = [[obj[i] for obj in data_list] for i in range(4)]
# # print(db_list)

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in data_list])
# # print(transposed)

# import builtins
# # print("内置变量:", dir(builtins))

# def number(num):
#     # 质数大于 1
#     if num > 1:
#     # 查看因子
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"不是质数")
#                 print(i,"乘于",num//i,"是",num)
#                 break
#         else:
#             print(num,"是质数")

#         # 如果输入的数字小于或等于 1,不是质数
#     else:
#         print(num,"不是质数")
# # number(1)

# # 使用递归遍历文件夹列表
# allfile = []

# def getallfile(path):
#     allfilelist = os.listdir(path)
#     for val in allfilelist:
#         if val.startswith('.'):
#             allfilelist.remove(val)

#     for file in allfilelist:
#         filepath = os.path.join(path, file)

#         if os.path.isdir(filepath):
#             getallfile(filepath)

#         allfile.append(filepath)
#     return allfile

# a= ""
# a.upper

def filter_func(str):
    new_str = ""
    for i in str:
        if i.isalpha():
            if i.islower():
                i = i.upper()
            new_str = new_str + i
        continue
    return new_str


if __name__ == "__main__":
    # path = os.path.abspath(__file__)
    # path = os.path.basename(__file__)
    # path = os.getcwd()
    # # print('===', path)
    # allfiles = getallfile(path)

    # for item in allfiles:
    # print(item)
    val = filter_func("adhaskj,.,.;;31888  fjksJHJKH")
    print(val)
    print(os.getpid(), os.getppid())