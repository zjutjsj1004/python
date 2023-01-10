import os
cmd = 'ls -l {0}'.format("/usr")
cmd = cmd + " |awk '/^d/ {print $NF}'"
ret = os.popen(cmd)
ret = ret.read()
print(ret)
print("-----------------------------")
ret = ret.split('\n')
print(ret)
print("-----------------------------")
for name in ret:
  if name.find("insta_one") != -1:
    print("one")
  elif name.find("insta_pro") != -1:
    print("pro")
  elif name.find("bi") != -1:
    print("bin")
  else:
    print("default")


cmd = "ls -d */"
ret = os.popen(cmd)
ret = ret.read()
print(ret)
print("-----------------------------")
ret = ret.split('\n')
print(ret)
