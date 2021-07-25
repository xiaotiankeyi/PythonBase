# 概念：是3.4以后的协程模块，是python实现并发重要的包，使用事件循环驱动实现并发
import asyncio

async def aunt():
    for i in range(10):
        print(f'{i}婶婶说，python是世界上最好的语言')
        await asyncio.sleep(0)      # 释放cpu避免阻塞

async def uncle():
    for i in range(10):
        print(f'{i}叔叔说，python是世界上最好的语言')
        await asyncio.sleep(0)

if __name__ == "__main__":
    a1 = aunt()
    a2 = uncle()

    # 创建循环事件
    loop = asyncio.get_event_loop()

    # 创建监听事件
    loop.run_until_complete(asyncio.gather(a1, a2))

    # 关闭事件循环
    loop.close()