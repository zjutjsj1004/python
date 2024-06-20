#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time

def create_and_remove_symlink(src, dst, delay=10):
    """
    创建一个从 src 到 dst 的软链接，并在延迟 delay 秒后删除该软链接。

    参数:
    src (str): 源文件或目录路径。
    dst (str): 目标软链接路径。
    delay (int): 暂停时间（秒），默认是10秒。
    """
    # 提取目标路径的父目录
    parent_dir = os.path.dirname(dst)

    # 创建目标目录的父目录
    try:
        os.makedirs(parent_dir, exist_ok=True)
        print(f"目录 '{parent_dir}' 创建成功或已存在")
    except OSError as e:
        print(f"创建目录 '{parent_dir}' 失败: {e}")
        return

    # 创建软链接
    try:
        os.symlink(src, dst)
        print(f"软链接 '{dst}' 创建成功")
    except FileExistsError:
        print(f"软链接 '{dst}' 已存在")
    except OSError as e:
        print(f"创建软链接 '{dst}' 失败: {e}")
        return

    # 暂停 delay 秒
    print(f"暂停 {delay} 秒...")
    time.sleep(delay)

    # 删除软链接
    if os.path.islink(dst):
        try:
            os.unlink(dst)
            print(f"软链接 '{dst}' 已删除")
        except OSError as e:
            print(f"删除软链接 '{dst}' 失败: {e}")
    else:
        print(f"软链接 '{dst}' 不存在或路径不是软链接")

# 使用函数
src_path = '/data/gocpplua/python/aa'
dst_path = '/tmp/python/aa'

create_and_remove_symlink(src_path, dst_path)
