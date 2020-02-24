#开发环境说明：基于Python3开发
#功能说明:此脚本实现目标文件夹下面，文件夹和文件的一键重命名功能。 目前重命名后的文件名和文件夹名字是原文件夹名和文件名的反转。
#        脚本执行后，默认在根文件夹(假设根文件夹名字为rootPath)同一目录生成rootPathGen。
#使用说明: 设置下面三个参数:
# 1、rootPath 进行重命名的文件根路径
# 2、EXCLUDEDIRLIST 目标文件夹下需要过滤的文件夹名称
# 3、EXCULUEFILELIST 目标文件夹下需要过滤的文件名称
rootPath="E:\\Gitlab\\teen"
EXCLUDEDIRLIST=[".git", ".vscode"]
EXCULUEFILELIST=[""]
#rootPath="C:\\Users\\cq\\Desktop\\a"
#conding=utf8  
import os 
import shutil
import time
import stat

#
def fun_formatDirPath(dirPath):
    return dirPath[::-1]

def fun_formatFileName(fileName):
    return fileName[::-1]

def rm_read_only(fn, tmp, info):
    if os.path.isfile(tmp):
         os.chmod(tmp, stat.S_IWRITE)
         os.remove(tmp)
    elif os.path.isdir(tmp):
        os.chmod(tmp, stat.S_IWRITE)
        shutil.rmtree(tmp, onerror=rm_read_only)

def clear_dir(filepath):
    """
    清空某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:无
    """
    if os.path.isdir(filepath):
        shutil.rmtree(filepath, onerror=rm_read_only)
    else:
        print("文件夹不存在,无需删除")

    if not os.path.exists(filepath):
        os.makedirs(filepath)

def getNewDir(oldDir):
    newDir = ""
    if oldDir not in gDict:
        keys = os.path.split(oldDir)
        while True:
            newDir = os.path.join(newDir, fun_formatDirPath(keys[1]))
            print(keys)
            if 0 != len(keys[0]) and keys[0] in gDict:
                newDir = os.path.join(gDict[keys[0]], newDir)
                break
            keys = os.path.split(keys[0])
    else:
        newDir = gDict[oldDir]
    return newDir

#生成新目录
def genNewDir(oldDir):
    #根据老的目录，获取新目录
    newDir = getNewDir(oldDir)
    if not os.path.exists(newDir):
        os.makedirs(newDir)
    gDict[oldDir] = newDir 
    return newDir

print("============开始运行============")
startTime = time.clock()
gDict = {}
gDictFile = {}

pathinfo=os.path.split(rootPath)
genPath = os.path.join(pathinfo[0], pathinfo[1]+"Gen")
gDict[rootPath] = genPath
print("rootPath", gDict[rootPath])
clear_dir(genPath)

print("==========文件夹扫描和生成新文件夹==============")
g = os.walk(rootPath) #walk不包括rootPath下面的文件
for dirpath,dirnames,filenames in g:
    bContinue = True
    for key in EXCLUDEDIRLIST:
        if dirpath.lower().find(key.lower()) != -1:
            bContinue = False
            break

    if bContinue:
        for dirname in dirnames:
            if dirname.lower() not in EXCLUDEDIRLIST:
                print(os.path.join(dirpath,dirname), " ---->", genNewDir(os.path.join(dirpath,dirname)))
        
g = os.walk(rootPath) #walk不包括rootPath下面的文件
print("==========文件扫描和生成新文件==============")
for dirpath,dirnames,filenames in g:
    bContinue = True
    for key in EXCLUDEDIRLIST:
        if dirpath.lower().find(key.lower()) != -1:
            bContinue = False
            break
    if bContinue:
        for filename in filenames:
            if filename not in EXCULUEFILELIST:
                #考虑文件是否会存在文件后缀
                splitFilename = filename.split('.')
                splitFilenameLen = len(splitFilename)
                fileFullPathBefore = os.path.join(dirpath,filename)
                fileFullPathAfter = os.path.join(gDict[dirpath], filename)
                if splitFilenameLen == 0:
                    fileFullPathAfter = os.path.join(gDict[dirpath], filename)
                elif splitFilenameLen == 1:
                    fileFullPathAfter = os.path.join(gDict[dirpath], fun_formatFileName(filename.split('.')[0]))
                elif splitFilenameLen == 2:
                    filePrefix = filename.split('.')[0]
                    fileSuffix = filename.split('.')[1]
                    fileFullPathAfter = os.path.join(gDict[dirpath],  fun_formatFileName(filePrefix) + "." +fileSuffix)
                else:
                    fileFullPathAfter = os.path.join(gDict[dirpath], filename)
                print(fileFullPathBefore, " ---> ", fileFullPathAfter)
                if os.path.exists(fileFullPathAfter):
                    print("文件夹不存在")
                    continue
                shutil.copy(fileFullPathBefore, fileFullPathAfter)
                gDictFile[fileFullPathBefore] = fileFullPathAfter
                #os.renames(os.path.join(dirpath,filename), os.path.join(dirpath,  formatDirName + "." +fileSuffix))

print("==========gDict==============")
f=open(os.path.join(genPath, 'map.txt'), "w",encoding="utf-8")
print("filename:", f.name)
for key, value in gDictFile.items():
    f.writelines([key.replace("\\", "/"), ",", value.replace("\\", "/"), "\n"])
    print(key, "--->", value)
f.close()

ret = os.system('F:\\gocpplua\\awesome-cpp\\CodeSegment\\Debug\\CodeSegment' + " 11111" + " 22222")
if 0 != ret:
    print("CodeSegment 执行失败!")
    pass

print("运行结束!! 耗时统计:", str(time.clock() - startTime))
print("重命名文件和文件夹请查看下述路径:", genPath)