import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置页面标题
st.title('Streamlit 测试程序')

# 显示文本
st.write("欢迎使用 Streamlit 测试程序！")

# 创建一个简单的输入框
number = st.slider('选择一个数字', 0, 100, 25)

# 显示输入的数字
st.write(f'你选择的数字是: {number}')

# 生成一个简单的图表
st.write('这是一个简单的图表:')
data = np.random.randn(100)
fig, ax = plt.subplots()
ax.hist(data, bins=30, color='blue', alpha=0.7)
st.pyplot(fig)

# 创建一个数据表
st.write('这是一个数据表:')
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})
st.dataframe(df)

# 显示 Markdown
st.write('## 这是一个 Markdown 示例')
st.markdown('**Streamlit** 可以渲染 *Markdown* 格式的文本')

# 显示图片
st.write('这是一个示例图片:')
st.image('https://www.example.com/sample.jpg', caption='示例图片')
