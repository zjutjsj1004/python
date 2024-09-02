import os
from datetime import datetime
import re

INSV_SUFFIX = ".insv"
# 获取固定文件夹下的 .insv 文件列表（不递归查询）
def get_insv_files(directory):
    rename_insv_files = []
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.lower().endswith(INSV_SUFFIX):

            # 使用正则表达式匹配并提取三个部分
            match = re.match(r'(.*VID_[0-9]{8}_[0-9]{6})(_[0-9]{2}_)(.+)',file)
            if match:
                continue
            else:
                rename_insv_files.append(file_path)
    
    return rename_insv_files

# 根据修改时间进行分组（每组最多2个文件）
def group_insv_files_by_mod_time(files, time_difference=600000000):
    grouped_files = []
    
    while files:
        group = [files.pop(0)]
        file_mtime = os.path.getmtime(group[0])
        
        for file in files[:]:
            if len(group) < 2 and abs(os.path.getmtime(file) - file_mtime) <= time_difference:
                group.append(file)
                files.remove(file)
                break  # 每组最多2个文件，找到第二个文件后停止
        
        grouped_files.append(group)
    
    return grouped_files

def rename_grouped_files(grouped_files):
    for group in grouped_files:
        # 获取 group 长度
        group_len = len(group)
        if group_len != 2:
            print(f"Group{group} has {group_len} files, expected 2.")
            return False
        
        # 根据第一个文件的修改时间，进行重命名
        mod_time = os.path.getmtime(group[0])
        # 将修改时间转换为 datetime 对象
        mod_time_dt = datetime.fromtimestamp(mod_time)

        # 格式化修改时间为所需的字符串格式
        formatted_time = mod_time_dt.strftime("VID_%Y%m%d_%H%M%S")

        # 获取哪一个文件是 00, 哪一个是 10， 这里先假设第一个是00
        # 假设你有一些自定义后缀，如 _10_020
        custom_suffix0 = "_{0}_020".format("00")
        custom_suffix1 = "_{0}_020".format("10")
        # 最终的文件名
        formatted_filename0 = formatted_time + custom_suffix0 + INSV_SUFFIX
        formatted_filename1 = formatted_time + custom_suffix1 + INSV_SUFFIX
        # 使用下标，rename 前后文件名
        os.rename(group[0], os.path.join(os.path.dirname(group[0]), formatted_filename0))
        os.rename(group[1], os.path.join(os.path.dirname(group[1]), formatted_filename1))
        print(f"Group[0] {group[0]} -> {formatted_filename0}")
        print(f"Group[1] {group[1]} -> {formatted_filename1}")

    return True

# 打印分组结果
def print_grouped_files(grouped_files):
    for i, group in enumerate(grouped_files, 1):
        print(f"Group {i}:")
        for file in group:
            mod_time = datetime.fromtimestamp(os.path.getmtime(file))
            print(f"  {file} (Last Modified: {mod_time})")
        print()


if __name__ == "__main__":
    #directory = "/data/scp/dt/kinect_4k/chenqi"
    #directory = "/data/scp/dt/tag/insv_tag/video"
    #directory = "/data/scp/dt/notag/onex2_no_qr/video"  # 目标目录
    directory = "/data/scp/liantong/RGBD"
    files = get_insv_files(directory)
    if len(files) == 0:
        print("No .insv files need rename")
        exit(1)
    else:
        print(f"Found {len(files)} .insv files({files})  need rename")

    grouped_files = group_insv_files_by_mod_time(files)
    rename_grouped_files(grouped_files)
    #print_grouped_files(grouped_files)
