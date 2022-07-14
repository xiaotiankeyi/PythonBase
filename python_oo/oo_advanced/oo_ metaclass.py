# 创建元类


def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))

if __name__ == "__main__":
    obj = Hello()
    print(type(Hello))
    print(obj.__dict__)
    obj.hello()