#提交表单
import requests

params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params)  #注意是data=xxx

print(r.text)