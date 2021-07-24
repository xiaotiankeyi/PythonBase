"""日历___Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历："""
import calendar,time

cal = calendar.month(2019, 7)
print("\n2019年7月的日历为：{}".format(cal))
# 判断是不是闰年
estimate = calendar.isleap(2016)
print("2019年是不是闰年(True/False)：{}".format(estimate))

"""____time___"""
time.sleep(2)

import datetime

print(datetime.datetime.now())
