import os
ret = os.popen('pwd').read()
print (ret)

# $/data/gocpplua/python$ python3 ./python语法/3文件当前目录.py
# /data/gocpplua/python    <----- 输出当前目录


cloud_tools_dir = os.path.split(os.path.realpath(__file__))
print (cloud_tools_dir)
# $/data/gocpplua/python/python语法$ python3 3文件当前目录.py 
# ('/data/gocpplua/python/python语法', '3文件当前目录.py')