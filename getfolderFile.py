import os
# 写入文件
#


file_folder_name = input('请输入您要统计的文件夹路径:')
# file_folder_name = r'C:\Users\admin\Desktop\批量文章下载'
lis = os.listdir(file_folder_name)
# a 追加 w写入
with open(r'统计.txt', 'w', encoding='utf-8') as file_obj:
    for file_name in lis:
        # 存在这个目录并且是文件夹则打开
        _address = f'{file_folder_name}\\{file_name}'
        if os.path.exists(_address) and os.path.isdir(_address):
            _file = os.listdir(_address)
            _len = len(_file)
            print(file_name+'：'+str(_len)+'篇')
            file_obj.write(file_name+'：'+str(_len)+'篇'+'\n')
        # for item_name in _file:
        #     file_obj.write(item_name+'\n')
