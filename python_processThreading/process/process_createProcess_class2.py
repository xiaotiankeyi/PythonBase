"""自定义方法实现非阻塞性进程"""

from multiprocessing import Process
from multiprocessing import Pool
import time
import os
import random


class NewProcess(Process):

    def __init__(self, args):
        super(NewProcess, self).__init__()
        self.args = args
        self.p = Pool(5)

    def __way(self, task):
        start = time.time()
        time.sleep(random.randint(1, 5))
        end = time.time()

        # return f"父进程:{os.getppid()}, 子进程:{os.getpid()},任务【{task}】完成时间为{end - start}s"  # 异步调用并使用回调
        return f"完成时间为{end - start}s"

    def __callback(self, backResult):
        """接收Foo返回的字符"""
        # print(os.getppid(), "result", os.getpid(), backResult)
        print(backResult)

    def __poolRun(self):
        # p = Pool(5)
        print(p.__class__)
        systemStart = time.time()

        print(type(self.args))
        for val in self.args:
            print(val)
            self.p.apply_async(func=self.__way, args=(val,), callback=self.__callback)

        p.close()
        p.join()
        systemEnd = time.time()
        print(f"总的运行时长{systemEnd - systemStart}s")

    def run(self):
        self.__poolRun()


if __name__ == "__main__":
    task = ["游戏", "吃饭", "睡觉", "拖地", "洗衣服", "学习", "上厕所", "看视频"]
    p = NewProcess(task)
    p.start()
    p.join()
