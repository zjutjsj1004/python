# python3
import subprocess
def popen_communicate_sys_cmd(cmd):
    proc = subprocess.Popen([cmd],
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdoutdata, stderrdata = proc.communicate()
    ret = proc.returncode
    print("ret:", ret)
    if ret == 0:
        ret = [True, stdoutdata.decode('utf-8'), proc.pid, cmd]
    else:
        ret = [False, stderrdata.decode('utf-8'), proc.pid, cmd]
    return ret

cmd = './main'
res = popen_communicate_sys_cmd(cmd)
print(res)

cmd = 'python3 submain.py 2'
res = popen_communicate_sys_cmd(cmd)
print(res)