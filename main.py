import os

print(os.listdir(os.getcwd()))
with open('1.txt', encoding='utf-8') as f:
    text = f.read()
    lines_1 = text.count('\n') + 1
with open('2.txt', encoding='utf-8') as f:
    text = f.read()
    lines_2 = text.count('\n') + 1
with open('3.txt', encoding='utf-8') as f:
    text = f.read()
    lines_3 = text.count('\n') + 1
print(lines_1, lines_2, lines_3)
