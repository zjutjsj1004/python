
#参考:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000
# # 输入Email地址和口令:
#from_addr = input('From: ')
#password = input('Password: ')
# 输入收件人地址:
#to_addr = input('To: ')
# 输入SMTP服务器地址:
#smtp_server = input('SMTP server: ')

# 输入Email地址和口令:
from_addr = "448764699@qq.com"
password = "XXX"
# 输入收件人地址:
to_addr = "448764699@qq.com"
# 输入SMTP服务器地址:
smtp_server = "smtp.qq.com"

#有时候发送没有反应，我们就调整端口试试
import smtplib
server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25,qq SMTP服务器（端口465或587）
server.ehlo()
server.starttls()
server.set_debuglevel(1)
try:
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], "1212")
except:
    print("Error")
else:
    print("OK")
server.quit()