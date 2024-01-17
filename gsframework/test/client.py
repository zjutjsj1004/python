import requests
import json

url = 'http://localhost:8888'  # 服务器地址和端口

data = {
    'key': 'value',
    'foo': 'bar'
}

headers = {
    'Content-Type': 'application/json'
}

# 发送 POST 请求
response = requests.post(url, data=json.dumps(data), headers=headers)

# 输出服务器的响应
print("Server response:", response.text)
