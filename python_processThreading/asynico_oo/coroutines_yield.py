# 概念:两个函数或是多个函数之间互相切换的调用,本质是一个函数在执行,程序本身控制协程,在线程基础上开启协程
# 优点:但线程内就实现并发效果,最大限度的利用cpu,成本低,扩展性好
# 缺点:无法利用多核资源,协程需要和进程配合才能运行在多cpu上,进行阻塞操作时会阻塞掉整个程序

def service():
    while True:
        o = yield
        print('生产了第{}杯奶茶.....'.format(o))



def client():
    g = service()
    next(g)
    for i in range(10):
        g.send(i)
        print("消费了第{}杯奶茶,,,,".format(i))


if __name__ == "__main__":
    client()