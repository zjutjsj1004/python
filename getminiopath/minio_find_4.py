import os
import re
import logging
import time
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
INCLUDE_DIR = ["video-onex2", "zip-onex2"] # output太大，进行排除

# 构建正则表达式
REGEX_PATTERN_INSV_FILES_VIDEO_INSV = rf".*/video-onex2/video/.*\.insv$"
REGEX_PATTERN_INSV_FILES_VIDEO_ZIP = rf".*/video-onex2/.*\.zip$"
REGEX_PATTERN_APP_FILES_ZIP = rf".*/zip-onex2/.*\.zip$"
REGEX_PATTERN = [REGEX_PATTERN_INSV_FILES_VIDEO_INSV, REGEX_PATTERN_INSV_FILES_VIDEO_ZIP, REGEX_PATTERN_APP_FILES_ZIP]

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


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

    objects_leval1 = minio_client.list_objects(bucket_name, current_prefix, recursive=False)
    for obj_leval1 in objects_leval1:
        current_level1 = obj_leval1.object_name
        object_parts1 = current_level1.split('/')
        if is_integer(object_parts1[0]):
            objects_leval2 = minio_client.list_objects(bucket_name, current_level1, recursive=False) 
            for obj_leval2 in objects_leval2:
                current_level2 = obj_leval2.object_name
                object_parts2 = current_level2.split('/')
                if is_integer(object_parts2[1]):
                    objects_leval3 = minio_client.list_objects(bucket_name, current_level2, recursive=False) 
                    for obj_leval3 in objects_leval3:
                        current_level3 = obj_leval3.object_name
                        object_parts3 = current_level3.split('/')
                        if len(object_parts3) > 2 and object_parts3[2]  not in (exclude_dir) and object_parts3[2] in (INCLUDE_DIR):
                            logger.info(f"Added object: {current_level3}")
                            result_list.append(current_level3)
            
def list_objects(minio_client, bucket_name, prefix, exclude_dir):
    result_list = []
    logger.info("Starting traverse_objects operation...")
    traverse_objects(minio_client, bucket_name, 0, prefix, exclude_dir, result_list)
    logger.info(f"Stopping traverse_objects operation...{len(result_list)} ")

    # 层级
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

    found_files = []
    count = 1
    for object_name in result_list:
        logger.info(f"operation: {object_name}, {count} / {len(result_list)} ")
        for objFiltered in minio_client.list_objects(bucket_name, prefix=object_name, recursive=True):
            for pattern in REGEX_PATTERN:
                if re.match(pattern, objFiltered.object_name):
                    found_files.append(objFiltered.object_name)
                    break
        count += 1

    return found_files


def main():
    start_time = time.time()  # 记录脚本开始执行的时间

    # 创建 MinIO 客户端连接
    minio_client = Minio(MINIO_ENDPOINT,
                        access_key=MINIO_ACCESS_KEY,
                        secret_key=MINIO_SECRET_KEY,
                        secure=False)

    # 执行查找操作并写入文件
    logger.info("Starting the search operation...")
    found_files = list_objects(minio_client, BUCKET_NAME, PREFIX, EXCLUDE_DIR)
    logger.info(f"Found {len(found_files)} files.")

    with open('output_file.txt', 'w') as f:
        for file in found_files:
            f.write(file+'\n')

    end_time = time.time()  # 记录脚本结束执行的时间
    execution_time = end_time - start_time  # 计算执行时间
    logger.info(f"operation {execution_time:.2f} seconds.")

if __name__ == "__main__":
    main()
# 备注: 
# 版本1：
'''
prd 环境一共执行了186分钟  匹配了 1390, 但是其中只有1269是对的

优化版本 在PRD得到 1224 个文件 2分钟,   在 DT测试环境使用 3秒 59个文件
'''