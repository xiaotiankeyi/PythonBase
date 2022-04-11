"""
实现输入某年某月某日,判断这一天是这一年的第几天?闰年情况也考虑进去
"""
import calendar

print("==== please ouput in this format 'year/month/day' ====")
all_day = 0
while True:
    month = [31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = input(">>> ")
    y, m, d = year.split("/")
    y = int(y)
    m = int(m)
    d = int(d)
    # if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    if calendar.isleap(y):
        month[1] = 28
        if m > 0 and m < 12:
            if d > 0 and d < month[m - 1]:
                for i in month[0:m - 1]:
                    all_day += i
                all_day = all_day + d
            else:
                print("超出范围请重试")
        else:
            print("超出范围请重试")
        break
    else:
        if m > 0 and m < 12:
            if d > 0 and d < month[m - 1]:
                for i in month[0:m - 1]:
                    all_day += i
                all_day = all_day + d
            else:
                print("超出范围请重试")
        else:
            print("超出范围请重试")
        break
print("今天是%s的第%s天" % (y, all_day))
