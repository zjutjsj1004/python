import os

curr_dir = os.path.split(os.path.realpath(__file__))
print(curr_dir)

cloud_tools_txt = ""
for maindir, subdir, file_name_list in os.walk(curr_dir[0]):
    print ('----------------------')
    for filename in file_name_list:
        cloud_tools_txt = os.path.join(maindir, filename)
        if cloud_tools_txt.find('cloud-tools') != -1 and cloud_tools_txt.endswith('.txt'):
          print(cloud_tools_txt)
          break

if cloud_tools_txt == "":
  print("error: cloud_tools_txt is not exists")
  os._exit(1)

txt_fh = open(cloud_tools_txt)
lines_list = txt_fh.readlines()
txt_fh.close()
for i in range(len(lines_list)):
    line = lines_list[i]
    if line.find('fail') != -1:
      print("error:", line)
      os._exit(1)

os._exit(0)