# -*- coding: utf-8 -*-
# @Author: zhang yuxiao

import requests
from bs4 import BeautifulSoup
from src.const.const_value import *

class GetNovelMain:
    web_name = ''
    title = ''
    base_url = ''
    sub = ''
    end = ''
    info = ()

    def __init__(self, web_name, title, base_url, sub, end):
        self.web_name = web_name
        self.title = title
        self.base_url = base_url
        self.sub = sub
        self.ends = end
        self.info = WEB_INFO[self.web_name]

    def get_novel(self):
        html_url = self.base_url + self.sub
        req = requests.get(url=html_url, headers=HEADER)
        req.encoding = 'gbk'
        bf = BeautifulSoup(req.text, "lxml")
        titles = bf.find_all('div', class_=self.info[1])
        text = bf.find_all('div', class_=self.info[2])
        chapter = self.get_chapter(self, titles)
        return chapter, text[0].text.replace(self.info[-1], ''), self.get_next(self, bf)

    # TODO 不同网站有不同的获得策略 且 还需要判断是否要手动加上章节判定
    @staticmethod
    def get_chapter(self, titles):
        if self.web_name == WEB_NAMES[0]:
            index = titles.text.find('作品:')
            return titles.text[0:index]
        elif self.web_name == WEB_NAMES[1]:
            return titles.find('h1').text
        return ''

    @staticmethod
    def get_next(self, bf):
        return bf.find('div', class_=self.info[3]).find_all('a')[3].get('href')
