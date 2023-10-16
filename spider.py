# -*- coding = utf-8 -*-

import csv
import json

import requests

from bs4 import BeautifulSoup

import re

import os

import urllib.request
import urllib.parse


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


class ihchina:
    # # 定义要创建的目录
    # mkpath = "E:/spidertxt/MyModel"
    # mkdir(mkpath)

    def __init__(self):
        pass

    def run(self):
        print("################################ ihchina ################################")
        # 非遗博物馆
        self._get_ihchina_root_info()
        self._parser_ihchina_info()

    def _get_ihchina_root_info(self):
        with open("E:/spidertxt/MyModel/MS/ihchina_link.txt", "wt+") as f:
            count = 0
            url = "http://www.ihchina.cn/Article/Index/getProject.html?"
            for i in range(1, 50):
                data = circlePage(i)
                s = requests.session()
                r = s.get(url, params=data)
                # self.soup = BeautifulSoup(r.text, "html.parser")
                f_data = r.json()
                f_data = f_data['list']
                # data = data['id']
                for j in range(len(f_data)):
                    count += 1
                    # print('http://www.ihchina.cn/project_details/' + f_data[j]['id'] + '/')
                    temp = 'http://www.ihchina.cn/project_details/' + f_data[j]['id'] + '/'
                    f.write(temp)
                    f.write('\n')
                    print(count)
            f.close()

    def _parser_ihchina_info(self):
        # 写入csv文件
        csv_file = open("E:/spidertxt/MyModel/MS/ihchina_info.csv", "a+", encoding='utf-8', newline='')
        try:
            csv_writer = csv.writer(csv_file, delimiter=",")
            header = ["NAME", "INFO"]  # csv文件头
            csv_writer.writerow(header)
        finally:
            csv_file.close()

        count_all = 0
        count_delete = 0
        ctjy_name = ''  # 存储传统技艺名称(去重存入txt）
        ctjy_name2 = [] # 不去重直接存入csv
        ctjy_info = []  # 存储传统技艺内容
        with open("E:/spidertxt/MyModel/MS/ihchina_link.txt", "r") as f:
            for line in f.readlines():
                line = line.strip()
                count_all += 1
                # 尝试爬取
                try:
                    r = requests.get(line, timeout=30)
                    r.raise_for_status()
                    r.encoding = r.apparent_encoding
                except:
                    print('Error')
                    break
                self.soup = BeautifulSoup(r.text, "html.parser")
                # 开始解析内容
                content = self.soup.find(name="div", attrs={"class": "x-container"})
                name = content.find(name="div", attrs={"class": "h30"})
                name = name.get_text()  # 传统技艺名称
                ctjy_name2.append(name)
                print(name)
                if name not in ctjy_name:
                    ctjy_name = ctjy_name + name + '\n'
                    count_delete += 1
                info = content.find(name="div", attrs={"class": "text"})
                info = info.find(name="div", attrs={"class": "p"})
                info = info.get_text()
                print(info)
                print("--------------------------------------------------")
                ctjy_info.append(info)
            f.close()
        print("----------------------------遍历完成----------------------------")
        print("所有技艺", count_all)
        print("技艺名去重", count_delete)
        with open("E:/spidertxt/MyModel/MS/ihchina_name.txt", "wt+", encoding='utf-8') as f:
            f.write(ctjy_name)
        print("---------------传统技艺名称（去重）存储成功---------------")
        csv_file = open("E:/spidertxt/MyModel/MS/ihchina_info.csv", "a+", encoding='utf-8', newline='')
        try:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerows(zip(ctjy_name2, ctjy_info))
        finally:
            csv_file.close()
            print("---------------传统技艺信息（未去重）存储成功---------------")


