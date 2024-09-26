
from minio import Minio
import datetime

# 替换为您自己的 MinIO 服务器设置
MINIO_ENDPOINT = "xxxxxx"
MINIO_ACCESS_KEY = "xxxxxx"
MINIO_SECRET_KEY = "xxxxxx"
BUCKET_NAME = "test"
OBJECT_KEYS = ['715/381/video-onex2/video/VID_20220627_143315_00_081.insv',
'715/382/video-onex2/video/VID_20220518_101504_00_064.insv',
'715/382/video-onex2/video/VID_20220518_101504_10_064.insv',
'715/382/video-onex2/video/VID_20220627_143315_10_081.insv']

# 创建 MinIO 客户端连接
minio_client = Minio(MINIO_ENDPOINT,
                     access_key=MINIO_ACCESS_KEY,
                     secret_key=MINIO_SECRET_KEY,
                     secure=False)


# 获取对象元数据
for object in OBJECT_KEYS:
    object_stat = minio_client.stat_object(BUCKET_NAME, object)

    # 获取并打印 ETag（MD5 校验和）
    etag_md5 = object_stat.etag.strip('"')  # ETag 值通常带有双引号，所以去除引号
    print("MD5 (ETag):", etag_md5) # 所有都是输出 MD5 (ETag): 00000000000000000000000000000000-1

    # 获取最后修改时间
    last_modified = object_stat.last_modified
    print("时间:", last_modified, int(last_modified.timestamp()))

