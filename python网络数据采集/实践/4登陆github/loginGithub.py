# coding:utf-8



import requests
from bs4 import BeautifulSoup

USERNAME = 'FizLBQ'
PWD = 'Ll139196'

LoginUrl_GET = 'https://github.com/login'
LoginUrl = 'https://github.com/session'

headers = {
    'Host': 'github.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://github.com',
    'Connection': 'keep-alive',
}

formData = {
    'commit': 'Sign+in',
    'utf8': "✓",
    "login": "XXXXXXXX",
    "password": "XXXXXXX",

}
s = requests.Session()
RESULT = s.get(LoginUrl_GET, headers=headers)


content = RESULT.content

with open('login.html', 'wb') as fp:
    fp.write(content)
html = open('login.html', 'rb')
soup = BeautifulSoup(html, "html.parser")
token = soup.find('input', {'name': 'authenticity_token'})['value']
formData['authenticity_token'] = token

# RESULT = s.post(LoginUrl, headers=headers, data=formData,)
RESULT = s.post(LoginUrl, data=formData,)

content=RESULT.content
print (RESULT.url)

print (RESULT.status_code)
print (RESULT.cookies)

with open('bitbucket.html', 'wb') as fp:
    fp.write(content)