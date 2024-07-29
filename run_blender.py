import subprocess

# 定义Blender命令和参数
blender_executable = 'blender'
# blender_script = 'blender_test.py'
blender_script = 'script.py'
blender_args = '--background --python'.split()
script_args = ['example_param']

# 创建完整的命令
cmd = [blender_executable] + blender_args + [blender_script, '--'] + script_args

# 打印命令以供调试
print("运行命令:", ' '.join(cmd))

# 使用subprocess运行命令
try:
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    print("Blender输出:", result.stdout)
except subprocess.CalledProcessError as e:
    print("运行命令时出错:", e)
    print("错误输出:", e.stderr)
