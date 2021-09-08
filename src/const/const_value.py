# -*- coding:utf-8 -*-
# @Project ：get_novel
# @File: const_value.py
# @Time: 2021/9/6 14:18
# @Author: zyxhangzhou

import enum


class webs(enum.Enum):
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.138 '
                      'Safari/537.36 '
    }
    WEB_INFO = {'DIYI_BANZHU': ('http://www.diyibanzhu.info/', 'nr_title', 'novelcontent', 'nr_page', '\xa0' * 4),
                'BIQOOGE': ('https://www.biqooge.com/', 'bookname', 'content', 'bottem1', '\xa0' * 4)}
