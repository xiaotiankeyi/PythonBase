import yagmail
import os

# print(os.getcwd())

# 连接邮箱服务器
yag = yagmail.SMTP(user='zhitian_lantuo@sina.com',
                   password='59c43837067936b5',
                   host='smtp.sina.com')

#邮件正文
subject = '自动化测试报告'
contents = '正文, 请查看附件'

#邮件发送
yag.send(['laizhitian163@163.com', '1606291729@qq.com'], subject, contents,
         [os.getcwd()+'\\'+ 'test.txt', os.getcwd()+'\\'+'2019-10-16 21_45_27htmlResult.html'])
