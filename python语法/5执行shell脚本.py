# commands是python2版本里的，在python3.0以上已经没有commands模块了，使用subprocess代替commands
import subprocess
a =  subprocess.call('ls', shell=True)
print(a)
