# 获取文件夹下文件，并且排序
import os
def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        print ('----------------------')
        print(maindir, subdir)
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if apath.endswith('mkv'):
                base_name=int(os.path.splitext(filename)[0])
                print(apath, base_name, maindir)
                for cmaindir, csubdir, cfile_name_list in os.walk(maindir):
                    print(cfile_name_list)
                    ccname = ""
                    for cfilename in cfile_name_list:
                        cpath = os.path.join(cmaindir, cfilename)
                        if cpath.endswith('mp4') or cpath.endswith('invs'):
                            ccname = cpath
                    result.append({"index": base_name, "txttfilepath": apath, "dirpath": maindir, "ccfilepath": ccname})
    resultSort = sorted(result, key = lambda i: i['index'])
    return resultSort


result = all_path('/data/gocpplua/python/python网络数据采集/实践/1通过QQSMTP发送邮件/')
print ('result:')
for index in range(len(result)):
   print (' %s' % result[index])


