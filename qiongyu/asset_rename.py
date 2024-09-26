import os,sys
import argparse

def rename_model_nerf():
    return

def rename_osgb():
    return

def rename_3dgs():
    return

def rename_model3d():
    return

def rename_simplified():
    return

def asset_rename(rebuilding_modules):
    if "MODEL_NERF" in rebuilding_modules:
        rename_model_nerf()

    if "OSGB" in rebuilding_modules:
        rename_osgb()

    if "MODEL_3DGS" in rebuilding_modules:
        rename_3dgs()

    if "MODEL_3D" in rebuilding_modules:
        rename_model3d()

    if "MODEL_SIMPLIFIED" in rebuilding_modules:
        rename_osgb()
        
# 主函数
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='asset_rename', description='asset_rename', allow_abbrev=False)
    parser.add_argument('-p', '--port', type=int, default=8899)
    parser.add_argument('-rebuilding_modules', '--rebuilding_modules', type=str, default="")

    args = parser.parse_args()
    print(args.port, args.rebuilding_modules)

    # 使用逗号分割字符串
    rebuilding_modules = args.rebuilding_modules.split(',')
    if len(rebuilding_modules) == 0:
        print( "rebuilding_modules is empty" )

    asset_rename(rebuilding_modules)

    