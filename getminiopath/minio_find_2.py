import os
import re
from minio import Minio

# 替换为您自己的 MinIO 服务器设置
MINIO_ENDPOINT = "xxxxxx"
MINIO_ACCESS_KEY = "xxxxxx"
MINIO_SECRET_KEY = "xxxxxx"
BUCKET_NAME = "test"
PREFIX = ""
OUTPUT_DIR_LEVEL = 2 # 表示在{PREFIX}下第二层的目录。 例如: 当  PREFIX = ""，那么会得到 715/381/video-onex2/
EXCLUDE_DIR = "output" # output太大，进行排除

# 动态构建正则表达式
output_dir_levels = ''.join(['[^/]+'] * OUTPUT_DIR_LEVEL)
REGEX_PATTERN_INSV_FILES = rf"/{output_dir_levels}/video-onex2/video/.*\.insv$"

def traverse_objects(minio_client, bucket_name, current_level, current_prefix, exclude_dir, result_list):
    objects = minio_client.list_objects(bucket_name, current_prefix, recursive=False)
    
    for obj in objects:
        object_parts = obj.object_name.split('/')
        
        # 检查当前层级是否存在，防止索引越界
        if len(object_parts) <= current_level:
            continue
        
        # 如果当前层级小于目标层级或当前层级不是排除目录，则添加对象并继续遍历
        if (current_level < OUTPUT_DIR_LEVEL or object_parts[current_level] != exclude_dir) and \
           (current_level + 1 < len(object_parts) and object_parts[current_level + 1] != exclude_dir):
            result_list.append(obj)
            
            # 只有当当前层级低于最大可能层级时才递归进入下一层级
            if current_level < len(object_parts) - 1:
                next_prefix = "/".join(object_parts[:current_level + 2])
                traverse_objects(minio_client, bucket_name, current_level + 1, next_prefix, exclude_dir, result_list)

def list_non_output_objects(minio_client, bucket_name, prefix, exclude_dir):
    result_list = []
    traverse_objects(minio_client, bucket_name, 0, prefix, exclude_dir, result_list)

    # result_list 得到的是小于等于指定层级的数据
    '''
    716/ ['716', ''] 2
    716/383/ ['716', '383', ''] 3
    716/383/Unity/ ['716', '383', 'Unity', ''] 4
    716/383/Unity/Package/ ['716', '383', 'Unity', 'Package', ''] 5
    716/383/Unity/Package/CustomBackup/ ['716', '383', 'Unity', 'Package', 'CustomBackup', ''] 6
    716/383/Unity/Package/UnicomOutPut/ ['716', '383', 'Unity', 'Package', 'UnicomOutPut', ''] 6
    716/383/Unity/Package/UnityBackup/ ['716', '383', 'Unity', 'Package', 'UnityBackup', ''] 6
    716/383/video-onex2/ ['716', '383', 'video-onex2', ''] 4
    716/383/video-onex2/video/ ['716', '383', 'video-onex2', 'video', ''] 5
    '''
    filtered_result_list = []
    for obj in result_list:
        object_name_split = obj.object_name.split('/')
        if len(object_name_split) == 4:
            filtered_result_list.append(obj)

    return filtered_result_list


def list_objects_without_output(minio_client, bucket_name, prefix, exclude_dir, regex_pattern):
    non_output_objects = list_non_output_objects(minio_client, bucket_name, prefix, exclude_dir)
    found_files = []
    for obj in non_output_objects:
        # 需要过滤不同的层
        print(obj.object_name, obj.object_name.split('/'), len(obj.object_name.split('/')))
        if re.match(regex_pattern, obj.object_name[len(prefix):]):
            found_files.append(obj.object_name)

    return found_files

# 创建 MinIO 客户端连接
minio_client = Minio(MINIO_ENDPOINT,
                     access_key=MINIO_ACCESS_KEY,
                     secret_key=MINIO_SECRET_KEY,
                     secure=False)

# 执行查找操作并打印结果
found_files = list_objects_without_output(minio_client, BUCKET_NAME, PREFIX, EXCLUDE_DIR, REGEX_PATTERN_INSV_FILES)
for file in found_files:
    print(file)