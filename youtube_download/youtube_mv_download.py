# -*- coding: utf-8 -*-
import subprocess

import time

import os


# list.txt路径
PATH = os.path.dirname(os.path.abspath(__file__))+'/list.txt'
# 查询视频信息语句
COMMAND_PREFIX_CHECK = 'youtube-dl -F '
# 下载1080p视频语句
COMMAND_PREFIX_DOWNLOAD = 'youtube-dl -f 137+140 '


# 传入url，加载相应的1080p视频
def download_by_url(url):
    p = subprocess.Popen(COMMAND_PREFIX_DOWNLOAD + ur, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    start = time.time()
    print("********\tStart download:" + ur + "\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
    for elm in p.stdout.readlines():
        if not elm.strip():
            # do stuff
            line = p.stdout.readline()
            if not line == '':
                print(line.strip(b'\n'))
            else:
                break
    end = time.time()
    print("********\tEnd\t"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)),)
    print("taking："+str(int(end-start))+" seconds")
    mark_downloaded_url(url)


# 从list.txt中读取一条未下载过的url
def get_url_from_list():
    print("\n********\tGet url")
    f = open(PATH, 'r+')
    for line in f.readlines():
        if not line == '\n':
            if line[0] == 'h':
                return line.strip('\n')
    return '下载完成'


# 标记已经下载过的url（url前面加上*）
def mark_downloaded_url(url):
    output = []
    f = open(PATH, 'r+')
    i = 0
    for line in f.readlines():
        line = line.strip('\n')
        url = ur.strip('\n')
        if line == url:
            line = "*" + line
        output.append(line+"\n")
        i = i + 1
    f.close()
    f = open(PATH, 'w+')
    f.writelines(output)
    f.close()


if __name__ == '__main__':
    # 检查list.txt文件是否存在
    if not os.path.exists(PATH):
        print("can't find "+PATH)
        exit(0)
    while True:
        # 若想暂停下载，在同级目录下建一个stop.txt
        if os.path.exists(os.path.dirname(os.path.abspath(__file__))+'/stop.txt'):
            exit(0)
        ur = get_url_from_list()
        url = ur.encode()
        print("\t\t\tRead:" + ur)
        if ur == '下载完成':
            print("FINISH DOWNLOAD")
            break
        download_by_url(url)
