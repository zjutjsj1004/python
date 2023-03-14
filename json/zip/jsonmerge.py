import os
import json
from ruamel import yaml


def MergeCoco(listTO, listFrom):
    for valFrom in listFrom:
        find = False
        for valTo in listTO:
            if valFrom['id'] == valTo['id']:
                find = True
        if not find:
            listTO.append(valFrom)
    return listTO



def AnalysisJson(coco_list):
    for dir in coco_list:
        mergejson = os.path.join(dir, "merge.json")
        if os.path.isfile(mergejson):
            print("remove {0}".format(mergejson))
            os.remove(mergejson)
        mergeData = {}
        mergeData["images"] = []
        mergeData["categories"] = []
        mergeData["annotations"] = []
        for _,_,filesTmp in os.walk(os.path.join(dir)): 
            for fileTmp in filesTmp:  #遍历当前路径下所有非目录子文件
                if os.path.splitext(fileTmp)[1] == '.json' and fileTmp != "merge.json": #只获取Json格式的文件
                    with open(os.path.join(dir, fileTmp), encoding="utf-8", mode='r') as f:
                        # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
                        temp = json.load(f)      #json格式数据转换为python字典类型
                        #mergeData["images"].extend(temp["images"])
                        #mergeData["categories"].extend(temp["categories"])
                        #mergeData["annotations"].extend(temp["annotations"])
                        MergeCoco(mergeData["images"], temp["images"])
                        MergeCoco(mergeData["categories"], temp["categories"])
                        MergeCoco(mergeData["annotations"], temp["annotations"])
            
            if len(mergeData["images"]) == 0:
                print("error")
            else:
                with open(mergejson, "w") as outfile: 
                    json.dump(mergeData, outfile)

def Check(coco_list):
    for dir in coco_list:
        mergejson = os.path.join(dir, "merge.json")
        if not os.path.isfile(mergejson):
            print("file {0} not exists".format(mergejson))

def load_yaml(yaml_path):
    config_dict = {}
    with open(yaml_path, 'r', encoding='utf-8') as config_file:
        config_dict = yaml.load(config_file.read(), Loader=yaml.RoundTripLoader)
    return config_dict

def save_yaml(yaml_path, config_dict):
    with open(yaml_path, 'w', encoding='utf-8') as config_file:
        yaml.dump(config_dict, config_file, Dumper=yaml.RoundTripDumper)


def ModifyTrainYaml(coco_list):
    yamlPath = '/data/gocpplua/python/json/zip/train_instance.yaml'
    name = []
    train = []
    ann_json = []
    img_root = []
    for dir in coco_list:
        dirname = os.path.basename(dir)
        name.append(dirname)
        train.append(dirname)
        ann_json.append(os.path.join(dir, "merge.json"))
        img_root.append(os.path.join(dir, "images"))

    
    data = load_yaml(yamlPath)
    print(data['DATASET']['name'])
    print(data['DATASET']['train'])
    data['DATASET']['name'] = name
    data['DATASET']['train'] = train
    data['DATASET']['ann_json'] = ann_json
    data['DATASET']['img_root'] = img_root
    save_yaml(yamlPath, data)
    return

if __name__ == '__main__':
    data = load_yaml('./cabinet_inference.yaml')
    data['TEST']['HUMAN_MODEL_NAME'] = "xxx"
    save_yaml('./cabinet_inference.yaml', data)

    file_path = "/data/gocpplua/python/json/zip"
    coco_list = []
    for root,dirs,files in os.walk(file_path):  # 遍历file_path下所有的子目录及文件
        for dir in dirs:
            for rootTmp,dirsTmp,_ in os.walk(os.path.join(root, dir)): 
                coco_list.append(os.path.join(rootTmp))

    AnalysisJson(coco_list)
    Check(coco_list)
    ModifyTrainYaml(coco_list)



