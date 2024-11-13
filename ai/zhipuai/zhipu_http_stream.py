import time
import jwt
import requests
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 你的API密钥
api_key = os.getenv("ZHIPU_API_KEY")
print(api_key)
# 请求的URL
url = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
def generate_token(apikey: str, exp_seconds: int):
    try:
        id, secret = apikey.split(".")
    except Exception as e:
        raise Exception("invalid apikey", e)
 
    payload = {
        "api_key": id,
        "exp": int(round(time.time() * 1000)) + exp_seconds * 1000,
        "timestamp": int(round(time.time() * 1000)),
    }
 
    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
        headers={"alg": "HS256", "sign_type": "SIGN"},
    )


# 请求头
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# 请求数据
data = {
    "model": "glm-4",
    "stream": "true", # 关键字段！！！！
    "messages": [
        {
            "role": "system",
            "content": "作为一名助手，请使用英文回答用户的问题,每个问题字数需要大于200字"
        },
        {
            "role": "user",
            "content": "你是谁？"
        }
    ]
}

# 发送POST请求
with requests.post(url, headers=headers, json=data, stream=True) as response:
    # 检查响应状态码
    if response.status_code == 200:
        # 逐行读取响应内容
        for line in response.iter_lines():
            if line:
                # 处理每一行数据，这里简单地将其解码为字符串并打印
                decoded_line = line.decode('utf-8')
                print(decoded_line)
    else:
        print(f"Failed to retrieve response: {response.status_code}")