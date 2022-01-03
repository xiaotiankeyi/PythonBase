from datetime import tzinfo, timedelta, datetime


class BeiJingTimezone(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=8)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return '+08:00'


bj = BeiJingTimezone()
dt = datetime(2018, 11, 1, hour=8, tzinfo=bj)
utc_naive = dt.replace(tzinfo=None) - dt.utcoffset()
# utc_naive datetime.datetime(2018, 11, 1, 0, 0)
timestamp = (utc_naive - datetime(1970, 1, 1)).total_seconds()
# print(timestamp)


def tokenTime():
    '''设置token有效期5分钟'''
    ToTime = (datetime.now() + timedelta(minutes=5)
              ).strftime("%Y-%m-%d %H:%M:%S")

    nowTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    a = datetime.strptime(ToTime, "%Y-%m-%d %H:%M:%S")
    print(type(a))
    b = datetime.strptime(nowTime, "%Y-%m-%d %H:%M:%S")
    print(b)

    lastTime = (a - b).total_seconds()
    print(type(int(lastTime)))


tokenTime()
