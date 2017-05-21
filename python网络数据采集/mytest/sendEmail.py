#cxicrbmclkfzdcgg  chenqiailn1314
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#http://www.runoob.com/python/python-email.html
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender='3100768452@qq.com'    # 发件人邮箱账号
my_pass = 'cxicrbmclkfzdcgg'              # 发件人邮箱密码
my_user='3100768452@qq.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEText('亲爱的开发者你好，目前浙江畅唐网络正在进行人才的招聘，详情请见官网:http://www.ct108.com/join/job 。\n' \
        '公司成立于2007年5月，注册资金7500万，坐落于美丽的钱塘江畔。\n' \
        '目前诚招网站程序员，C++软件工程师，网页前端工程师，测试工程师，运营人员，美工等等！\n' \
        '需要内推请添加QQ:3100768452 请备注:内推\n' \
        '需要内推请添加QQ:3100768452 请备注:内推\n' \
        '需要内推请添加QQ:3100768452 请备注:内推','plain','utf-8')

        msg['From']=formataddr(["浙江畅唐网络",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="浙江畅唐网络诚邀您的加入"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465,不是网上说的25，而且要使用SMTP_SSL不是SMTP
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败:%s" % str(e))
    
'''
#发送邮件:http://www.cnblogs.com/leetao94/p/5460520.html
#https://zhuanlan.zhihu.com/p/24180606
import smtplib
from email.mime.text import MIMEText
import sys
type = sys.getfilesystemencoding()
_user = "3100768452@qq.com"
_pwd  = "cxicrbmclkfzdcgg"
_to   = "3100768452@qq.com"

msg = MIMEText("Test")
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    #s.set_debuglevel(1)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print ("Success!")
except smtplib.SMTPException as e:
    print ("Failure to send email:", e)
'''