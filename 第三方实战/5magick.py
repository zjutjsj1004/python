#使用说明:安装第三方工具ImageMagick后,正确填写下述参数后直接运行脚本即可。参数说明:
# 1、ImageMagickPath:magick.exe的路径
# 2、rootPath:需要修改Hash值的图片集的根路径

#开发环境说明：基于Python3开发 + ImageMagick(用于微压缩/Hash值修改)
# ImageMagick说明:
# 1、下载地址:https://imagemagick.org/script/download.php#windows
# 2、命令行处理: magick XXX/源文件.jpg  XXX/目标文件.png, eg:magick image.jpg image.png  -- 文件名不能有空格

ImageMagickPath="E:\\ImageMagick\\ImageMagick-7.0.9-Q16\\magick"
rootPath="E:\\Gitlab\\teen_client"


#conding=utf8  
import os 
import time

print("============开始运行============")
startTime = time.clock()

g = os.walk(rootPath) #walk不包括rootPath下面的文件
for dirpath,dirnames,filenames in g:
    for filename in filenames:
        #考虑文件是否会存在文件后缀
            splitFilename = filename.split('.')
            splitFilenameLen = len(splitFilename)
            if splitFilenameLen == 2:
                filePrefix = splitFilename[0]
                fileSuffix = splitFilename[1]
                if fileSuffix in ["png", "jpg"]:
                    fileFullPath = os.path.join(dirpath,filename)
                    transFullPath = fileFullPath
                    if transFullPath.find(" "):
                        # 发现空格就替换
                        transFullPath = transFullPath.replace(" ", "A")
                        os.rename(fileFullPath, transFullPath) # os.rename(src, dst)
                    ret = os.system(os.path.join(ImageMagickPath) + " " + transFullPath + " " + transFullPath)
                    if 0 != ret:
                        print("[Error]PNG文件转换失败!", "Path=", fileFullPath, "\n")
                        os.exit(1)
                    else:
                        os.rename(transFullPath, fileFullPath)
                    print("转换PNG:",fileFullPath,"成功!")
                    

costTime = time.clock() - startTime
print("[Success]执行成功!! 耗时:", str(costTime))

