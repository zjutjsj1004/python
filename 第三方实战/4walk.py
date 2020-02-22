#conding=utf8  
import os 
import shutil
import time
import stat

def fun_formatDirPath(dirPath):
    #return dirPath
    return dirPath[::-1]

def fun_formatFileName(fileName):
    #return fileName
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
    :return:
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
#currPath="C:\\Users\\cq\\Desktop\\slot\\teen_an_Facebook-armeabi-release\\assets\\teen"
currPath="E:\\Gitlab\\teen"
#currPath="C:\\Users\\cq\\Desktop\\a"

EXCLUDEDIRLIST=[".git", ".vscode"]
EXCULUEFILELIST=["Node.csb"]

pathinfo=os.path.split(currPath)
genPath = os.path.join(pathinfo[0], pathinfo[1]+"Gen")
gDict[currPath] = genPath
print("curr", gDict[currPath])
clear_dir(genPath)

print("==========文件夹扫描和生成新文件夹==============")
g = os.walk(currPath) #walk不包括currPath下面的文件
for dirpath,dirnames,filenames in g:
    bContinue = True
    print(dirpath, type(EXCLUDEDIRLIST))
    for key in EXCLUDEDIRLIST:
        if dirpath.lower().find(key.lower()) != -1:
            bContinue = False
            break

    if bContinue:
        for dirname in dirnames:
            if dirname.lower() not in EXCLUDEDIRLIST:
                print(os.path.join(dirpath,dirname), " ---->", genNewDir(os.path.join(dirpath,dirname)))
        
g = os.walk(currPath) #walk不包括currPath下面的文件
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
    os.system('F:\\gocpplua\\awesome-cpp\\CodeSegment\\Debug\\CodeSegment' + " 11111" + " 22222")
f.close()

print("运行结束!! 耗时统计:", str(time.clock() - startTime))