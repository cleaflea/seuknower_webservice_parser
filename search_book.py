# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib
import re
import json
import urllib2, cookielib, urllib

'''
book_item = book.BookSearchItem(
                book_div.h3.a['href'].encode('utf-8').strip()[17:],
                decode_strange_str(book_divs[0].h3.a.string[2:]).encode('utf-8').strip(),
                book_div.find('span',{'class':'doc_type_class'}).string.encode('utf-8').strip(),
                decode_strange_str(book_div.h3.contents[2].string).encode('utf-8').strip(),
                decode_strange_str(book_div.p.contents[2].string).encode('utf-8').strip(),
                decode_strange_str(book_div.p.contents[4].string).encode('utf-8').strip(),
                book_div.p.span.contents[1].string.encode('utf-8').strip(),
                book_div.p.span.contents[5].string.encode('utf-8').strip()
            )
'''
import book
def getbooklist():
    url = "http://www.lib.seu.edu.cn:8080/opac/openlink.php?strSearchType=title&historyCount=1&strText=ios&x=-926&y=-182&doctype=ALL&match_flag=forward&displaypg=20&sort=CATA_DATE&orderby=desc&showmode=list&dept=ALL"
    uFile = urllib.urlopen(url)
    html = uFile.read()
    soup = BeautifulSoup(html)
    book_divs = soup.findAll('div',{'class':'list_books', 'id':'list_books'})
    # print len(book_divs)

# decode to utf-8
def decode_strange_str(s):
    s = s.replace('&#x','\u').replace(';','').replace('&nbsp','')
    u = s.decode('unicode-escape')
    return u
    # s = s.replace('&#x', '\u').replace(';','')
    # return s

def parsebookitem():
    html = '''<div class="list_books" id="list_books">
            
            <h3><span class="doc_type_class">中文图书</span><a href="item.php?marc_no=0000917439">1.&#x0069;&#x004f;&#x0053;&#x5f00;&#x53d1;&#x6307;&#x5357;&#x003a;&#x4ece;&#x96f6;&#x57fa;&#x7840;&#x5230;&#x0041;&#x0070;&#x0070;&#x0020;&#x0053;&#x0074;&#x006f;&#x0072;&#x0065;&#x4e0a;&#x67b6;</a>      &#x0054;&#x004e;&#x0039;&#x0032;&#x0039;&#x002e;&#x0035;&#x0033;&#x002f;&#x0033;&#x0033;&#x0037; </h3> 
            <p>
            <span><strong>馆藏复本：</strong>2 <br />
            <strong>可借复本：</strong>0 </span>
            &#x5173;&#x4e1c;&#x5347;&#x7f16;&#x8457; <br />
            &#x4eba;&#x6c11;&#x90ae;&#x7535;&#x51fa;&#x7248;&#x793e;&nbsp;&#x0032;&#x0030;&#x0031;&#x0033;
            </p>
        </div>

    '''

    soup = BeautifulSoup(html)
    book_div = soup.findAll('div',{'class':'list_books', 'id':'list_books'})
    # get the marc_no
    print book_div[0].h3.a['href'].encode('utf-8').strip()[17:]
    # book_title
    print decode_strange_str(book_div[0].h3.a.string[2:]).encode('utf-8').strip()
    # chinese or foreign book
    print book_div[0].find('span',{'class':'doc_type_class'}).string.encode('utf-8').strip()
    # TN929.53/337
    print decode_strange_str(book_div[0].h3.contents[2].string).encode('utf-8').strip()
    # auther
    print decode_strange_str(book_div[0].p.contents[2].string).encode('utf-8').strip()
    # publisher
    print decode_strange_str(book_div[0].p.contents[4].string).encode('utf-8').strip()
    # 馆藏复本：
    print book_div[0].p.span.contents[1].string.encode('utf-8').strip()
    # 可借复本：
    print book_div[0].p.span.contents[5].string.encode('utf-8').strip()

if __name__ == '__main__':
    parsebookitem()