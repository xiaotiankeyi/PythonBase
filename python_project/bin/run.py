from python_project.registered import registered_function
from python_project.login import login_function
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


def run_handle():
    tag = True
    while tag:
        print(
            "1:登录" + "\n"
                     "2:注册" + "\n"
                              "3:退出"
        )
        num = input("请输入所要操作的功能的序号：").strip()
        if num.isdecimal():
            if num == "1":
                login_function.login()

            elif num == "2":
                registered_function.registered()

            elif num == '3':
                tag = False

            else:
                print('你输入的操作不存在,请重新输入')

        else:
            print('输入错误,请输入序号')


if __name__ == "__main__":
    run_handle()
