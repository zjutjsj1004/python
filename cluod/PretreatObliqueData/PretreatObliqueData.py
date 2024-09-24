import os
import shutil

def rename_and_stop_recursive(folder_path, found_cam_folders=False):
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    camera_names = ['x', 'y', 'h', 'z', 'q']

    # Check if the subfolders are 'x', 'y', 'h', 'z', 'q'
    if set(subfolders) == set(camera_names):
        found_cam_folders = True

        # Rename the subfolders
        for i, subfolder in enumerate(camera_names):
            old_path = os.path.join(folder_path, subfolder)
            new_name = f"cam{i}"
            new_path = os.path.join(folder_path, new_name)
            print(old_path, new_path)
            os.rename(old_path, new_path)
        
        # Stop recursive traversal
        return found_cam_folders

    # Continue recursive traversal for each subfolder
    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        found_cam_folders = rename_and_stop_recursive(subfolder_path, found_cam_folders)

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
print(ret)

