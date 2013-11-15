# -*- coding: utf-8 -*-
# from BeautifulSoup import BeautifulSoup
import BeautifulSoup
import urllib
import re
import json
import urllib2, cookielib, urllib
import time

# decode to utf-8
def decode_strange_str(s):
    s = s.replace('&#x','\u').replace(';','').replace('&nbsp','')
    u = s.decode('unicode-escape')
    return u

# tag就是标签 beautifulsoup.tag就是bs中的标签对象
def extract_string(node):
    '''Extract all strings under one Tag.

    It is properly to use this function to extract strings under one node only when the strings are
    split from a entirety in meaning.

    Args:
        node: BeautifulSoup node.
    Returns:
        All the split strings will be combined into a entirety of unicode type.
    '''
    u = u''
    if type(node) == BeautifulSoup.Tag:
        for i in node.contents:
            u += extract_string(i)
    else:
        u += node.string
    return u

def parseBookDetail():
    html = '''<dl class="booklist">
                    <dt>题名/责任者:</dt>
                    <dd><a href="openlink.php?title=iOS%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97">&#x0069;&#x004f;&#x0053;&#x5f00;&#x53d1;&#x6307;&#x5357;</a>:&#x4ece;&#x96f6;&#x57fa;&#x7840;&#x5230;&#x0041;&#x0070;&#x0070;&#x0020;&#x0053;&#x0074;&#x006f;&#x0072;&#x0065;&#x4e0a;&#x67b6;/&#x5173;&#x4e1c;&#x5347;&#x7f16;&#x8457;</dd>
                </dl>
           '''
    soup = BeautifulSoup.BeautifulSoup(html)
    book_intro = soup.findAll('dl', {'class': 'booklist'})
    # .dt返回的参数是带有dt标签的
    # print book_intro[0].dt
    # print type(book_intro[0].dt)
    # for i in book_intro[0].dt.contents:
    #     print i
    # text is equal to string
    # print book_intro[0].dt.text
    # print book_intro[0].dt.string
    print extract_string(book_intro[0].dt)
    print decode_strange_str(extract_string(book_intro[0].dd))

def getBookDetail():
    url = "http://www.lib.seu.edu.cn:8080/opac/item.php?marc_no=0000917439"
    uFile = urllib.urlopen(url)
    html = uFile.read()
    soup = BeautifulSoup.BeautifulSoup(html)

    book_intro = soup.findAll('dl', {'class': 'booklist'})
    # for intro in book_intro:
    #     print intro

    for i in xrange(len(book_intro)-1):
        intro_item = book_intro[i]
        # print 

if __name__ == '__main__':
    # parseBookDetail()
    # timestamp = "%13f" % (time.time()*1000)
    print time.time()
    print time.time()*1000
    print "%13f" % (time.time()*1000)
    # 获得13位的时间戳
    print "%13.0f" % (time.time()*1000)
    print 333333.33
    print "%3f" % 333333.33
