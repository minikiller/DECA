import streamlit as st
from PIL import Image, ImageOps
import io

# 设置页面标题
st.title("图片处理应用")

# 文件上传
uploaded_file = st.file_uploader("上传一张图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 读取图片
    image = Image.open(uploaded_file)
    
    # 在前台显示原始图片
    st.image(image, caption='原始图片', use_column_width=True)
    
    # 应用处理（示例：将图片转换为灰度图）
    processed_image = ImageOps.grayscale(image)
    
    # 显示处理后的图片
    st.image(processed_image, caption='处理后的图片', use_column_width=True)
    
    # 将处理后的图片保存为字节
    buf = io.BytesIO()
    processed_image.save(buf, format='PNG')
    byte_im = buf.getvalue()
    
    # 提供下载链接
    st.download_button(
        label="下载处理后的图片",
        data=byte_im,
        file_name="processed_image.png",
        mime="image/png"
    )
