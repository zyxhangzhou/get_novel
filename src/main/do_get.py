# -*- coding:utf-8 -*-
# @Project ：get_novel
# @File: do_get.py
# @Time: 2021/9/6 17:37
# @Author: zyxhangzhou
from src.const.const_value import *
from main import GetNovelMain
import time
import random


class SaveNovel:
    web_name = ''
    title = ''
    url_first_page = ''
    sub = ''
    end = ''
    base_url = ''

    def __init__(self, web_name, title, url_first_page):
        self.web_name = web_name
        self.title = title
        self.url_first_page = url_first_page
        self.pre_check()

    def pre_check(self):
        self.base_url = WEB_INFO[self.web_name][0]
        self.sub = self.url_first_page[len(self.base_url):]
        self.end = self.process_ends(self, self.sub)

    @staticmethod
    def process_ends(self, text: str):
        index_last_slash = text.rfind('/')
        end = text[0:index_last_slash + 1]
        if self.web_name == WEB_NAMES[0]:
            end += '0.html'
        return end

    def print_novel(self):
        with open(self.title + '.txt', 'a') as f:
            main = GetNovelMain(self.web_name, self.title, self.base_url, self.sub, self.end)
            while True:
                chapter, text, next_page = main.get_novel()
                f.write(chapter)
                f.write(text)
                f.write('\n')
                if next_page == self.end:
                    break
                main.sub = next_page
                time.sleep(random.random())
