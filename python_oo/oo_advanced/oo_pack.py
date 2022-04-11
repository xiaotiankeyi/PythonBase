# 概念:包装,对现有的属性进行重新设定


class List(list):  # 继承list所有的属性,也可以派生出自己新的list方法,比如对append重新定义和mid
    def append(self, p_object):
        """派生自己的append:加上类型检查"""
        if not isinstance(p_object, int):
            """判断要添加的参数是不是int类型"""
            raise TypeError('must be int')
        super().append(p_object)

    # @property     # 设置为静态属性,调用时可以不加()
    def mid(self):
        """新增自己的属性,显示列表中最中间的数"""
        index = len(self) // 2
        return self[index]


l = List([1, 2, 3, 4, 6, 3, 78])

l.append(5)
print(l)

# l.append('1111111')  # 报错,必须为int类型

print(l.mid())

# 其余的方法都继承原有list的方法
l.insert(0, -123)
print(l)
l.clear()
print(l)
l.sort()
print(l)
