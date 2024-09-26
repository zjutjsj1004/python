# pip install minio
import os
import re
from minio import Minio

# 替换为您自己的 MinIO 服务器设置
MINIO_ENDPOINT = "http://localhost:9000"
MINIO_ACCESS_KEY = "xxxxxx"
MINIO_SECRET_KEY = "xxxxxx"
BUCKET_NAME = "test"
PREFIX = "716"
EXCLUDE_DIR = "output"
REGEX_PATTERN = "video-onex2/video/.*\.insv"

def list_objects(minio_client, bucket_name, prefix, exclude_dir, regex_pattern):
    found_files = []

    def _is_excluded(object_path):
        return exclude_dir in object_path

    for obj in minio_client.list_objects(bucket_name, prefix=prefix, recursive=True):
        if not _is_excluded(obj.object_name) and re.match(regex_pattern, obj.object_name):
            found_files.append(obj.object_name)

    return found_files

# 创建 MinIO 客户端连接
minio_client = Minio(MINIO_ENDPOINT,
                     access_key=MINIO_ACCESS_KEY,
                     secret_key=MINIO_SECRET_KEY,
                     secure=False)

# 执行查找操作并打印结果
found_files = list_objects(minio_client, BUCKET_NAME, PREFIX, EXCLUDE_DIR, REGEX_PATTERN)
for file in found_files:
    print(file)