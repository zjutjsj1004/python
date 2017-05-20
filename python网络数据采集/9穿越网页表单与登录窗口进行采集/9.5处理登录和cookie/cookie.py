#cookie 方法1 -- 网站cookie单一
'''
import requests

params = {'username':'chenq', 'password':'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", data=params)  #注意是files=xxx
print('Cookoe is set to:')
print(r.cookies.get_dict())
print('-----------------')
print('go to profile page')
r = requests.post("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)  #注意是files=xxx
print(r.text)
'''

#cookie 方法2 -- 如果网站经常调整cookie或者我们不想用cookie，那我们可以用session
import requests
session = requests.Session()
params = {'username':'chenqi', 'password':'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", data=params)  #注意是files=xxx
print('Cookoe is set to:')
print(s.cookies.get_dict())
print('-----------------')
print('go to profile page')
#r = requests.post("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)  #注意是files=xxx
s=session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)



