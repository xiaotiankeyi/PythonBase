"""自定义process方法"""
import time

from multiprocessing import Process
from multiprocessing import Lock


class Handler(Process):
    """
    自定义process方式加上同步锁的功能
    """
    lock = Lock()

    def __init__(self, values):
        super(Process, self).__init__()
        self.values = values
        self.lock = self.lock

    def __processLock(self):
        """调用"""
        try:
            self.lock.acquire()
            time.sleep(0.5)

            print(self.name, "%s start operation func" % self.values)

            print(self.name, "%s end operation func" % self.values)
        except Exception as err:
            return err
        finally:
            self.lock.release()
            pass

    def run(self):
        self.__processLock()


if __name__ == "__main__":
    p_list = []
    for i in range(5):
        p = Handler(i)
        p_list.append(p)
        p.start()

    for j in p_list:
        j.join()

    print('main process end')
