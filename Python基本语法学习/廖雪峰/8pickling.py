#把变量从内存中变成可存储或传输的过程称之为序列化
import pickle
d = dict(name = 'Bob')
a = pickle.dumps(d)
print (a)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print (d)


#json
import json
a = json.dumps(d)
print(a)