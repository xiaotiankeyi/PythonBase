# 继承顺序
"""
    概念：
        1、深度优先
        2、广度优先
        3、查看继承顺序的方法为( .__mro__)
"""


class A():
    def output(self):
        return 'A'


class B(A):
    def output(self):
        return 'B'


class C(A):
    def output(self):
        return 'C'


class D(B):
    def output(self):
        return 'D'


class E(C):
    def output(self):
        return 'E'


class F(D):
    # def output(self):
    #     return 'F'
    pass


class G(E):
    def output(self):
        return 'G'


accept = F()
print(F.__mro__)
print(accept.output())
