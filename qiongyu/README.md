# rebuilding_modules
## 支持的模型类型
- Nerf模型: MODEL_NERF  
- OSGB模型: OSGB  
- 3DGS模型: MODEL_3DGS   
- Mesh贴图模型: MODEL_3D   
- Mesh减面模型: MODEL_SIMPLIFIED  
- 单体化模型: MODEL_ENTITY

## 例子
MODEL_NERF,OSGB


# 重命名
目录	当前文件名	正式备份文件名	备注
dense-export	model.obj		不变
	model_trans.obj		不变
	model_texture_trans.tar.gz	兵马俑_09011030_model_Textured.zip	场景+日期+时间+类型
	model_sem_trans.obj		不变
	dom.tif		不变
	dsm.tif		不变
	dense_points.jpg		不变
	dense_points_no_ground.jpg		不变
	densesimplify 产物	兵马俑_0901_model_50w.tar.gz	场景+日期+时间+类型
			
nerf-export	xxxx.ssnr 或多个文件(分块数据)	兵马俑_09011030_NeRF.tar.gz	场景+日期+时间+类型
			
sfm-workspace/0/dense	lod_obj目录	兵马俑_0901_OSGB.tar.gz	场景+日期+时间+类型
	lod_ply目录		
			
gs-export	SenseGS.ply	兵马俑_09011030_3DGS.ply	场景+日期+时间+类型
	SenseGS.splat	兵马俑_09011030_3DGS.splat	场景+日期+时间+类型
			
seg-export			
	单体化文件(多个)	兵马俑_09011030_Instance.zip	场景+日期+时间+类型
