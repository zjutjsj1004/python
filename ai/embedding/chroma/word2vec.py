import chroma # pip3 install chroma
import numpy as np
from gensim.models import Word2Vec # pip3 install gensim

# 步骤1：安装Chroma并导入所需的库

# 步骤2：准备数据
text = "ChatGPT（全名：Chat Generative Pre-trained Transformer），是OpenAI [1]研发的一款聊天机器人程序 [12]，于2022年11月30日发布 [2-3]。ChatGPT是人工智能技术驱动的自然语言处理工具，它能够基于在预训练阶段所见的模式和统计规律，来生成回答，还能根据聊天的上下文进行互动，真正像人类一样来聊天交流，甚至能完成撰写邮件、视频脚本、文案、翻译、代码，写论文 [21]等任务。 [2]"

# 步骤3：创建数据库
db_name = "knowledge_db"
vector_dim = 300

db = chroma.Database(db_name, vector_dim)

# 步骤4：将文字转为向量并存入Chroma数据库
# 使用Word2Vec模型
sentences = [text.split()]  # 将文本分成句子或词语的列表
model = Word2Vec(sentences, vector_size=vector_dim, min_count=1)  # 训练Word2Vec模型

# 获取句子向量
sentence_vector = np.mean([model.wv[word] for word in text.split()], axis=0)

# 将句子向量存入Chroma数据库
db.add_vector("text_vector", sentence_vector)

# 步骤5：提问并获取输出结果
# 查询"chatgpt是什么？"的向量表示形式
query = "chatgpt是什么？"
query_vector = np.mean([model.wv[word] for word in query.split()], axis=0)

# 使用Chroma的查询功能检索最相似的向量
most_similar = db.search(query_vector)

# 输出最相似向量的标识符
print("Most similar vector ID:", most_similar)