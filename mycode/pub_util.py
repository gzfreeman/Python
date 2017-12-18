
##整合常用的函数

##文件类
# Description	: Check a file exists and that we can read the file
from os import rename, chdir, makedirs,path,walk
from os.path import exists, pardir
import platform


def isWindowsSystem():
    return 'Windows' in platform.system()


def isLinuxSystem():
    return 'Linux' in platform.system()

##创建目录
def create_directory(name):
    if exists(pardir+"\\"+name):
        print('目录已存在')
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

#文件目录大小

def GetPathSize(strPath):
    if not path.exists(strPath):
        return 0;

    if path.isfile(strPath):
        return path.getsize(strPath);

    nTotalSize = 0;
    for strRoot, lsDir, lsFiles in walk(strPath):
        # get child directory size
        for strDir in lsDir:
            nTotalSize = nTotalSize + GetPathSize(path.join(strRoot, strDir));

            # for child file size
        for strFile in lsFiles:
            nTotalSize = nTotalSize + path.getsize(path.join(strRoot, strFile));

    print (nTotalSize);


def write_to_file(filename, txt):
  with open(filename, 'w') as file_object:
      s = file_object.write(txt)