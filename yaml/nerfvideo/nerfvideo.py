from ruamel import yaml
import os
def load_yaml(yaml_path):
    config_dict = {}
    if os.path.exists(yaml_path):
        with open(yaml_path, 'r', encoding='utf-8') as config_file:
            config_dict = yaml.load(config_file.read(), Loader=yaml.RoundTripLoader)
            if config_dict == None or len(config_dict) == 0:
                print("xxxxxxxxxxxxxxxxxxxxxxxx")
                return {}
    return config_dict

def save_yaml(yaml_path, config_dict):
    with open(yaml_path, 'w', encoding='utf-8') as config_file:
        yaml.dump(config_dict, config_file, Dumper=yaml.RoundTripDumper)

files = [
"0601.yaml",  "0801.yaml",     "calibration.yaml",
"0703.yaml",  "0811.yaml",     "kongkeng.yaml",
"0705.yaml",  "0817.yaml",     "snapshot-1.3.0.1-aitower-large-0.5-clean2.yaml",
"0712.yaml",  "1000000.yaml",
]

for v in files:
    filepath = './out/{0}'.format(v)
    print("filepath:",filepath)

    src = load_yaml(filepath)
    dest = {}
    ids = []

    for k, v in src.items():
        if isinstance(v, dict):
            if v.get("image", None):
                img_name = v["image"]
                if img_name.find("_0.") == -1 and img_name.find("_2.") == -1 and \
                    img_name.find("_3.") == -1 and img_name.find("_4.") == -1 and \
                    img_name.find("_5.") == -1:
                    id = int(k.split("_")[-1])
                    ids.append(id)

    ids.sort()
    pos_id = 0
    for id in ids:
        key = 'pose_' + str(id)
        # 获取文件所在目录和完整文件名
        dir_name, full_file_name = os.path.split(src[key]['image'])
        new_name = full_file_name.replace("_", "")
        new_key = 'pose_' + str(pos_id)
        dest[new_key] = src[key]
        dest[new_key]['image'] = os.path.join(dir_name, new_name)
        pos_id += 1
    dest['num_poses'] = len(ids)
    save_yaml(filepath, dest)
