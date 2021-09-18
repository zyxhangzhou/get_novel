# -*- coding:utf-8 -*-
# @Project ：get_novel
# @File: test.py
# @Time: 2021/9/9 17:50
# @Author: zyxhangzhou
from src.main.do_get import SaveNovel
from src.const.const_value import *

if __name__ == '__main__':
    web_name = WEB_NAMES[0]
    novel = SaveNovel(web_name, '飞剑问道', 'http://www.diyibanzhu.info/0/2/20.html')
    novel.print_novel()

