# 概念:是3.4以后的协程模块,是python实现并发重要的包,使用事件循环驱动实现并发
import asyncio

async def aunt():
    for i in range(1, 2):
        print(f'{i}婶婶说,python是世界上最好的语言')
        await asyncio.sleep(1)
        return i

async def uncle():
    result = await aunt()       # 阻塞了,在等待aunt函数完成
    print(f'{result}叔叔说,{result}婶婶说的对！！')

if __name__ == "__main__":

    # 创建循环事件
    loop = asyncio.get_event_loop()

    # 创建监听事件
    loop.run_until_complete(uncle())

    # 关闭事件循环
    loop.close()