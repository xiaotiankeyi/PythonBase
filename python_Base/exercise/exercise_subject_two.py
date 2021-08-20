def handle():
    while True:
        day = 1
        j = 1
        money = 0
        print("\t.....请输入距离、、或输入'q'退出......")
        distance = input("....>>>>>>    ")
        if distance.isdecimal():
            distance = int(distance)
            if distance > 0:
                print("\t_____是不是一卡通?? 'y'是 'n'不是_____")
                yikatong = input(">>>>>[y/n] ")
                if yikatong.lower() == 'y':
                    while day < 20:
                        j = 1
                        while j <= 2:
                            if money < 100:
                                if distance <= 6:
                                    pass

                elif yikatong.lower() == 'n':
                    while day <= 20:
                        j = 1
                        while j <= 2:
                            if distance <= 6:
                                money += 3
                            if distance > 6 and distance <= 12:
                                money += 4
                            if distance > 12 and distance <= 22:
                                money += 5
                            if distance > 22 and distance <= 32:
                                money += 6
                            if distance > 32:
                                money += ((distance - 33) // 22) + 6 + 1
                            j += 1
                        day += 1
                    money += 5
                    print("\t...你的总花费为：%.4f" % money)
                else:
                    print("\t...你输入的有误,请重新输入>>>>>")

            else:
                print("\t\t距离必须大于零....请中心输入。。。")

        elif distance == "q":
            break
        else:
            print(".....必须是大于0的数字,请重新输入......")


"""
地铁交通价格调整为：6公里(含)内3元;6公里至12公里(含)4元;12公里至22公里(含)5元;22公里至32公里(含)6元;32公里以上部分，
每增加1元可乘坐20公里。使用市政交通一卡通刷卡乘坐轨道交通，每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;
满150元以后的乘次，价格给予5折优惠;支出累计达到400元以后的乘次，不再享受打折优惠。
"""
while True:
    money = 110
    print("\t.....请输入距离、、或输入'q'退出......")
    distance = input("....>>>>>>    ")
    if distance.isdecimal():
        distance = int(distance)
        if money < 100:
            if distance < 6:
                print("3元")
            if distance > 6 and distance <= 12:
                print("4元")
            if distance > 12 and distance <= 22:
                print("5元")
            if distance > 22 and distance <= 32:
                print("6元")
            if distance > 32:
                km = distance - 32
                if km % 20 == 0:
                    print(6 + km / 20)
                else:
                    print(6 + (km / 20) + 1)
        elif money >= 100 and money < 150:
            if distance < 6:
                print("价格为:%.2f" % (3 * 0.8))
            if distance > 6 and distance <= 12:
                print("价格为:%.2f" % (4 * 0.8))
            if distance > 12 and distance <= 22:
                print("价格为:%.2f" % (5 * 0.8))
            if distance > 22 and distance <= 32:
                print("价格为:%.2f" % (6 * 0.8))
            if distance > 32:
                km = distance - 32
                if km % 20 == 0:
                    print("价格为:%.2f" % ((6 + km / 20) * 0.8))
                else:
                    print("价格为:%.2f" % ((6 + (km / 20) + 1) * 0.8))

        elif money >= 150 and money < 400:
            pass
        elif money > 400:
            pass

    elif distance == "q":
        break
    else:
        print("\t\t输入错误,请再次输入>0的数....")
