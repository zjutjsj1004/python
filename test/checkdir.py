import os

def check_first_level_folders(folder_a, folder_b):
    # 获取文件夹A和B的第一层文件夹名
    folders_a = [name for name in os.listdir(folder_a) if os.path.isdir(os.path.join(folder_a, name))]
    folders_b = [name for name in os.listdir(folder_b) if os.path.isdir(os.path.join(folder_b, name))]

    # 检查第一层文件夹名是否一致
    if set(folders_a) == set(folders_b):
        print("文件夹A和B的第一层文件夹名一致")
    else:
        print("文件夹A和B的第一层文件夹名不一致")

# 例子
folder_path_a = '/data/gocpplua/python/test'
folder_path_b = '/data/gocpplua/python/'

check_first_level_folders(folder_path_a, folder_path_b)
