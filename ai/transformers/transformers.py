'''
如果您不想使用 OpenAI 或其他付费服务，而是想要使用本地模型进行生成，可以使用一些开源的预训练模型，例如 GPT-2、GPT-Neo、BERT 等。
以下是一个使用 Hugging Face Transformers 库（一个用于访问和使用各种预训练模型的库）的简单示例

首先，确保您已安装 Transformers 库：
pip3 install transformers
pip3 install torch

使用以下 Python 代码根据 prompt 生成 completion
'''

from transformers import GPT2Tokenizer, GPT2LMHeadModel

# 加载 GPT-2 预训练模型和分词器
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 定义 prompt
prompt = "Once upon a time, in a land far, far away"

# 将 prompt 分词并编码
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 生成 completion
output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

# 解码生成的文本
completion_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(completion_text)
