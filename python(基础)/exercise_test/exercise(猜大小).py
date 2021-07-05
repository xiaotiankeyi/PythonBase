import random


def call(count=0):
    asset = 1000
    while count < 3:
        print("\t\t猜大小游戏")
        print(">>>请输入你竞猜的数字")
        num = int(input(">>>>>>> "))
        robot = random.randint(1, 100)
        if num > robot:
            asset = asset + 10
            print(
                "robot出的是{}, 你出的是{}.....你赢了...资产为{}".format(
                    robot, num, asset))
        else:
            asset = asset - 10
            print(
                "robot出的是{}, 你出的是{}.....你输了....资产为{}".format(
                    robot, num, asset))
        count += 1
        if count >= 3:
            if asset >= 1000:
                print("你的资产为{},最后结果是你赢了 *^_^* *^_^* *^_^*".format(asset))
            else:
                print("你的资产为{},最后结果是你输了—_- -_- -_-".format(asset))
        else:
            pass


call()


def handle():
    asset = 1000
    count = 0
    while count < 5:
        print("\t\t猜大小游戏")
        print(">>>请输入你竞猜的数字")
        num = int(input(">>>>>>> "))
        robot = random.randint(1, 100)
        if num > robot:
            asset = asset + 10
            print(
                "robot出的是{}, 你出的是{}.....你赢了...资产为{}".format(
                    robot, num, asset))
        else:
            asset = asset - 10
            print(
                "robot出的是{}, 你出的是{}.....你输了....资产为{}".format(
                    robot, num, asset))
        count += 1
