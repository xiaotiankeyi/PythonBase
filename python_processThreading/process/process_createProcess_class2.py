"""自定义方法实现非阻塞性进程"""

from multiprocessing import Process
from multiprocessing import Pool
import time
import os
import random


class NewProcess():
    """封装进程池方法,方便调用"""

    def __init__(self, args, processSize=5):
        super(NewProcess, self).__init__()
        self.args = args
        self.processSize = processSize

    def way(self, task):
        start = time.time()
        time.sleep(random.randint(1, 5))
        end = time.time()

        return f"父进程:{os.getppid()}, 子进程:{os.getpid()},任务【{task}】完成时间为{end - start}s"  # 异步调用并使用回调

    def callback(self, backResult):
        """接收Foo返回的字符"""
        print(os.getppid(), "result", os.getpid(), "|", backResult)

    def run(self):
        p = Pool(self.processSize)
        systemStart = time.time()

        for val in self.args:
            p.apply_async(func=self.way, args=(val,), callback=self.callback)

        p.close()
        p.join()
        systemEnd = time.time()
        print(f"总的运行时长{systemEnd - systemStart}s")


if __name__ == "__main__":
    task = ["游戏", "吃饭", "睡觉", "拖地", "洗衣服", "学习", "上厕所", "看视频"]
    p = NewProcess(task)
    p.run()
