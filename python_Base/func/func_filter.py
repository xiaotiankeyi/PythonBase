# filter实现过滤筛选功能
people = ['sb_jack', 'sb_tom', 'sb_lucy', 'lucia', 'sb_birth']

"""显示判断开头字母功能"""


def replace(n):
    return n.startswith("sb")


def strip(func, accept):
    array = []
    for i in accept:
        """判断不是以sb开头的用户...."""
        if not func(i):
            array.append(i)
    return array


print(strip(replace, people))

"""第二种方法"""
print(strip(lambda x: x.startswith("sb"), people))
"""第三种方法"""
network = filter(lambda n: not n.startswith("sb"), people)
# print(list(network))
"""filter对获取的值做bool判断,,当字符串是以'sb'开头的就不添加进列表array,当字符串不是以'sb'开头就添加进列表array"""
