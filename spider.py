# -*- coding:utf-8 -*-
"""

@Time    : 2018/2/10 18:52
@Author  : YeJian
@File    : spider.py

"""

import urllib.request
import urllib.parse
import re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html


def get_urls(url):    # 获取一个页面下的所有文章链接
    html = open_url(url)
    p = re.compile(r'<a title="" target="_blank" href="(http://blog\.sina\.com\.cn/s/blog_\w+\.html)">')
    html_list = re.findall(p, html)
    return html_list


def download_texts(bowen_list_urls):    # 根据列表下载所有文章

    with open('hanhan.txt', 'ab+') as f:

        for text_url in bowen_list_urls:
            html = open_url(text_url)
            title = re.findall(r'class="titName SG_txta">(.+?)</h2>', html)
            f.write(title[0].encode('utf-8'))
            f.write('\n'.encode('utf-8'))
            time = re.findall(r'<span class="time SG_txtc">\((.+?)\)</span>', html)
            f.write(time[0].encode('utf-8'))
            f.write('\n\n'.encode('utf-8'))
            start = html.find(u"<!-- 正文开始 -->")
            end = html.find(u"<!-- 正文结束 -->")
            html = html[start:end]
            html = re.sub(re.compile('<p.*?>'), "\n    ", html)
            html = re.sub(re.compile('<p>'), "\n    ", html)
            html = re.sub(r'<(S*?)[^>]*>.*?|<.*? /> ', '', html)
            html = re.sub(r'&[^>]*?\;', ' ', html)
            f.write(html.encode('utf-8'))
            f.write('\n\n\n'.encode('utf-8'))

        return "下载完成"


def XLWB(author='1191258123', page=2):    # 获取页面，主要函数

    bowen_list = []
    for h in range(page):
        h = h + 1
        urls = 'http://blog.sina.com.cn/s/articlelist_%s_0_%d.html' % (author, h)
        bowen_list = bowen_list + get_urls(urls)

    str = download_texts(bowen_list)
    print(str)


if __name__ == '__main__':
    XLWB()   # 第一个参数为新浪博客作者的博客目录网址后的标志数字，默认为韩寒的
             # 第二个参数为需要下载的博客目录的页数
