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
#data['mvs_yaml_param']['test'] = 1

if not data['sfm_yaml_param']: # 不添加这个判定会报错: TypeError: 'NoneType' object does not support item assignment
    data['sfm_yaml_param'] = {}
data['sfm_yaml_param']['test'] = 1

data['obj_format'] = ['ply', 'ply1']


print(data)
save_yaml("./a.yaml", data)

data_mvs = load_yaml('./mvs.yaml')
param_dict = data.get('mvs_yaml_param')
size = param_dict.get('max_image_size')
print('max_image_size:', size)
for (key, value) in param_dict.items():
    print(key, value)
    if key == "max_image_size":
        value = size
    
    data_mvs[key] = value

save_yaml("./b.yaml", data_mvs)

import subprocess

def popen_communicate_sys_cmd(cmd):
    proc = subprocess.Popen([cmd],
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdoutdata, stderrdata = proc.communicate()
    ret = proc.returncode
    if ret == 0:
        ret = [True, stdoutdata.decode('utf-8'), proc.pid, cmd]
    else:
        ret = [False, stderrdata.decode('utf-8'), proc.pid, cmd]
    return ret

ret = popen_communicate_sys_cmd('ls -l /usr/bin')
print(ret[1])