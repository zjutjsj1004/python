import time
import jwt
import requests
# 你的API密钥
api_key = ''

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
    "messages": [
        {
            "role": "system",
            "content": "作为一名助手，请回答用户的问题"
        },
        {
            "role": "user",
            "content": "你是谁？"
        },
        {
            "role": "assistant",
            "content": "I am a chatbot."
        }
    ]
}

# 发送POST请求
response = requests.post(url, headers=headers, json=data)

# 打印响应内容
print(response.status_code)
print(response.json())


# 请求数据(每次请求都是独立的，这里大模型无法拿到上下文)
data = {
    "model": "glm-4",
    "messages": [
        {
            "role": "user",
            "content": "我刚才问你什么问题"
        }
    ]
}


# 发送POST请求
response = requests.post(url, headers=headers, json=data)

# 打印响应内容
print(response.status_code)
print(response.json())
