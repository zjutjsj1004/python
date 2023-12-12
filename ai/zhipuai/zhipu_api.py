import zhipuai
zhipuai.api_key = "xxxxx" #填写控制台中获取的 APIKey 信息

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
response = zhipuai.model_api.invoke(
    model=model,
    prompt=question
)
print(response)

# $ python3 /data/gocpplua/python/ai/zhipuai/zhipu_api.py
# {'code': 200, 'msg': '操作成功', 'data': {'request_id': '8168877954219582641', 'task_id': '8168877954219582641', 'task_status': 'SUCCESS', 'choices': [{'role': 'assistant', 'content': '" 你好👋！我是人工智能助手智谱清言，可以叫我小智🤖，很高兴见到你，欢迎问我任何问题。"'}], 'usage': {'prompt_tokens': 2, 'completion_tokens': 27, 'total_tokens': 29}}, 'success': True}

