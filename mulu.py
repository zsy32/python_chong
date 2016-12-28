import os
import re


pattern = re.compile(r'\d{4}[a-zA-Z]{2}\d{2,}')  # 编译个正则表达式
listfiles = []
gch = []
tempgch = []


def getgch(listfiles):
    for files in listfiles:  # 把传入的文件列表逐个取出用'\\'分开后写入list
        global pattern
        global gch
        global tempgch
        a = files.split('\\')
        for i in a:  # 将list逐个取出和正则表达式匹配
            match = pattern.match(i)
            if match:
                tempgch.append(match.group())  # 把匹配的结果放到临时list中
    gch = list(set(tempgch))  # 把临时list去重
    return gch


def walkdir(srcdir):  # 遍历目录
    global listfiles
    srcdir = os.path.abspath(srcdir)
    for parent, dirs, files in os.walk(srcdir):
        for file in files:
            infile = os.path.join(parent, file)
            listfiles.append(infile)
    # print listfiles
    getgch(listfiles)  # 返回文件列表，这里似乎更应该直接返回dirs这个列表即可


srcdir = str(raw_input("please input the dirs:\n"))
walkdir(srcdir)