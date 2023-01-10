from ruamel import yaml

def load_yaml(yaml_path):
    config_dict = {}
    with open(yaml_path, 'r', encoding='utf-8') as config_file:
        config_dict = yaml.load(config_file.read(), Loader=yaml.RoundTripLoader)
    return config_dict

def save_yaml(yaml_path, config_dict):
    with open(yaml_path, 'w', encoding='utf-8') as config_file:
        yaml.dump(config_dict, config_file, Dumper=yaml.RoundTripDumper)


data = load_yaml('./tools-config.yaml')
data['mvs_yaml_param']['test'] = 1

if not data['sfm_yaml_param']: # 不添加这个判定会报错: TypeError: 'NoneType' object does not support item assignment
    data['sfm_yaml_param'] = {}
data['sfm_yaml_param']['test'] = 1

data['obj_format'] = ['ply', 'ply1']


print(data)
save_yaml("./a.yaml", data)