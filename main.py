import glob
import os

dir_name = 'D:\\Netology\Homeworks Files_3'
pattern = '*.txt'
new_file = 'new_file.all'
glob_path = os.path.join(dir_name, pattern)
list_files = glob.glob(glob_path)
list_files = sorted(list_files, key=lambda x: os.stat(os.path.join(dir_name, x)).st_size)

for file_name in list_files:
    print(file_name)
    with open(file_name, 'r', encoding='utf-8') as fr, open(new_file, 'a', encoding='utf-8') as fw:
        fw.write(f'\n\n------------ {file_name}\n\n')
        for line in fr:
            fw.write(line)

    file_path = os.path.join(dir_name, file_name)
    file_size = os.stat(file_path).st_size
    print(file_size, ' -->', file_name)

# if list_files:
#     for file_name in list_files:
#         with open(file_name, 'r') as fr, open(new_file, 'a') as fw:
#             fw.write(f'\n\n------------ {file_name}\n\n')
#             for line in fr:
#                 fw.write(line)
