# # -*- coding:utf-8 -*-
# """
#
# @Time    : 2018/2/10 20:19
# @Author  : YeJian
# @File    : test.py
#
# """
#
import urllib.request
import urllib.parse
import re
#
#
# req = urllib.request.Request('http://blog.sina.com.cn/s/blog_4701280b0102elmo.html')
# req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
# response = urllib.request.urlopen(req)
# text = response.read().decode('utf-8')
#
def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html
#
# def download_texts(bowen_list_urls):    # 根据列表下载所有文章
#
#     with open('hanhan.txt', 'ab+') as f:
#
#         for text_url in bowen_list_urls:
#             html = open_url(text_url)
#             title = re.findall(r'class="titName SG_txta">(.+?)</h2>', html)
#             f.write(title[0].encode('utf-8'))
#             f.write('\n'.encode('utf-8'))
#             time = re.findall(r'<span class="time SG_txtc">\((.+?)\)</span>', html)
#             f.write(time[0].encode('utf-8'))
#             f.write('\n\n'.encode('utf-8'))
#             start = html.find(u"<!-- 正文开始 -->")
#             end = html.find(u"<!-- 正文结束 -->")
#             html = html[start:end]
#             html = re.sub(re.compile('<p.*?>'), "\n    ", html)
#             html = re.sub(re.compile('<p>'), "\n    ", html)
#             html = re.sub(r'<(S*?)[^>]*>.*?|<.*? /> ', '', html)
#             html = re.sub(r'&[^>]*?\;', ' ', html)
#             f.write(html.encode('utf-8'))
#
#
#     print('done')
#
#
# if __name__ == '__main__':
#     rrr = ['http://blog.sina.com.cn/s/blog_4701280b0102eo83.html', 'http://blog.sina.com.cn/s/blog_4701280b0102edcd.html']
#     download_texts(rrr)

def get_urls(url):    # 获取一个页面下的所有文章链接
    html = open_url(url)
    p = re.compile(r'<a title="" target="_blank" href="(http://blog\.sina\.com\.cn/s/blog_\w+\.html)">')
    html_list = re.findall(p, html)
    return html_list

bowen_list = []
for h in range(2):
    h = h + 1
    urls = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_%d.html' % (h)
    bowen_list = bowen_list + get_urls(urls)

print(bowen_list)