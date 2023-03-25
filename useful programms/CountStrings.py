"""
Подсчитать кол-во строк в питоновских файлах, исключая закоменнтированные и пустые строки
"""


import os

def strings_count(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            count = 0
            if os.path.join(root, file).endswith('.py'):
                curr_file = open(os.path.join(root, file), 'r')
                for line in curr_file.readlines():
                    if not (line == '\n' or line.strip().startswith(('"', '#', "'"))):
                        count += 1
                yield os.path.join(root, file), count

for element in strings_count(directory='..'):
    print('File {} : amount of strings - {}'.format(element[0], element[1]))
