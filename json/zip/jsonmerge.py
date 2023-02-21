import os
import json

def AnalysisJson():
    file_path = "/data/gocpplua/python/json/zip/"
    for root,dirs,files in os.walk(file_path):  # 遍历file_path下所有的子目录及文件
        for dir in dirs:
            for rootTmp,dirsTmp,filesTmp in os.walk(os.path.join(root, dir)): 
                mergejson = os.path.join(rootTmp, "merge.json")
                if os.path.isfile(mergejson):
                    print("remove {0}".format(mergejson))
                    os.remove(mergejson)
                mergeData = {}
                mergeData["images"] = []
                mergeData["categories"] = []
                mergeData["annotations"] = []
                for fileTmp in filesTmp:  #遍历当前路径下所有非目录子文件
                    if os.path.splitext(fileTmp)[1] == '.json' and fileTmp != "merge.json": #只获取Json格式的文件
                        with open(os.path.join(rootTmp, fileTmp), encoding="utf-8", mode='r') as f:
                            # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
                            temp = json.load(f)      #json格式数据转换为python字典类型
                            mergeData["images"].extend(temp["images"])
                            mergeData["categories"].extend(temp["categories"])
                            mergeData["annotations"].extend(temp["annotations"])
                

                with open(mergejson, "w") as outfile: 
                    json.dump(mergeData, outfile)


if __name__ == '__main__':
    AnalysisJson()


