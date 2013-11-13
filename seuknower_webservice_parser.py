# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib
import re
import json

def parseJwcService():
    uFile = urllib.urlopen("http://127.0.0.1:8000/seuknower_webservice/jwc/info")
    jsonresult = uFile.read()
    result = json.loads(jsonresult)

    for info in result:
        print 'updateTime--->' + info[0] + 'channel--->' + info[1] + 'title--->' + info[2] + 'attachmentList--->'
        for attachment in info[3]:
            print 'name--->' + attachment[0] + 'href--->' + attachment[1]
        print '\n'

def parseCurriculumService():
    uFile = urllib.urlopen("http://127.0.0.1:8000/seuknower_webservice/curriculum/213101579/11-12-2/")
    jsonresult = uFile.read()
    result = json.loads(jsonresult)
    # print json
    sideList = result[0]
    courseList = result[1]

    print sideList
    print courseList

    print '---sidebar---'
    for item in sideList:
        print item[0] + '---' + item[1] + '---' + item[2] + '---' + item[3]
    print '---sidebar---'

    morningList = courseList[0]
    afternoonList = courseList[1]
    eveningList = courseList[2]
    saturdayList = courseList[3]
    sundayList = courseList[4]

    print '---morning---'
    for i in xrange(len(morningList)):
        if i == 0:
            print 'monday'
            for course in morningList[0]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 1:
            print 'tuesday'
            for course in morningList[1]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 2:
            print 'wednesday'
            for course in morningList[2]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 3:
            print 'thursday'
            for course in morningList[3]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 4:
            print 'friday'
            for course in morningList[4]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]            

    print '---morning---'

    print '---afternoon---'
    for i in xrange(len(afternoonList)):
        if i == 0:
            print 'monday'
            for course in afternoonList[0]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 1:
            print 'tuesday'
            for course in afternoonList[1]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 2:
            print 'wednesday'
            for course in afternoonList[2]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 3:
            print 'thursday'
            for course in afternoonList[3]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 4:
            print 'friday'
            for course in afternoonList[4]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3] 

    print '---afternoon---'

    print '---eveningList---'
    for i in xrange(len(eveningList)):
        if i == 0:
            print 'monday'
            for course in eveningList[0]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 1:
            print 'tuesday'
            for course in eveningList[1]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 2:
            print 'wednesday'
            for course in eveningList[2]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 3:
            print 'thursday'
            for course in eveningList[3]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3]
        if i == 4:
            print 'friday'
            for course in eveningList[4]:
                print 'name--->' + course[0] + 'week--->' + course[1] + 'time--->' + course[2] + 'location--->' + course[3] 

    print '---afternoon---'

    print '---saturday---'
    for i in xrange(len(saturdayList)):
        print 'name--->' + saturdayList[i][0] + 'week--->' + saturdayList[i][1] + 'time--->' + saturdayList[i][2] + 'location--->' + saturdayList[i][3]
    print '---saturday---'

    print '---sunday---'
    for i in xrange(len(sundayList)):
        print 'name--->' + sundayList[i][0] + 'week--->' + sundayList[i][1] + 'time--->' + sundayList[i][2] + 'location--->' + sundayList[i][3]
        # for item in sundayList[i]:
        #     print item
    print '---sunday---'

import urllib2, cookielib, urllib
def parseLibraryService():
    '''check account is valid''' 
    # cj = cookielib.CookieJar()
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # urllib2.install_opener(opener)
    data = {
        'username' : '08010422',
        'password' : '08010422'
    }

    req = urllib2.Request("http://127.0.0.1:8000/seuknower_webservice/library/check_account/", urllib.urlencode(data))
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
    # timeout=8 set 8 seconds
    # if raise urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR 
    # 是因为django的csrf防护机制导致没法用爬虫模拟post提交需要在django中使用csrf_exempt
    try:
        res = urllib2.urlopen(req, timeout=8)
        '''if account is valid is true or account is invalid is false'''
        print res.read()
    # 有时候图书馆网站会抽风 可能会出现500
    except urllib2.HTTPError:
        print 'library server is down'

    '''search book and get booklist'''
    url = "http://127.0.0.1:8000/seuknower_webservice/library/search_book?strText='ios'"
    uFile = urllib.urlopen(url)
    jsonresult = uFile.read()
    # 有时候图书馆网站会抽风
    if jsonresult == 'server error':
        print 'library server is down'
    else:
        booklist = json.loads(jsonresult)
        print jsonresult


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
    # parseJwcService()
    parseLibraryService()
    # getbooklist()
    # parsebookitem()