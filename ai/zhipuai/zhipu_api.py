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

