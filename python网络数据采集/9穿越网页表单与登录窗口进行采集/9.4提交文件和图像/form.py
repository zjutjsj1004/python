#提交文件和图像
import requests

files = {'uploadFile':open('F:\\github\\python.git\\trunk\\python网络数据采集\\9穿越网页表单与登录窗口进行采集\\9.4提交文件和图像\\1.jpg', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)  #注意是files=xxx

print(r.text)

