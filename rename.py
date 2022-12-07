import os
# 重命名工具
#
print('如果文件夹目录名称为1，从1开始重命名，直接点回车即可')
print('*'*20)

file_folder_name = input('请输入您要同级目录下文件夹名称(或者绝对路径的全路径)：（默认为1）')
num = input('请输入您要重命名的启始序号：（默认为1）')
if (num):
    num = int(num)
else:
    num = 1
if not file_folder_name:
    file_folder_name = '1'
lis = os.listdir(file_folder_name)

for file_name in lis:
    if (not file_name.endswith('.exe') and not file_name.endswith('.py')):
        try:
            new_name = file_folder_name+'/' + \
                str(num)+'-' + file_name.lstrip('0123456789.-_ ')
            old_name = file_folder_name+'/'+file_name

            os.rename(old_name, new_name)
            num = num+1
            print('原名称:', old_name, '新名称', new_name, '修改成功')
        except:
            print(new_name, '重命名失败')
print('重命名结束')
input('点击回车键退出')