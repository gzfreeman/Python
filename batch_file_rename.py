# batch_file_rename.py
# 批量修改文件名


__author__ = 'Marco'
__version__ = '1.0'

import os
import argparse
from random import choice
import string

# def batch_rename(work_dir, old_ext, new_ext):
#
#     for filename in os.listdir(work_dir):
#         # Get the file extension
#         split_file = os.path.splitext(filename)
#         file_ext = split_file[1]
#         # Start of the logic to check the file extensions, if old_ext = file_ext
#         if old_ext == file_ext:
#             newfile = split_file[0] + new_ext
#             os.rename(
#                 os.path.join(work_dir, filename),
#                 os.path.join(work_dir, newfile)
#             )

def batch_rename_prefix(work_dir):
      for filename in os.listdir(work_dir):
        # 获取文件主文件名
        split_file = os.path.splitext(filename)
        #file_pf = split_file[0]
        #if old_pf == file_pf:

        newfile = GenPassword(5) + split_file[1]
        os.rename(os.path.join(work_dir, filename),os.path.join(work_dir, newfile))

def GenPassword(length,chars=string.ascii_letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

if __name__ == '__main__':
    batch_rename_prefix('d:/test1')
