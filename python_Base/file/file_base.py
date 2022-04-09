def handle():
    with open("study_file.txt", 'r', encoding='utf8') as f:
        """读取文件所有内容"""
        f.read()
        file = [i.replace("\n", "") for i in f.read().strip()]
        file = set(file)  # 转化为集合,进行去重操作

        """判断是否为可读文件"""
        print(f.readable())  # 可读为True or False

        """读取第一行内容"""
        f.readline()

        """读取到的内容与列表方式返回,存放在列表中....."""
        f.readlines()

        """返回文件被访问的模式"""
        print(f.mode)

        """返回被访问的文件名"""
        print(f.name)

        """关闭文件"""
        f.close()

        """查看文件的编码格式"""
        print(f.encoding)


handle()

"""< r+ (读、写、指针在开始) >"""

"""
模式 	r 	r+ 	w 	w+ 	a 	a+
读 	    + 	+ 		+ 		+
写 		    + 	+ 	+ 	+ 	+
创建 			+ 	+ 	+ 	+
覆盖 			+ 	+
开始 	+ 	+ 	+ 	+
结尾 					+ 	+
"""

"""
1、求出花了多少钱
2、打印出所有商品信息格式为[{'name':'xxx','price':333,'count':3},...]
3、求单价大于10000的商品信息
"""
text = []
with open('shopping.txt') as f:
    for line in f:
        msg = line.strip('\n').split(",")
        for i in msg:
            v = i.split()
            # print(v)
        goods_info = {'name': v[0], 'price': int(v[1]), 'count': int(v[2])}
        # goods_info = {'name': msg}
        text.append(goods_info)
    print("商品", text)

# 1.总共花了多少钱:
total = 0
for item in text:
    # print(item)
    total += item['price'] * item['count']
print("加起来一共花了 %s" % total)

# 3.求单价大于10000的商品信息,格式同上
"""列表推导式表达"""
info = [item for item in text if item['price'] > 10000]
print("价格大于10000的商品有", info)

# 方法2
info = []
for item in text:
    if item['price'] > 10000:
        info.append(item)
print(info)
