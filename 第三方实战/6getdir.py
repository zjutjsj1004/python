import os

cmd = "ls -l /usr/ |awk '/^d/ {print $NF}'"
ret = os.popen(cmd)
ret = ret.read()
print(ret)
print("-----------------------------")
ret = ret.split('\n')
print(ret)
print("-----------------------------")



cmd = "ls -d */"
ret = os.popen(cmd)
ret = ret.read()
print(ret)
print("-----------------------------")
ret = ret.split('\n')
print(ret)
