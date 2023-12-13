# 1.请确保您的Python版本是3.x: pip3 install gensim 和 pip3 install nltk
# 2. 需要下载Spacy的预训练模型: python3 -m spacy download en_core_web_sm


from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import nltk
nltk.download('punkt', quiet=True)

# 示例文本
text = "这是一段文本，我想要生成它的嵌入。"
# 分词和嵌入
tokenized_text = word_tokenize(text.lower())


# 训练Word2Vec模型
model = Word2Vec([tokenized_text], vector_size=50, window=5, min_count=1, workers=4)

# 提取文本嵌入
embedding = model.wv[tokenized_text]
print(embedding)

'''
$ python3 Word2Vec.py 
[[-1.0724545e-03  4.7286032e-04  1.0206699e-02  1.8018546e-02
  -1.8605899e-02 -1.4233618e-02  1.2917743e-02  1.7945977e-02
  -1.0030856e-02 -7.5267460e-03  1.4761009e-02 -3.0669451e-03
  -9.0732286e-03  1.3108101e-02 -9.7203208e-03 -3.6320353e-03
   5.7531595e-03  1.9837476e-03 -1.6570430e-02 -1.8897638e-02
   1.4623532e-02  1.0140524e-02  1.3515387e-02  1.5257311e-03
   1.2701779e-02 -6.8107317e-03 -1.8928051e-03  1.1537147e-02
  -1.5043277e-02 -7.8722099e-03 -1.5023164e-02 -1.8600845e-03
   1.9076237e-02 -1.4638334e-02 -4.6675396e-03 -3.8754845e-03
   1.6154870e-02 -1.1861792e-02  9.0322494e-05 -9.5074698e-03
  -1.9207101e-02  1.0014586e-02 -1.7519174e-02 -8.7836506e-03
  -7.0199967e-05 -5.9236528e-04 -1.5322480e-02  1.9229483e-02
   9.9641131e-03  1.8466286e-02]]
'''

# 示例文本
text1 = "这是一段文本，我想要生成它的嵌入。"
text2 = "另一段文本，我希望获得它的嵌入。"

# 分词和嵌入
tokenized_text1 = word_tokenize(text1.lower())
tokenized_text2 = word_tokenize(text2.lower())
model = Word2Vec([tokenized_text1, tokenized_text2], vector_size=50, window=5, min_count=1, workers=4)
# 提取文本嵌入
embedding1 = model.wv[tokenized_text1]
embedding2 = model.wv[tokenized_text2]

# 方法1: 计算欧氏距离
euclidean_distance = np.linalg.norm(embedding1 - embedding2)
print(f"欧氏距离: {euclidean_distance}")

# 欧氏距离: 0.11068378388881683


# 方法2: 计算余弦相似度  pip3 install scikit-learn

# 假设 embedding1 和 embedding2 是两个嵌入矩阵
# 将嵌入矩阵降维为二维数组
embedding1_flat = np.reshape(embedding1, (1, -1))
embedding2_flat = np.reshape(embedding2, (1, -1))

cosine_sim = cosine_similarity(embedding1_flat, embedding2_flat)
cosine_distance = 1 - cosine_sim[0][0]
print(f"余弦相似度: {cosine_distance}")
# 余弦相似度: 0.9576270207762718