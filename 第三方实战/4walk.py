#conding=utf8  
import os 
import shutil
def fun_formatDirPath(dirPath):
    return dirPath[::-1]

def fun_formatFileName(fileName):
    return fileName[::-1]

def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)



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

gDict = {}
gDictFile = {}
#currPath="C:\\Users\\cq\\Desktop\\slot\\teen_an_Facebook-armeabi-release\\assets\\teen"
currPath="C:\\Users\\cq\\Desktop\\a"
pathinfo=os.path.split(currPath)
genPath = os.path.join(pathinfo[0], pathinfo[1]+"Gen")
gDict[currPath] = genPath
print("curr", gDict[currPath])
del_file(genPath)

print("==========startDir==============")
g = os.walk(currPath) #walk不包括currPath下面的文件
for dirpath,dirnames,filenames in g:
    print(dirpath)
    for dirname in dirnames:
        print(os.path.join(dirpath,dirname), " ---->", genNewDir(os.path.join(dirpath,dirname)))
    print("=================================")

g = os.walk(currPath) #walk不包括currPath下面的文件
print("==========startFile==============")
for dirpath,dirnames,filenames in g:
    for filename in filenames:
        filePrefix = filename.split('.')[0]
        fileSuffix = filename.split('.')[1]
        fileFullPathBefore = os.path.join(dirpath,filename)
        fileFullPathAfter = os.path.join(gDict[dirpath],  fun_formatFileName(filePrefix) + "." +fileSuffix)
        print(fileFullPathBefore, " ---> ", fileFullPathAfter)
        shutil.copy(fileFullPathBefore, fileFullPathAfter)
        gDictFile[fileFullPathBefore] = fileFullPathAfter
        #os.renames(os.path.join(dirpath,filename), os.path.join(dirpath,  formatDirName + "." +fileSuffix))

print("==========gDict==============")
f=open(os.path.join(genPath, 'map.txt'), "w",encoding="utf-8")
print("filename:", f.name)
#for key, value in gDict.items():
    #f.writelines([key.replace("\\", "/"), ",", value.replace("\\", "/"), "\n"])
for key, value in gDictFile.items():
    f.writelines([key.replace("\\", "/"), ",", value.replace("\\", "/"), "\n"])
f.close()