import bpy
import sys
# blender --background --python blender_test.py -- example_param=123456
# 获取命令行参数
argv = sys.argv

# Blender会添加一些它自己的参数，所以我们需要找到我们的参数的起点
argv = argv[argv.index("--") + 1:]

# 打印所有参数
print("传递的参数是：", argv)

# 你可以访问特定的参数，比如第一个参数
if len(argv) > 0:
    first_arg = argv[0]
    print("第一个参数是：", first_arg)

# 你的脚本逻辑在这里
# 例如，你可以根据传递的参数执行不同的操作
if first_arg == "example":
    print("执行示例操作")
    # 你的操作代码
else:
    print("执行默认操作")
    # 你的默认操作代码
