import re
import os
video_list = ["d:/VID_20220613_154650_00_002.insv", "d:/VID_20220613_154650_10_002.insv",
                "1_VID_20220613_154650_00_002_1.insv", "1_VID_20220613_154650_10_002_1.insv", 
              "2_VID_20220621_100503_00_004_2.insv", "2_VID_20220621_100503_10_004_2.insv", 
              "3_33_VID_20220621_100503_00_004_2_22.insv", "3_33_VID_20220621_100503_10_004_2_22.insv"]
device_list = {}

for i in range(len(video_list)):
    print("---------------")

    video_dir, video_name= os.path.split(video_list[i])
    #video_name = video_list[i].split('/')[-1]
    print( video_dir, " xx ", video_name)

    #video_name = video_list[i].split('/')[-1].split('.')[0]

    # 使用正则表达式匹配并提取三个部分
    match = re.match(r'(.*VID_[0-9]{8}_[0-9]{6})(_[0-9]{2}_)(.+)', video_name)
    if match:
        first_part = match.group(1)
        second_part = match.group(2)
        third_part = match.group(3)

        device_tag = os.path.join(video_dir, first_part)
        device_list[device_tag] = third_part
        print(f"{device_tag},{second_part},{third_part}")

print("---------------")
for device_tag in device_list:
    left_video = device_tag + "_00_" +  device_list[device_tag]
    right_video = device_tag + "_10_" +  device_list[device_tag]
    print(left_video, "  ", right_video)

