#!/usr/bin/env python3
# coding: utf-8
# email:zjut.cq@gmail.com

# 混淆py文件
# 使用前面需要执行 SOURCE_FILE_FOLD_PATH(文件夹路径)  和 DEST_FILE_FOLD_PATH(混淆后输出文件路径)
import requests
import json
import os
import shutil


SOURCE_FILE_FOLD_PATH = '/data/tmp/Oxyry/task/'
DEST_FILE_FOLD_PATH = '/data/tmp/Oxyry/taskOxyry/'

def get_log_path_dict():
  for root, dirs, files in os.walk(SOURCE_FILE_FOLD_PATH):
    log_path_dict = dict()
    for file in files:
      if file.endswith('.py'):
        log_path_dict[file] = os.path.join(root,file)
    return log_path_dict

# 删除文件夹
if os.path.isdir(DEST_FILE_FOLD_PATH):
  shutil.rmtree(DEST_FILE_FOLD_PATH)

# 创建文件夹
os.mkdir(DEST_FILE_FOLD_PATH)


files = get_log_path_dict()

filesLen = len (files)
print (filesLen , "个文件开始混淆！")
print ("")

count = 0
for key, value in files.items():
  f = open(value)
  lines = f.read()
  f.close()

  data = {
  'append_source': False,
  'preserve': "", # Blank, NQueens, Dancing Links, Classes, Module with __all__, Module without __all__, Function Arguments
  'remove_docstrings': True,
  'rename_default_parameters': False,
  'rename_nondefault_parameters': True,
  'source': lines
  }

  # https://pyob.oxyry.com/
  ## headers中添加上content-type这个参数，指定为json格式
  headers = {'content-encoding': 'gzip', 'Content-Type': 'application/json'}

  ## post的时候，将data字典形式的参数用json包转换成json格式。
  response = requests.post(url='https://pyob.oxyry.com/obfuscate', headers=headers, data=json.dumps(data))
  if 200 != response.status_code:
    print (key, 'Obfuscator Failed:', response.status_code)
    continue
  else:
    count = count + 1
    print (key, 'Obfuscator Success')

  dest = json.loads(response.text)['dest']
  f = open(DEST_FILE_FOLD_PATH + key, 'w+')
  f.write(dest)
  f.close()

print("")
print ("混淆结束! 成功%d个,失败%d个" % (count, filesLen - count))
