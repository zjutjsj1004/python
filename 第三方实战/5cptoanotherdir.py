import os
import subprocess
from termios import VREPRINT

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

def cus_cp(srcPath):
  i = 0
  for root, _, files in os.walk(srcPath):
    for file_name in files:
      print(i)
      i = i + 1
      full_file_name = os.path.join(root, file_name)
      firstLevel = full_file_name.split('/')[-4]
      srcDir = "/data/gocpplua/python/第三方实战/update-images/{0}".format(firstLevel)
      dstDir = "/data/gocpplua/python/第三方实战/images/{0}".format(firstLevel)
      print(srcDir, "==>", dstDir)
      popen_communicate_sys_cmd("mv /{0}/* /{1}".format(srcDir, dstDir))
      break


cus_cp("/data/gocpplua/python/第三方实战/update-images")


path1 = "images/insta_one_default/VID/cam0/a.png"
path2 = "images/insta_pano_default/VID/a.png"

video_name = os.path.join(*path1.split('/')[0:-3])
print(video_name)

video_name = os.path.join(*path2.split('/')[0:-2])
print(video_name)

video_name = path1.split('/')[-4]
print(video_name)

video_name = path2.split('/')[-3]
print(video_name)