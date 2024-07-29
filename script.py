
# input_filepath='/home/user/project/sunlf/expre/TestSamples/examples/results/alfw1/alfw1.obj'
input_filepath='./wang.obj'

import bpy

# 指定输入和输出文件路径
# input_filepath = "/path/to/your/input_file/.obj"  # 替换为你的输入文件路径
output_filepath = "./output_wang.obj"  # 替换为你的输出文件路径

# 删除所有现有的对象（可选）
bpy.ops.wm.read_factory_settings(use_empty=True)

# 导入 OBJ 文件
bpy.ops.import_scene.obj(filepath=input_filepath)
print(bpy.app.version_string)

# 获取导入的对象
obj = bpy.context.selected_objects[0]
# bpy.context.view_layer.objects.active = obj
bpy.context.scene.objects.active = obj


# 确保处于编辑模式
bpy.ops.object.mode_set(mode='EDIT')

# 选择所有面片
bpy.ops.mesh.select_all(action='SELECT')

# 将三角面片转换为四边形面片
# bpy.ops.mesh.tris_convert_to_quads()



# 将三角面片转换为四边形面片
# face_threshold 参数设置为 45 度
# shape_threshold 参数设置为 0.5
bpy.ops.mesh.tris_convert_to_quads(
    face_threshold=45.0,
    shape_threshold=0.5
)

# 返回到对象模式
bpy.ops.object.mode_set(mode='OBJECT')


# 简化网格（使用比例简化）
# bpy.ops.object.modifier_add(type='DECIMATE')
# decimate_modifier = obj.modifiers['Decimate']
# decimate_modifier.ratio = 0.5  # 调整比例以减少面片数量

# # 应用简化修改器
# bpy.ops.object.modifier_apply(modifier='Decimate')

# 移除多余数据（如材料、UV 坐标等）
# bpy.ops.object.material_slot_remove_unused()
# 导出为新的 OBJ 文件
bpy.ops.export_scene.obj(filepath=output_filepath, use_materials=False)
