# 水仙花数
# 例如：153 是一个"水仙花数"，因为 153=1 的三次方＋5 的三次方＋3 的三次方。

a = []
for i in range(100, 1000):
    s = 0
    m = list(str(i))
    for j in m:
        s += int(j) ** len(m)
    if i == s:
        print(i)
        a.append(i)

print('100-999的水仙花数为{}'.format(a))