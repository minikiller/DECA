



# Load the mesh (assuming the file is a .obj file)
obj_file_path='/home/user/project/sunlf/expre/TestSamples/examples/results/alfw1/alfw1.obj'


import open3d as o3d

# 加载三角形网格
mesh = o3d.io.read_triangle_mesh(obj_file_path)

# 应用 Catmull-Clark 细分算法
mesh = mesh.subdivide_midpoint(number_of_iterations=1)

# 保存细分后的网格
o3d.io.write_triangle_mesh("output_mesh.obj", mesh)

