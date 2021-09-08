# -*- coding:utf-8 -*-
# @Project ：get_novel
# @File: do_get.py
# @Time: 2021/9/6 17:37
# @Author: zyxhangzhou
from src.const.const_value import webs

class save_novel:
    web_name = ''
    title = ''
    url_first_page = ''
    subs = ''
    end = ''

    def __init__(self, web_name, title):
        self.web_name = web_name
        self.title = title

    def pre_check(self):
        base_url = webs.WEB_INFO[self.web_name][0]
        subs = self.url_first_page[len(base_url):]
        