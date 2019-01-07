# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

dirname = []
for i in range(1, 9):
    dirname.append("dir_" + str(i))

for j in dirname:
    dir_path = os.path.join(os.getcwd(), j)
    print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Directory already exists')

for k in dirname:
    dir_path = os.path.join(os.getcwd(), k)
    print(dir_path)
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Directory doesnt exist')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for m in os.listdir(path=os.getcwd()):
    if os.path.isdir(m):
        print(m)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
file_name = os.path.basename(__file__)
copy_name = file_name[:-3] + "_copy.py"

try:
    shutil.copy(os.path.join(os.getcwd(), file_name), os.path.join(os.getcwd(), copy_name))
except FileExistsError:
    print('Copy already exists')
