import os




def ch_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(dir_path):
        os.chdir(dir_name)
        return "We are in folder {}".format(dir_name)
    else:
        return "Can't change dir"


def ls_dir():
    print("Files and folders in the current directory:")
    files_and_folders = os.listdir(path=".")
    for item in files_and_folders:
        print(item)


def rm_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(dir_path):
        os.rmdir(dir_path)
        return "Directory successfully removed"
    else:
        return "Can't remove dir"


def mk_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        return "Directory successfully created"
    except FileExistsError:
        return "Directory already exists"
