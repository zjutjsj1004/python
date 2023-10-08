from ruamel import yaml
import os
import numpy as np


def load_yaml(yaml_path):
    config_dict = {}
    if os.path.exists(yaml_path):
        with open(yaml_path, 'r', encoding='utf-8') as config_file:
            config_dict = yaml.load(config_file.read(), Loader=yaml.RoundTripLoader)
            if config_dict == None or len(config_dict) == 0:
                print("xxxxxxxxxxxxxxxxxxxxxxxx")
                return {}
    return config_dict

addLine = np.array([0,0,0,1])


ned = []
f = open('ned_to_ecef.txt', "r", encoding='utf-8')

lines = f.readlines()
f.close()

if len(lines) != 3:
    exit(0)

ned.append(lines[0].rstrip().split(" "))
ned.append(lines[1].rstrip().split(" "))
ned.append(lines[2].rstrip().split(" "))


ned = np.matrix(ned)

nedT = ned.astype(np.float)

Tn2e = np.r_[nedT,[addLine]]


T1 = None
data = load_yaml('./1.yaml')
if data.get("transMatrix", None):
    transMatrix =   data["transMatrix"]  
    print(transMatrix)
    if transMatrix.get("data", None):
        transMatrixData = transMatrix["data"]  
        transMatrixDataT = np.array(transMatrixData).reshape(3,4)
        print(transMatrixDataT)
        T1 = np.r_[transMatrixDataT,[addLine]]
    else:
        exit(0)
else:
     exit(0)


rotT = np.matrix([-1,0,0,0, 0,0,1,0, 0,1,0,0, 0,0,0,1]).reshape(4,4)

print('-------- original data ------------')

print("T1:", T1)
print("Tn2e:", Tn2e)
print("rotT:", rotT)

print('-------- temporary data ------------')
A = np.matrix(rotT * T1)
print("rotT * T1:", A)


print('-------- result------------')
result = Tn2e * A.I

# result = Tn2e * np.linalg.pinv(rotT * T1)

print(result)

print('-------- nedTransT------------')
nedTransT = np.delete(result, 3, 0)
print(nedTransT)


print('-------- write trans_ned_to_ecef.txt------------')
np.savetxt("trans_ned_to_ecef.txt", nedTransT,fmt='%f',delimiter=' ')

