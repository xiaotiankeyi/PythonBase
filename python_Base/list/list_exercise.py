# v = ['egon', 'male', '18', '3000']
#
# text = []
# for i in v:
#     goods_info = {'name': v[0], 'price': v[1], 'count': v[2]}
#     # goods_info = {'name': msg}
#     text.append(goods_info)
# print("商品", text)

goods = [
    {"name": "电脑", "price": 1000},
    {"name": "Iphone", "price": 1200},
    {"name": "豪车", "price": 3280},
    {"name": "别墅", "price": 6500},
    {"name": "游艇", "price": 5800},
    {"name": "美女", "price": 2500},
]

temp_cart = []
for y in goods:
    if y not in temp_cart:
        temp_cart.append(y)
# print(temp_cart)
all_price = 10000
for m, z in enumerate(temp_cart, 1):
    print(m, z["name"], z["price"])
num = int(input("序号>>>> "))
all_price = all_price - temp_cart[num - 1]["price"]
print(temp_cart[num - 1]["price"])
print(temp_cart)
print(all_price)


