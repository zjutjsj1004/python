import os
import zipfile
import tarfile
import random
import glob
import shutil
import argparse

def compress_files(pattern, output_filename, compress_func):
    """根据文件模式压缩符合的文件"""
    files = glob.glob(pattern)
    if files:
        compress_func(files, output_filename)
    else:
        print(f"No files matched the pattern {pattern}. Skipping...")

def compress_to_zip_from_files(files, output_filename):
    """从文件列表压缩为ZIP"""

    """从文件列表压缩为ZIP。如果文件列表为空，不生成ZIP文件。"""
    if not files:
        print("No files to compress. Skipping ZIP creation...")
        return
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            arcname = os.path.basename(file)
            # zipf.write(file, os.path.relpath(file, root_dir)) # 会包含目录
            zipf.write(file, arcname=arcname)

root_dir = "/data/gocpplua/python/qiongyu"
upload_dir = "/data/gocpplua/python/qiongyu"

# 6. 压缩符合正则"^snapshot(-\\d+)?.ssnr$"的文件为ZIP
compress_files(os.path.join(root_dir, "nerf-export/snapshot*[0-9]*.ssnr"),
                os.path.join(upload_dir, "nerf-snapshot-package.zip"),
                compress_to_zip_from_files)