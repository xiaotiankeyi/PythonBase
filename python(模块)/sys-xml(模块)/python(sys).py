import time,sys

# for i in range(10):
#     sys.stdout.write("#")   #编写进度条功能
#     time.sleep(0.2)
#     sys.stdout.flush()      #刷新

"""获取python解释器的版本信息"""
v= sys.version
print("\n",v)

"""返回操作系统平台名称"""
# g = sys.platform()
# print(g)

def progress(percent,width=50):
    if percent >= 1:
        percent=1
    show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
    print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')


#=========应用==========
data_size=1025
recv_size=0
while recv_size < data_size:
    time.sleep(0.3) #模拟数据的传输延迟
    recv_size+=1024 #每次收1024

    percent=recv_size/data_size #接收的比例
    progress(percent,width=70) #进度条的宽度70