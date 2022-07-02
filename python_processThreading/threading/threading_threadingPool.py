from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

import time

# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times

def handle_func():
    executor = ThreadPoolExecutor(max_workers=2)

    # 通过submit函数提交执行的函数到线程池中,submit函数立即返回,不阻塞
    task1 = executor.submit(get_html, (3))
    task2 = executor.submit(get_html, (2))

    # done方法用于判定某个任务是否完成
    print(task1.done())

    # cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
    print(task2.cancel())

    time.sleep(4)
    print(task1.done())

    # result方法可以获取task的执行结果
    print(task1.result())


def get_result():
    #有时候我们是得知某个任务结束了,就去获取结果,而不是一直判断每个任务有没有结束。
    # 这是就可以使用as_completed方法一次取出所有任务的结果
    
    executor = ThreadPoolExecutor(max_workers=2)
    urls = [3, 2, 4] # 并不是真的url
    all_task = [executor.submit(get_html, (url)) for url in urls]

    for future in as_completed(all_task):
        data = future.result()
        print("in main: get page {}s success".format(data))


if __name__ == "__main__":
    # handle_func()
    get_result()