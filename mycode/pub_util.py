
##整合常用的函数

##文件类
# Description	: Check a file exists and that we can read the file
from os import rename, chdir, makedirs,path,walk
from os.path import exists, pardir

##创建目录
def create_directory(name):
    if exists(pardir+"\\"+name):
        print('Folder already exists... Cannot Overwrite this')
    else:
        from os import makedirs
        makedirs(pardir+"\\"+name)


# 删除目录
def delete_directory(name):
    from os import removedirs
    removedirs(name)


# 目录重命名
def rename_directory(direct, name):
    rename(direct, name)


# Sets the working directory
def set_working_directory():
    chdir(pardir)


# 备份目录
def backup_files(name_dir, folder):
    from shutil import copytree
    copytree(pardir, name_dir + ':\\' + folder)


# 移动目录到某一个路径
# Overwrites the file if it already exists
def move_folder(filename, name_dir, folder):
    if not exists(name_dir+":\\"+folder):
        makedirs(name_dir+':\\'+folder)
    from shutil import move
    move(filename, name_dir+":\\"+folder+'\\')

##文件目录大小
def folder_size (folder_path):
    dir_size = 0  # Set the size to 0
    fsizedicr = {'Bytes': 1,
                 'Kilobytes': float(1) / 1024,
                 'Megabytes': float(1) / (1024 * 1024),
                 'Gigabytes': float(1) / (1024 * 1024 * 1024)}
    for (path, dirs, files) in walk(folder_path):
        for file in files:
            filename = path.join(path, file)
            dir_size += path.getsize(filename)

    fsizeList = [str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr]  # List of units

    if dir_size == 0:
        print("File Empty")
    else:
        for units in sorted(fsizeList)[::-1]:
            print("Folder Size: " + units)