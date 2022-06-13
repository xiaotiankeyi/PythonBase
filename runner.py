# import datetime
# import time

# print(datetime.datetime.now())

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
# print(val)

from hashlib import blake2b
from lib2to3.pytree import Node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        # print(l1)
        # print(l1.val[::-1])
        l1.val.reverse()
        val1 = ''.join(str(i) for i in l1.val)

        l2.val.reverse()
        val2 = ''.join(str(i) for i in l2.val)

        restlu = int(val1) + int(val2)

        return [int(i) for i in str(restlu)[::-1]]



l1 = ListNode(val=[3,4,5,2,6,7])
l2 = ListNode(val=[3,6,7,2,8])
obj = Solution()
val = obj.addTwoNumbers(l1, l2)
print(val)