from ruamel import yaml
import os
import numpy


def load_yaml(yaml_path):
    config_dict = {}
    if os.path.exists(yaml_path):
        with open(yaml_path, 'r', encoding='utf-8') as config_file:
            config_dict = yaml.load(config_file.read(), Loader=yaml.RoundTripLoader)
            if config_dict == None or len(config_dict) == 0:
                print("xxxxxxxxxxxxxxxxxxxxxxxx")
                return {}
    return config_dict

addLine = numpy.array([0,0,0,1])


ned = []
f = open('ned_to_ecef.txt', "r", encoding='utf-8')

lines = f.readlines()
f.close()

if len(lines) != 3:
    exit(0)

ned.append(lines[0].rstrip().split(" "))
ned.append(lines[1].rstrip().split(" "))
ned.append(lines[2].rstrip().split(" "))


ned = numpy.matrix(ned)

nedT = ned.astype(numpy.float)

Tn2e = numpy.r_[nedT,[addLine]]


T1 = None
data = load_yaml('./1.yaml')
if data.get("transMatrix", None):
    transMatrix =   data["transMatrix"]  
    print(transMatrix)
    if transMatrix.get("data", None):
        transMatrixData = transMatrix["data"]  
        transMatrixDataT = numpy.array(transMatrixData).reshape(3,4)
        print(transMatrixDataT)
        T1 = numpy.r_[transMatrixDataT,[addLine]]
    else:
        exit(0)
else:
     exit(0)


rotT = numpy.matrix([-1,0,0,0, 0,0,1,0, 0,1,0,0, 0,0,0,1]).reshape(4,4)

print('-------- original data ------------')

print("T1:", T1)
print("Tn2e:", Tn2e)
print("rotT:", rotT)

print('-------- temporary data ------------')
A = numpy.matrix(rotT * T1)
print("rotT * T1:", A)


print('-------- result------------')
result = Tn2e * A.I

# result = Tn2e * numpy.linalg.pinv(rotT * T1)

print(result)
