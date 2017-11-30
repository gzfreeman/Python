
##整合常用的函数

##文件类
# Description	: Check a file exists and that we can read the file
from os import rename, chdir, makedirs
from os.path import exists, pardir

def create_directory(name):
    if exists(pardir+"\\"+name):
        print('Folder already exists... Cannot Overwrite this')
    else:
        from os import makedirs
        makedirs(pardir+"\\"+name)


# Deletes a directory
def delete_directory(name):
    from os import removedirs
    removedirs(name)


# Rename a directory
def rename_directory(direct, name):
    rename(direct, name)


# Sets the working directory
def set_working_directory():
    chdir(pardir)


# Backup the folder tree
def backup_files(name_dir, folder):
    from shutil import copytree
    copytree(pardir, name_dir + ':\\' + folder)


# Move folder to specific location
# Overwrites the file if it already exists
def move_folder(filename, name_dir, folder):
    if not exists(name_dir+":\\"+folder):
        makedirs(name_dir+':\\'+folder)
    from shutil import move
    move(filename, name_dir+":\\"+folder+'\\')