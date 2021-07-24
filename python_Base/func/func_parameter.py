""".......关键字参数......"""


def num(a, b, c):
    return a, b, c


number = num(b=4, c=8, a=44)
print(number)

"""默认参数"""


def paras(accept, parameter=34):
    return accept, parameter


query = paras(12)
print(query)

"""位置参数"""


def true(replace, lower, upper):
    return replace, lower, upper


strip = true(1, 2, 3)
print(strip)

"""*args"""


def join(format, *args):
    return format, args


startswith = join(23, {"age": 34}, [45, 78, 22], (3, 1, 4))
print(startswith)

"""不定长参数"""


def foo(x, y, *args, a=1, b, **kwargs):
    print(x, y)
    print(args)
    print(a)
    print(b)
    print(kwargs)


foo(1, 2, 3, 4, 5, b=3, c=4, d=5)


def func(x, *y, **z):
    print(z, x, y)


func(2, 4, 5, 78, 2, )


def func(*y, **x):
    print(y, x)

# func(*[1,35,6,2,])
