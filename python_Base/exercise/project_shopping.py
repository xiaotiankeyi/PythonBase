# 购物车功能
"""
功能要求:

    完成以下要求:
        要求用户输入总资产,列入:15000
        判断输入的金额能否购买价格最低的商品,如果不能让用户重新输入
        显示商品列表,让用户根据序号选择商品,加入购物车
        查看购物车,购物车内如果有相同的产品不要重复显示,以产品后面加数字形式表示此产品在购物车有两个或两个以上
        结算时,判断购物车是否为空,如果为空则提示填充购物车
        可以让用户删除购物车内的产品,或清空购物车
        结算时如果余额不足,则提示账户余额不足

"""

goods = [
    {"name": "电脑", "price": 1000},
    {"name": "Iphone", "price": 1200},
    {"name": "豪车", "price": 3280},
    {"name": "别墅", "price": 6500},
    {"name": "游艇", "price": 5800},
    {"name": "美女", "price": 2500},
]
while True:
    q = 0
    money = []
    shopping_cart = []  # 购物车
    for i, v in enumerate(goods, 1):
        money.append(v["price"])

    print("请输入您的总金额")
    salary = input(">>> ")
    if salary.isdecimal():  # 判断只让输入十进制数字
        salary = int(salary)
        money.sort()
        if salary <= 0:
            print("\n你玩我呢,没钱还来买\n")
            print("直接退出")
            break
        elif salary > 0 and salary < money[0]:  # 判断输入的金额能否购买价格最低的商品
            print("你的金额买不起任何一个东西\n")
        elif salary > money[0]:
            while True:
                all_price = 0  # 统计消费
                print("\33[36;1m商品列表\33[1m".center(40, "="))
                for i, v in enumerate(goods, 1):
                    print("%d %s \33[34;1m%d\33[1m" %
                          (i, v["name"].ljust(4, " "), v["price"]))
                print(
                    "请输入产品\33[31;1m序号\33[1m添加到购物车、返回上一层请按 \33[31;1mP \33[1m、完全退出请按 \33[31;1mQ\33[1m")
                seq_num = input(">>> ")
                if seq_num.lower() == "p":
                    # 退出这个循环,返回上个循环
                    break
                if seq_num.lower() == "q":
                    q = 1
                    break
                if seq_num.isdecimal():
                    seq_num = int(seq_num)
                    if seq_num > 0 and seq_num <= len(goods):
                        # 加入购物车
                        # 减1的原因,因为商品序号是从1开始算起,而购车是从0开始算起
                        shopping_cart.append(goods[seq_num - 1])
                        for y in shopping_cart:
                            all_price += y["price"]
                        print("\33[33;1m%s\33[1m 已添加到购物车\n" %
                              (goods[seq_num - 1]["name"]))
                        while True:
                            print(
                                "继续添加产品请按 \33[31;1mC\33[1m 、结算请按 \33[31;1mB\33[1m 、"
                                "查看购物车请按 \33[31;1mS\33[1m 、完全退出请按 \33[31;1mQ\33[1m")
                            final_cho = input(">>> ")
                            if final_cho.lower() == "c":
                                break
                            elif final_cho.lower() == "b":
                                while True:
                                    print(
                                        "您的余额为:\33[34;1m%d\33[1m 您购买的商品总价为:\33[34;1m%d\33[1m 确定购买吗? "
                                        "确定 \33[31;1mY\33[1m 取消 \33[31;1mN\33[1m" %
                                        (salary, all_price))
                                    confirm_bill = input(">>> ")
                                    if confirm_bill.lower() == "y":
                                        if shopping_cart != []:
                                            if salary >= all_price:
                                                salary = salary - all_price
                                                print("购买成功\n")
                                                all_price = 0
                                                shopping_cart = 0
                                                break
                                            elif salary < all_price:
                                                print("-_-！余额不足\n")
                                                break
                                        elif shopping_cart == []:
                                            print("购物车空空如也,填充后再来吧\n")
                                            break
                                    elif confirm_bill.lower() == "n":
                                        break
                                    else:
                                        print("输入有误,请重新输入\n")
                            elif final_cho.lower() == "s":
                                while True:
                                    print("\33[35;1m购物车\33[1m".center(40, "="))
                                    temp_cart = []
                                    for y in shopping_cart:
                                        if y not in temp_cart:
                                            temp_cart.append(y)
                                    for m, z in enumerate(temp_cart, 1):
                                        print(
                                            "%d %s \33[34;1m%d\33[1m %d个" %
                                            (m, z["name"].ljust(
                                                4, " "), z["price"], shopping_cart.count(z)))
                                    print(
                                        "\n购物车商品总金额为:\33[34;1m%d\33[1m" %
                                        all_price)
                                    print("您的余额为:\33[34;1m%d\33[1m" % salary)
                                    print(
                                        "按\33[31;1m序号\33[1m可删除商品 、继续请按 \33[31;1mC\33[1m 、清空购物车请按 \33[31;1mE\33[1m")
                                    ctrl_shop_cart = input(">>> ")
                                    if ctrl_shop_cart.lower() == "c":
                                        break
                                    elif ctrl_shop_cart.lower() == "e":
                                        all_price = 0
                                        shopping_cart = []
                                        print("以清空购物车")
                                        break
                                    elif ctrl_shop_cart.isdecimal():
                                        ctrl_shop_cart = int(ctrl_shop_cart)
                                        if ctrl_shop_cart > 0 and ctrl_shop_cart <= len(
                                                temp_cart):
                                            all_price = all_price - \
                                                temp_cart[ctrl_shop_cart - 1]["price"]
                                            shopping_cart.reverse()
                                            shopping_cart.remove(
                                                temp_cart[ctrl_shop_cart - 1])
                                            shopping_cart.reverse()
                                            print("删除成功\n")
                                        else:
                                            print("输入超出范围,请重新输入")
                                    else:
                                        print("输入有误,请重新输入\n")
                            elif final_cho.lower() == "q":
                                q = 1
                                break
                            else:
                                print("输入有误,请重新输入\n")
                    else:
                        print("数字超出范围,请重新输入\n")
                else:
                    print("请输入数字\n")
                if q == 1:
                    break

    else:
        print("\n只能输入数字,请重新输入\n")
    #
    if q == 1:
        break
