# 概念：是3.4以后的协程模块，是python实现并发重要的包，使用事件循环驱动实现并发
import asyncio
import functools

async def aunt(x, y):
    print(f'婶婶问，{x}+{y}等于几？？')
    await asyncio.sleep(1)
    return x+y

async def uncle(x, y):
    # 创建task任务
    task = asyncio.create_task(aunt(x, y))
    # task绑定回掉函数
    task.add_done_callback(functools.partial(result, x, y))

    # 释放下cpu,进行其他操作
    await asyncio.sleep(0)

    print(f'叔叔开始计算')
    for i in range(50):
        print('呃。。。。')
        await asyncio.sleep(0.1)

def result(n, m, t):
    print(f'计算：{n}+{m}={t.result()}')

if __name__ == "__main__":

    # 创建循环事件
    loop = asyncio.get_event_loop()

    # 创建监听事件
    loop.run_until_complete(uncle(10, 5))

    # 关闭事件循环
    loop.close()