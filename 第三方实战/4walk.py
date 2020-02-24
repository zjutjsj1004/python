#开发环境说明：基于Python3开发
#功能说明:此脚本实现目标文件夹下面，文件夹和文件的一键重命名功能。脚本执行后，默认在根文件夹(假设根文件夹名字为rootPath)同一目录生成rootPathGen。
#重命名规则: 
# 1、目前重命名后的文件名和文件夹名字是原文件夹名和文件名的反转。
# 2、保留原后缀，不过如果后缀是plist,也进行反转为:tsilp

#参数说明: 
# 1、rootPath:进行重命名的文件根路径
# 2、spriteFramesPath:plist处理程序路径
# 3、mapName 重命名前后文件夹名和文件名记录表(一般不允许更改)
# 4、EXCLUDEDIRLIST:目标文件夹下需要过滤的文件夹名称
# 5、EXCULUEFILELIST:目标文件夹下需要过滤的文件名称

#特殊说明:文件夹名或者文件名不能使用等号(=)

rootPath="E:\\Gitlab\\teen"
#rootPath="C:\\Users\\cq\\Desktop\\a"
spriteFramesPath="F:\\github\\python.git\\trunk\第三方实战"
mapName = "map.txt"
EXCLUDEDIRLIST=[".git", ".vscode"]
EXCULUEFILELIST=[mapName]

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

# 字符串特殊处理("\\"-> "/")
def SpecialThans(str):
    return str.replace("\\", "/")

print("============开始运行============")
startTime = time.clock()
gDict = {}
gDictFile = {}
errorCount = 0

pathinfo=os.path.split(rootPath)
genPath = os.path.join(pathinfo[0], pathinfo[1]+"Gen")
gDict[rootPath] = genPath
print("rootPath", gDict[rootPath])
clear_dir(genPath)

#生成文件
f=open(os.path.join(genPath, mapName), "w",encoding="utf-8")

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
            bPlist = False
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
                    if fileSuffix == "plist":
                        fileSuffix = fileSuffix[::-1]
                        bPlist = True
                    fileFullPathAfter = os.path.join(gDict[dirpath],  fun_formatFileName(filePrefix) + "." +fileSuffix)
                    
                    
                else:
                    fileFullPathAfter = os.path.join(gDict[dirpath], filename)
                print(fileFullPathBefore, " ---> ", fileFullPathAfter)
                
                if bPlist:
                    ret = os.system(os.path.join(spriteFramesPath, "spriteframes") + " " + fileFullPathBefore + " " + fileFullPathAfter)
                    if 0 != ret:
                        print("[Error]spriteframes 执行失败!", "Path=", fileFullPathBefore)
                        errorCount = errorCount + 1
                        f.writelines(["[Error]spriteframes 执行失败!", "Path=", fileFullPathBefore, "\n"])
                else:
                    if os.path.exists(fileFullPathAfter):
                        errorCount = errorCount + 1
                        print("[Error]文件已经存在!", "Path=", fileFullPathAfter, "\n")
                        f.writelines(["[Error]文件已经存在!", "Path=", fileFullPathAfter, "\n"])
                        continue
                    shutil.copy(fileFullPathBefore, fileFullPathAfter)
                gDictFile[fileFullPathBefore] = fileFullPathAfter

print("==========gDict==============")
print("filename:", f.name)
f.writelines(["[map]", "\n"])
for key, value in gDictFile.items():
    f.writelines([SpecialThans(key), ":", SpecialThans(value), "\n"])
    if key.find("=") != -1:
        print("[Error]等号不能存在于文件夹名字或者文件名字，请重命名!!  ", key, "--->", value)
        f.writelines(["[Error]等号不能存在于文件夹名字或者文件名字，请重命名!!", key, "--->", value, "\n"])
        errorCount = errorCount + 1
        break
    print(key, "--->", value)


costTime = time.clock() - startTime
if errorCount == 0:
    print("重命名文件和文件夹请查看下述路径:", genPath)
    print("[Success]执行成功!! 耗时:", str(costTime))
else:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    f.writelines(["[Error]执行失败!!", "共失败:", str(errorCount), "次。", "耗时:", str(costTime), "\n"])
    print("[Error]执行失败!!", "共失败:",errorCount, "次.", "详细错误请查看文件:", mapName," 耗时:", str(costTime))

f.flush()
f.close()
