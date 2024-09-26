import os
import re
import logging
from minio import Minio

# 设置日志配置
logging.basicConfig(filename='script.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# 替换为您自己的 MinIO 服务器设置
MINIO_ENDPOINT = "xxxxxx"
MINIO_ACCESS_KEY = "xxxxxx"
MINIO_SECRET_KEY = "xxxxxx"
BUCKET_NAME = "test"
PREFIX = ""
OUTPUT_DIR_LEVEL = 2 # 表示在{PREFIX}下第二层的目录。 例如: 当  PREFIX = ""，那么会得到 715/381/video-onex2/
EXCLUDE_DIR = ["output", "Unity", 'bigimage'] # output太大，进行排除
MAX_DEPTH=4

# 构建正则表达式
REGEX_PATTERN_INSV_FILES_VIDEO_INSV = rf".*/video-onex2/video/.*\.insv$"
REGEX_PATTERN_INSV_FILES_VIDEO_ZIP = rf".*/video-onex2/.*\.zip$"
REGEX_PATTERN_APP_FILES_ZIP = rf".*/zip-onex2/.*\.zip$"
REGEX_PATTERN = [REGEX_PATTERN_INSV_FILES_VIDEO_INSV, REGEX_PATTERN_INSV_FILES_VIDEO_ZIP, REGEX_PATTERN_APP_FILES_ZIP]




def traverse_objects(minio_client, bucket_name, current_level, current_prefix, exclude_dir, result_list):
    """
    遍历 MinIO 中的文件
    :param minio_client: MinIO 客户端
    :param bucket_name: MinIO 中的 bucket 名称
    :param current_level: 当前遍历的层级
    :param current_prefix: 当前遍历的前缀
    :param exclude_dir: 排除的目录
    :param result_list: 结果列表
    :return: None
    """
    logger.info(f"Traversing objects at prefix: {current_prefix}, level: {current_level}")

    objects = minio_client.list_objects(bucket_name, current_prefix, recursive=False)
    
    for obj in objects:
        object_parts = obj.object_name.split('/')
        
        # 检查当前层级是否存在，防止索引越界
        if len(object_parts) <= current_level or current_level >= MAX_DEPTH:
            continue
        
        # 如果当前层级小于目标层级或当前层级不是排除目录，则添加对象并继续遍历
        if (current_level < OUTPUT_DIR_LEVEL or object_parts[current_level] not in (exclude_dir)) and \
           (current_level + 1 < len(object_parts) and object_parts[current_level + 1]  not in (exclude_dir)):
            result_list.append(obj)
            
            # 只有当当前层级低于最大可能层级时才递归进入下一层级
            if current_level < len(object_parts) - 1:
                next_prefix = "/".join(object_parts[:current_level + 2])
                logger.info(f"Recursing into next level with prefix: {next_prefix}")
                traverse_objects(minio_client, bucket_name, current_level + 1, next_prefix, exclude_dir, result_list)

def list_non_output_objects(minio_client, bucket_name, prefix, exclude_dir):
    result_list = []
    logger.info("Starting traverse_objects operation...")
    traverse_objects(minio_client, bucket_name, 0, prefix, exclude_dir, result_list)
    logger.info("Stopping traverse_objects operation...")

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
            logger.debug(f"Added object: {obj.object_name}")
            filtered_result_list.append(obj)

    return filtered_result_list


def list_objects_without_output(minio_client, bucket_name, prefix, exclude_dir):
    non_output_objects = list_non_output_objects(minio_client, bucket_name, prefix, exclude_dir)
    found_files = []
    for obj in non_output_objects:
        # 需要过滤不同的层        
        for objFiltered in minio_client.list_objects(bucket_name, prefix=obj.object_name, recursive=True):
            for pattern in REGEX_PATTERN:
                if re.match(pattern, objFiltered.object_name):
                    found_files.append(objFiltered.object_name)
                    break

    return found_files

# 创建 MinIO 客户端连接
minio_client = Minio(MINIO_ENDPOINT,
                     access_key=MINIO_ACCESS_KEY,
                     secret_key=MINIO_SECRET_KEY,
                     secure=False)

# 执行查找操作并写入文件
logger.info("Starting the search operation...")
found_files = list_objects_without_output(minio_client, BUCKET_NAME, PREFIX, EXCLUDE_DIR)
logger.info(f"Found {len(found_files)} files.")

with open('output_file.txt', 'w') as f:
    for file in found_files:
        f.write(file+'\n')


# 备注: 
# 版本1：
'''
prd 环境一共执行了186分钟  匹配了 1390, 但是其中只有1269是对的
'''