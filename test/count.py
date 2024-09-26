import os
import re
import shutil
import socket
import subprocess

def get_obj_count(search_dir):
    ret = get_count_with_ext(search_dir, "obj")
    return ret

def get_image_count(search_dir):
    ret = get_count_with_ext(search_dir, "jpg\|JPG\|png\|PNG")
    return ret

def get_count_with_ext(search_dir, ext):
    total_count = 0
    if not os.path.exists(search_dir):
        return 0
    cmd = "find {0} -iregex '.*\.\({1}\)$' |wc -l".format(search_dir, ext)
    ret = popen_communicate_sys_cmd(cmd)
    if ret[0]:
        total_count = ret[1].split('\n')[0]
    return int(total_count)

def popen_communicate_sys_cmd(cmd):
    proc = subprocess.Popen([cmd],
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdoutdata, stderrdata = proc.communicate()
    ret = proc.returncode
    if ret == 0:
        ret = [True, stdoutdata.decode('utf-8'), proc.pid, cmd]
    else:
        ret = [False, stderrdata.decode('utf-8'), proc.pid, cmd]
    return ret

count = get_image_count('./')
print(count)