#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, stat
import ConfigParser as cp
import subprocess
import shutil
import tarfile
import xml.etree.ElementTree as ET


# 定义和读取各种变量

def extract(tar_path, target_path):
    try:
        tar1 = tarfile.open(tar_path, "r:gz")
        file_names = tar1.getnames()

        for file_name in file_names:
            tar1.extract(file_name, target_path)
        tar1.close()
    except Exception as e:
        print('异常信息:' + str(e))


config = cp.ConfigParser()
config.read("tomcat.ini")
TomTarfile = eval(config.get("tomcatinfo", "TomcatTarFile"))
ExtractPath = eval(config.get("tomcatinfo", "ExtractPath"))
ExtarctName = eval(config.get("tomcatinfo", "ExtarctName"))
# retcode = subprocess.call((['ls','-l',monurl]),shell=False)

extract(TomTarfile, ExtarctName)





# def tomcat():
#         print("------安装tomcat " + index + "------")
#         target = _baseDir + "/tomcat-7"
#         if index > 0:
#             target = target + "-" + index
#         print("复制文件到" + target)
#         # shutil.copytree(_tomcatFile, target)
#         # bin_path = target + "/bin/"
#         # print("设置PID文件")
#         # pid_path_config = "CATALINA_PID=\"" + target + "/tomcat.pid\""
#         fileappend(bin_path + "setenv.sh", pid_path_config)
#
#         # 修改端口
#         if index > 0:
#             print("配置端口")
#             server_file = target + "/conf/server.xml"
#             server_xml = ET.parse(server_file)
#
#             node_server = server_xml.getroot()
#             old_port = node_server.attrib["port"]
#             node_server.set("port", str(int(old_port) + index))
#
#             node_connector = node_server.find("./Service/Connector")
#             old_port = node_connector.attrib["port"]
#             node_connector.set("port", str(int(old_port) + index))
#
#             old_port = node_connector.attrib["redirectPort"]
#             node_connector.set("redirectPort", str(int(old_port) + index))
#             server_xml.write(server_file)
#             return
#
#
#
#
# ##删除tomcat内置的示例目录,安装完后需要删除以上
#  def rmwebapps():
#
#
#
#
#
# def fileappend(file_path, text):
#     with open(file_path, "a") as file:
#         file.write(text)
#     return
#
#
# def filesearch(file_path, search_text):
#     is_exist = False
#     with open(file_path) as file:
#         for line in file.readlines():
#             if line.find(search_text) >= 0:
#                 is_exist = True
#                 break
#     return is_exist
#
#
# #tomcat()
