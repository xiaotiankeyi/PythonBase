# sorted排序

goods = [
    {"name": "电脑", "price": 1000},
    {"name": "Iphone", "price": 1200},
    {"name": "豪车", "price": 3280},
    {"name": "别墅", "price": 6500},
    {"name": "游艇", "price": 5800},
    {"name": "美女", "price": 2500},
]

number = [1, 21, 312, 2, 211, 32, 1, 0, 23, 44]
print('排序:', sorted(number, reverse=False))

print(sorted(goods, key=lambda x:x['price'], reverse=False))