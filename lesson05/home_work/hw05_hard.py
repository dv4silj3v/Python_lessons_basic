# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil


def print_help():
    print("help - get help")
    print("cpf <file_name> - copy file")
    print("rmf <file_name> - remove file")
    print("chd <dir_name> - change directory")
    print("lsd - list full path")


def cp_file():
    """
    Copy file in the local directory and append _copy

    :return: Copied or not
    """
    if not file_name:
        print("Please enter the filename")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    copy_path = os.path.join(os.getcwd(), file_name + "_copy")
    try:
        shutil.copy(file_path, copy_path)
        print("File '{}' has been copied".format(file_name))
    except (IOError, os.error):
        print("File '{}' doesn't exist".format(file_name))


def confirm():
    """
    Ask user for confirmation

    :return: True if the answer is Y
    :rtype: bool
    """
    answer = ""

    while answer not in ["y", "n"]:
        answer = input("Are you sure you want to remove the file? [Y/N]").lower()
    return answer == "y"


def rm_file():
    """
    Removes the file in current directory

    :return: Removed or Not
    """
    if not file_name:
        print("Please enter the right filename")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    if confirm() is True:
        try:
            os.remove(file_path)
            print("File '{}' has been removed".format(file_name))
        except OSError:
            print("File '{}' was not removed".format(file_name))
    else:
        print("Cancelling...")


def ch_dir():
    """
    Change current directory

    :param dir_name: use either absolute or local path
    :return:
    """

    if not dir_name:
        print("Please enter the right dir path")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        if os.path.isdir(dir_path):
            os.chdir(dir_path)
            print("Directory changed to '{}'".format(dir_path))
        else:
            print("{} is not a directory".format(dir_path))
    except IndexError:
        print("Wrong directory")


def ls_dir():
    """
    List full path of current directory

    :return: Full path
    """

    try:
        dir_path = os.getcwd()
        print("Current working directory is: {}".format(dir_path))
    except IndexError:
        return False


do = {
    "help": print_help,
    "cpf": cp_file,
    "rmf": rm_file,
    "chd": ch_dir,
    "lsd": ls_dir
}

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Wrong key")
        print("Please use help to see options")

