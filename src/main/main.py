# -*- coding: utf-8 -*-
# @Author: zhang yuxiao

import requests
from bs4 import BeautifulSoup
from src.const.const_value import webs


class get_novel_main:
    web_name = ''
    title = ''
    base_url = ''
    subs = ''
    end = ''
    info = ()

    def __init__(self, web_name, title, base_url, subs, ends):
        self.web_name = web_name
        self.title = title
        self.base_url = base_url
        self.subs = subs
        self.ends = ends
        self.info = webs.WEB_INFO[self.web_name]

    def get_novel(self):
        html_url = self.base_url + self.subs
        req = requests.get(url=html_url, headers=webs.HEADER)
        req.encoding = 'gbk'
        bf = BeautifulSoup(req.text, "lxml")
        titles = bf.find_all('div', class_=self.info[1])
        text = bf.find_all('div', class_=self.info[2])
        chapter = self.get_chapter(titles)
        return chapter, text[0].text.replace(self.info[-1], ''), self.get_next(self, bf)

    @staticmethod
    def get_chapter(text):
        index = text.find('作品:')
        return text[0:index]

    @staticmethod
    def get_next(self, bf):
        return bf.find('div', class_=self.info[3]).find_all('a')[3].get('href')
