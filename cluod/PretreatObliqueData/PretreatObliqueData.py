import os
import shutil
keep_folders =  ['cam0', 'cam1', 'cam2', 'cam3', 'cam4']
def rename_and_stop_recursive(folder_path, found_cam_folders=False):
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    print("subfolders:", subfolders)
    camera_names = ['x', 'y', 'h', 'z', 'q']

    # Check if the subfolders are 'x', 'y', 'h', 'z', 'q'
    if set(camera_names).issubset(set(subfolders)):
        found_cam_folders = True

        # Rename the subfolders
        for i, subfolder in enumerate(camera_names):
            old_path = os.path.join(folder_path, subfolder)
            rel_path = os.path.relpath(folder_path, destination_folder_path)
            print("rel_path:", rel_path)
            new_name = 'cam{0}'.format(i)
            new_path = os.path.normpath(os.path.join(destination_folder_path, new_name, rel_path)) # 去掉不必要的 . 或 ..
            print("old:", old_path, " new:", new_path)
            # 获取 new_path 的目录部分
            new_dir = os.path.dirname(new_path)
            # 如果目录不存在，则创建
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            os.rename(old_path, new_path)
            
            # 移除元素
            subfolders.remove(subfolder)

    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        found_cam_folders = rename_and_stop_recursive(
            subfolder_path, found_cam_folders)

    return found_cam_folders

def copy_folder(source_folder, destination_folder):
    try:
        # 如果目标文件夹存在，先删除
        if os.path.exists(destination_folder):
            shutil.rmtree(destination_folder)
        
        shutil.copytree(source_folder, destination_folder)
        print(f"Folder '{source_folder}' copied to '{destination_folder}' successfully.")
    except Exception as e:
        print(f"Error: {e}")



# 指定源文件夹和目标文件夹路径
source_folder_path = '/data/gocpplua/python/cluod/PretreatObliqueData/source/'
destination_folder_path = '/data/gocpplua/python/cluod/PretreatObliqueData/dst/'

# 调用函数进行复制
copy_folder(source_folder_path, destination_folder_path)

# Specify the root folder
root_folder = destination_folder_path
# Start the recursive traversal
ret = rename_and_stop_recursive(root_folder)

# 遍历 destination_folder_path 所有文件和文件夹（不嵌套）
# 如果 不是 cam0, cam1, cam2, cam3, cam4 ,那么就删除
# 遍历目标文件夹下的所有文件和文件夹（不递归）
for item in os.listdir(destination_folder_path):
    item_path = os.path.join(destination_folder_path, item)
    
    # 如果是文件夹且不在保留列表中，删除文件夹
    if os.path.isdir(item_path) and item not in keep_folders:
        print(f"Deleting folder: {item_path}")
        shutil.rmtree(item_path)

    # 如果是文件，则直接删除
    elif os.path.isfile(item_path):
        print(f"Deleting file: {item_path}")
        os.remove(item_path)

print(keep_folders[0])
print("ret:", ret)

