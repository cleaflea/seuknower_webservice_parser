# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib
import re
import json
import urllib2, cookielib, urllib

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
    url = "http://127.0.0.1:8000/seuknower_webservice/library/search_book?strText=ios"
    uFile = urllib.urlopen(url)
    jsonresult = uFile.read()
    # 有时候图书馆网站会抽风
    if jsonresult == 'server error':
        print 'library server is down'
    else:
        booklist = json.loads(jsonresult)
        print booklist

        for book in booklist:
            print '-----------------------'
            for key, value in book.items():
                print key + '--->' + value

    '''get book detail'''
    url = "http://127.0.0.1:8000/seuknower_webservice/library/book_detail/?marc_no=0000917439"
    uFile = urllib.urlopen(url)
    jsonresult = uFile.read()
    # print jsonresult
    if jsonresult =='server error':
        print 'library server is down'
    else:
        bookdetail = json.loads(jsonresult)
        # print bookdetail['detail']
        # print bookdetail['stores']
        for key, value in bookdetail['detail'].items():
            print key + '--->' + value

        for store in bookdetail['stores']:
            print '------------------------'
            for key, value in store.items():
                print key + '--->' + value

    # borrow book
    '''get book render'''
    url = "http://127.0.0.1:8000/seuknower_webservice/library/rendered_books/"

    data = {
        'username' : '08010422',
        'password' : '08010422'
    }

    req = urllib2.Request(url, urllib.urlencode(data))
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
    # timeout=8 set 8 seconds
    # if raise urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR 
    # 是因为django的csrf防护机制导致没法用爬虫模拟post提交需要在django中使用csrf_exempt

    res = urllib2.urlopen(req, timeout=8)
    borrowlist = json.loads(res.read())
    for borrowitem in borrowlist:
        print '-----------------'
        for key, value in borrowitem.items():
            print key + '--->' + value

    # 续借
    '''renew book'''
    url = "http://127.0.0.1:8000/seuknower_webservice/library/renew/"

    data = {
        'username' : '08010422',
        'password' : '08010422',
        'barcode' : '2287269'
    }

    req = urllib2.Request(url, urllib.urlencode(data))
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
    # timeout=8 set 8 seconds
    # if raise urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR 
    # 是因为django的csrf防护机制导致没法用爬虫模拟post提交需要在django中使用csrf_exempt
    res = urllib2.urlopen(req, timeout=8)
    renewresult = json.loads(res.read())
    print renewresult['result']

    # 预约
    '''check book appointed'''
    url = "http://127.0.0.1:8000/seuknower_webservice/library/appointed_books/"

    data = {
        'username' : '08010422',
        'password' : '08010422'
    }

    req = urllib2.Request(url, urllib.urlencode(data))
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
    # timeout=8 set 8 seconds
    # if raise urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR 
    # 是因为django的csrf防护机制导致没法用爬虫模拟post提交需要在django中使用csrf_exempt
    res = urllib2.urlopen(req, timeout=8)
    appointedresult = json.loads(res.read())
    for appointed in appointedresult:
        print '---------------------'
        for key, value in appointed.items():
            # python 判断类型是否是dict
            if type(value) == dict:
                print key + '--->'
                for newkey, newvalue in value.items():
                    print newkey + '--->' + newvalue
            else:
                print key + '--->' + value

    # 取消预约
    '''cancel book appointed'''
    url = "http://127.0.0.1:8000/seuknower_webservice/library/cancel_appoint/"

    '''call_no, marc_no, loca 从check book appointed中获取'''
    data = {
        'username' : '08010422',
        'password' : '08010422',
        'call_no' : 'TP393.092/2105',
        'marc_no' : '0000792503',
        'loca' : '90013'
    }

    req = urllib2.Request(url, urllib.urlencode(data))
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
    # timeout=8 set 8 seconds
    # if raise urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR 
    # 是因为django的csrf防护机制导致没法用爬虫模拟post提交需要在django中使用csrf_exempt
    res = urllib2.urlopen(req, timeout=8)
    cancelresult = json.loads(res.read())
    print cancelresult['result']

    # 获取一本书的预约信息
    '''get book appoint info'''
    url = "http://127.0.0.1:8000/seuknower_webservice/library/appoint_info/"

    data = {
        'username' : '08010422',
        'password' : '08010422',        
        'marc_no' : '0000792503'
    }

    req = urllib2.Request(url, urllib.urlencode(data))
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
    # timeout=8 set 8 seconds
    # if raise urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR 
    # 是因为django的csrf防护机制导致没法用爬虫模拟post提交需要在django中使用csrf_exempt
    res = urllib2.urlopen(req, timeout=8)
    # print res.read()
    booklist = json.loads(res.read())
    for book in booklist:
        print '----------'
        for key, value in book.items():
            if type(value) == list:
                print key + '--->'
                for item in value:
                    print item
            else:
                print key + '--->' + value
    # 预约一本书
    '''book appoint'''
    url = "http://127.0.0.1:8000/seuknower_webservice/library/appoint_book/"
    # 馆藏地编号和校区编号由图书馆代码得来，
    # take_loca: 90001-九龙湖总借还处, 00916-丁家桥中文借书处, 00940-四牌楼总借还处
    # location 是图书存放的地方，比如中文图书阅览室（4）之类的。
    # call_no 是索书号
    # check 感觉就是1 没什么用啊 预约的时候那个radio不按的话就没有check这个参数了，不知道check这个参数有什么用
    data = {
        'username' : '08010422',
        'password' : '08010422',        
        'call_no' : 'TP393.092/2105',
        'location' : '90013',
        'check' : '1',
        'take_loca' : '90001'
    }

    req = urllib2.Request(url, urllib.urlencode(data))
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
    # timeout=8 set 8 seconds
    # if raise urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR 
    # 是因为django的csrf防护机制导致没法用爬虫模拟post提交需要在django中使用csrf_exempt
    res = urllib2.urlopen(req, timeout=8)
    # print res.read()
    appointresult = json.loads(res.read())
    print appointresult['result']

def parseTyxService():
    '''tyx login'''
    url = "http://127.0.0.1:8000/seuknower_webservice/tyx/checkAccount/"
    data = {
        'card_number' : '213101579',
        'password' : '213101579',        

    }
    req = urllib2.Request(url, urllib.urlencode(data))
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
    res = urllib2.urlopen(req, timeout=8)
    # print res.read()
    loginresult = res.read()
    print loginresult

    '''get morning running count'''
    url = "http://127.0.0.1:8000/seuknower_webservice/tyx/%s/%s/" % ('213101579', '213101579')
    uFile = urllib.urlopen(url)
    print 'morning running count===> ' + str(uFile.read())

if __name__ == '__main__':
    # parseJwcService()
    # parseLibraryService()
    # parseLibraryService()
    parseTyxService()
    # python 判断类型是否是dict
    # print type({'clea': 'cleantha'}) == dict
