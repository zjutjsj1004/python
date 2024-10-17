from zhipuai import ZhipuAI
client = ZhipuAI(api_key="") # 填写您自己的APIKey

model = "chatglm_turbo" #用于配置大模型版本

def getText(role, content, text = []):
    # role 是指定角色，content 是 prompt 内容
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

question = getText("user", "你好")

# 请求模型
response = client.chat.completions.create(
    model=model,
    messages=question
)
print(response)

# $ python3 /data/gocpplua/python/ai/zhipuai/zhipu_api.py
# {'code': 200, 'msg': '操作成功', 'data': {'request_id': '8168877954219582641', 'task_id': '8168877954219582641', 'task_status': 'SUCCESS', 'choices': [{'role': 'assistant', 'content': '" 你好👋！我是人工智能助手智谱清言，可以叫我小智🤖，很高兴见到你，欢迎问我任何问题。"'}], 'usage': {'prompt_tokens': 2, 'completion_tokens': 27, 'total_tokens': 29}}, 'success': True}

tools = [{
    "type": "web_search",
    "web_search": {
        "enable": True #默认为关闭状态（False） 禁用：False，启用：True。
    }
}]

messages = [{
    "role": "user",
    "content": "中国 2024 年一季度的GDP是多少 "
}]

response = client.chat.completions.create(
    model="glm-4",
    messages=messages,
    tools=tools
)
print(response)