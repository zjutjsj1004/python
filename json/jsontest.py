import os
import json
print(111)
print(json.__file__)
print(json.__path__)
print(222)
# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print("deviceType1")
device_json = '/data/gocpplua/python/json/device.json'
with open(device_json, 'r') as f:
    data = json.load(f)
    device_type = data.get('deviceType', 'Insta360 ONE X2')
    print(device_type)

print("deviceType2")
data = json.loads(device_json)
device_type = data.get('deviceType', 'Insta360 ONE X2')
print(device_type)

# "images", "categories,"annotations"
with open('/data/gocpplua/python/json/view_00_00_01.json', 'r') as f:
    data1 = json.load(f)

with open('/data/gocpplua/python/json/view_00_00_04.json', 'r') as f:
    data2 = json.load(f)

data1["images"].append(data2["images"])
data1["categories"].append(data2["categories"])
data1["annotations"].append(data2["annotations"])

with open("merge.json", "w") as outfile: 
    json.dump(data1, outfile)