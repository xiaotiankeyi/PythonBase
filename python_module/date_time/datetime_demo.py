"""日历___Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历:"""
import datetime
import calendar
import time
from datetime import datetime, timedelta
cal = calendar.month(2019, 7)
print("\n2019年7月的日历为:{}".format(cal))
# 判断是不是闰年
estimate = calendar.isleap(2016)
print("2019年是不是闰年(True/False):{}".format(estimate))

"""____time___"""
time.sleep(2)


print('当前时间:', datetime.now())

print('格式化当前时间——年月日时分秒', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print('格式化当前时间——年月日时分', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

"""
加一分钟: minutes=1
加一小时: hours=1
"""
addTime = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
print('当前时间+一天', type(addTime))
