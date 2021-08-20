import random
import time

from multiprocessing import Process


class handler(Process):
    def __init__(self, values):
        super(Process, self).__init__()
        self.values = values

    def run(self):
        print(self.name, "%s start operation func" % self.values)
        # print("多进程测试.......",)
        print(time.sleep(random.randint(1, 4)))
        print(self.name, "%s end operation func" % self.values)


if __name__ == "__main__":
    p_list = []
    for i in range(5):
        p = handler((i))
        p_list.append(p)

    for j in p_list:
        j.start()

    for j in p_list:
        j.join()

    print('main process end')
