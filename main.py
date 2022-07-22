import glob
import os

dir_name = os.getcwd()
pattern = '*.txt'
new_file = 'new_file.all'
glob_path = os.path.join(dir_name, pattern)
list_files = glob.glob(glob_path)
list_files = sorted(list_files, key=lambda x: os.stat(os.path.join(dir_name, x)).st_size)

for file_name in list_files:
    with open(file_name, 'r', encoding='utf-8') as fr, open(new_file, 'a', encoding='utf-8') as fw:
        text = fr.read()
        lines = text.count('\n') + 1
        fw.write(f'\n{os.path.basename(file_name)}\n{lines}\n')
        for line in text:
            fw.write(line)
