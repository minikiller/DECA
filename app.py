import streamlit as st
from PIL import Image
import time
import os
import subprocess

import pyvista as pv
import stpyvista as stpv




# 这是一个调用外部命令处理图片的函数
def ai_process_image(input_path, output_path,output_file):
    # 构建外部命令
    command = ["python", "process_image.py", input_path, output_path]
    # 定义命令和参数
    command = [
        "python", "demos/demo_reconstruct.py",
        "-i", f"{input_path}",
        "-s", f"{output_path}",
        "--saveObj", "True"
    ]


    # 启动子进程并等待其完成
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # 检查进程是否成功完成
    if process.returncode != 0:
        st.error(f"处理图片时出错: {stderr.decode('utf-8')}")
        return None

    return output_path+output_file

# 设置图片保存的文件夹
SAVE_FOLDER = './uploaded_images'
PROCESSED_FOLDER = './processed_images/'

# 创建保存图片的文件夹（如果不存在）
os.makedirs(SAVE_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

st.title("AI 图片处理")

# 上传图片
uploaded_file = st.file_uploader("上传一张图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 保存上传的图片到本地文件夹
    input_path = os.path.join(SAVE_FOLDER, uploaded_file.name)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 显示上传的图片
    image = Image.open(input_path)
    st.warning(input_path)
    st.image(image, caption='上传的图片', use_column_width=True)

    # 按钮触发AI处理
    if st.button("开始处理"):
        # input_file = "wang.jpg"
        # 获取文件名和扩展名
        file_name, file_extension = os.path.splitext(uploaded_file.name)
        
        # 构建输出文件名
        output_file = f"{file_name}_vis.jpg"
        output_path = os.path.join(PROCESSED_FOLDER, uploaded_file.name)
        obj_file_name=os.path.join(PROCESSED_FOLDER, f"{file_name}/{file_name}.obj")
        with st.spinner('AI正在处理图片...'):
            processed_image_path = ai_process_image(input_path, PROCESSED_FOLDER,output_file)

        if processed_image_path:
            st.success('处理完成！')

            # 显示处理后的图片
            st.warning(processed_image_path)
            processed_image = Image.open(processed_image_path)
            st.image(processed_image, caption='处理后的图片', use_column_width=True)

            # Load the mesh using PyVista
            mesh = pv.read(obj_file_name)

            # Set up the plotter with off-screen rendering
            plotter = pv.Plotter(off_screen=True)
            # plotter.add_mesh(mesh, color='white')  # show_edges=True adds the gridlines
            plotter.add_mesh(mesh, color='white', show_edges=True)  # show_edges=True adds the gridlines
            plotter.view_isometric()
            plotter.show_axes()
            plotter.show_grid()  # Display the grid

            # Render the PyVista plotter using stpyvista
            stpv.stpyvista(plotter)

