# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import easy


choice = ''
while True:
    print("Please select the choice:\n\
1. Cd to a dir\n\
2. Show contents the of current dir\n\
3. Remove a dir\n\
4. Create a dir\n\
5. Quit")
    choice = input("What do you choose? (1/2/3/4/5): ")
    if choice == '1':
        dir_name_input = input("Enter the name of a directory you wish to \
cd to: ")
        print(easy.ch_dir(dir_name_input))
    elif choice == '2':
        easy.ls_dir()
    elif choice == '3':
        dir_name_input = input("Enter the name of a directory you wish to \
remove: ")
        print(easy.rm_dir(dir_name_input))
    elif choice == '4':
        dir_name_input = input("Enter the name of a directory you wish to \
create: ")
        print(easy.mk_dir(dir_name_input))
    elif choice == '5':
        print("Exiting...")
        exit()
    else:
        print("Incorrect number.")




