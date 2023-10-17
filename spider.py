# -*- coding = utf-8 -*-

import csv
import json

import requests

from bs4 import BeautifulSoup

import re

import os

import urllib.request
import urllib.parse
import time
import random


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def circlePage(i):  # 遍历每一页
    data = {
        "province": "",
        "rx_time": "",
        "type": 10,
        "cate": "",
        "keywords": "",
        "category_id": 16,
        "limit": 10,
        "p": i
    }
    return data


class Historian:
    # # 定义要创建的目录
    # mkpath = "E:/spidertxt/MyModel"
    # mkdir(mkpath)

    def __init__(self, url, path, headers):
        self.url = url
        self.path = path
        self.links = []
        self.headers = headers

    def getList(self):
        print("**********获取指定内容的网址**********")
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find(name="div", attrs={"class": "sons"})
            twelve_list = content.find(name="div", attrs={"class": "bookcont"})
            list = twelve_list.find_all('a')
            pre_link = 'https://shiwens.com'
            for single in list:
                link = pre_link + single.get('href')
                self.links.append(link)


    def getContent(self):
        print("**********开始获取每个网址下的具体内容**********")
        # 写入csv文件
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            print(self.path + " build success")
        else:
            print(self.path + " already exist")
        filePath = os.path.join(self.path, 'twelveContent.csv')
        csv_file = open(filePath, "a+", encoding='utf-8', newline='')
        try:
            csv_writer = csv.writer(csv_file, delimiter=",")
            header = ["NAME", "CONT"]  # csv文件头
            csv_writer.writerow(header)
        finally:
            csv_file.close()

        titleList = []
        contentList = []
        for link in self.links:
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                loc = soup.find(name="div", attrs={"class": "main3"}).find(name="div", attrs={"class": "cont"})
                # title
                title = loc.find('b').get_text()
                print(title)
                titleList.append(title)
                # content
                content = ''
                lines = loc.find(name="div", attrs={"class": "contson"})
                lines = lines.find_all('p')
                for line in lines:
                    content += line.get_text() + '\n'
                contentList.append(content)
            else:
                print("error")
            # # 设置一个随机的延时，例如在1到3秒之间
            # delay = random.uniform(1, 3)
            # time.sleep(delay)

        print("**开始写入文件**")
        csv_file = open(filePath, "a+", encoding='utf-8', newline='')
        try:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerows(zip(titleList, contentList))
        finally:
            csv_file.close()

    def forTest(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            loc = soup.find(name="div", attrs={"class": "main3"}).find(name="div", attrs={"class": "cont"})
            # title
            title = loc.find('b').get_text()
            print(title)
            # content
            content = ''
            lines = loc.find(name="div", attrs={"class": "contson"})
            lines = lines.find_all('p')
            for line in lines:
                content += line.get_text() + '\n'
                # content += line.get_text()
                # content += '\n'
            with open('/Users/tanyuyao/Documents/PaperDocument/OriginalContent/test.txt', 'w', encoding='utf-8') as f:
                f.write(content)



if __name__ == '__main__':
    # 自定义请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://example.com',
        'Accept-Language': 'en-US,en;q=0.5',
    }

    url = 'https://shiwens.com/book_361.html'

    folder_path = os.path.expanduser('~/Documents/PaperDocument/OriginalContent')

    spider_twlve = Historian(url, folder_path,headers)

    # 获取十二本纪的网页地址
    spider_twlve.getList()
    for link in spider_twlve.links:
        print(link)
    # 获取十二本纪内容并存储
    spider_twlve.getContent()

    # spider_twlve.forTest("https://shiwens.com/bookv_23578.html")
