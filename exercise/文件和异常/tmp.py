import os

file_path = 'demo.txt'
file_stat = os.stat(file_path)

# 获取文件的权限位
file_mode = file_stat.st_mode

# 将权限位转换为八进制表示
file_permissions = oct(file_mode)[-3:]

print(f"文件权限: {file_permissions}")
