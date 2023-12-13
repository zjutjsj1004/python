# 1.请确保您的Python版本是3.x，因为Spacy不再支持Python2: pip3 install spacy
# 2. 需要下载Spacy的预训练模型: python3 -m spacy download en_core_web_sm


import spacy

# 加载预训练的Spacy模型
nlp = spacy.load('en_core_web_sm')

# 处理文本并提取嵌入
doc = nlp("这是一段文本，我想要生成它的嵌入。")
embedding = doc.vector
print(embedding)

'''
$ python3 /data/gocpplua/python/ai/embedding/Spacy/Spacy.py
[-0.97404516 -0.31424996  0.48329335 -0.8831836   2.14576    -0.52992326
  0.24648315  0.70936114 -0.59333646 -0.15236664  0.02700162 -0.27442133
 -0.43697584  0.5602532   0.50198656  1.0357435  -1.1707355   0.6517239
  0.27422956  1.0238644  -1.5871341  -0.02881142 -0.22614343 -0.6546386
  1.1176177   0.5512005   0.17426307  2.2296238  -0.0456582  -0.13559754
  1.3713669   0.08642803  1.5126557  -0.12841314 -0.25988564 -0.7489109
 -0.14080608  1.1997787  -0.2682246   1.3470675  -0.7744963   0.0160799
  0.5040055  -0.68179286  0.7119055  -1.0793042  -0.16790283 -0.5211008
  0.7203028  -0.42466423  2.4368973  -2.1287446   1.0716405   0.71516395
 -0.3896181  -0.42848447 -0.5482133   0.10774012  1.4304007   0.6887263
  0.18651332 -0.7573172  -0.4941362  -0.7180542   0.95763594  0.16069126
 -0.3328939   0.02060302 -0.08142149 -0.09759805 -0.08461209 -0.8560814
 -0.0942827  -0.10612106  0.26780292  0.68715644  0.78375864 -0.97171974
  0.11489427 -0.16555117 -0.8187787  -0.29493403  0.15692873 -0.945914
  0.4238903   0.31425077 -1.2532775   0.86829364 -0.5909984   0.14847845
 -0.62752247  1.6103642   0.46038303  0.45904806  0.28616112  0.44162238]
'''