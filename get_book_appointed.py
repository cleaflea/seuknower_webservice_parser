# -*- coding: utf-8 -*-
import BeautifulSoup
# from BeautifulSoup import BeautifulSoup
import urllib
import re
import json
import urllib2, cookielib, urllib
import time

def parseappointed():
	html = '''
		<table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#CCCCCC">
				<tr>
					<td  bgcolor="#d8d8d8" class="greytext" width="10%">索书号</td>
					<td  bgcolor="#d8d8d8" class="greytext" width="15%">题名</td>
					<td  bgcolor="#d8d8d8" class="greytext" width="15%">责任者</td>
					<td  bgcolor="#d8d8d8" class="greytext" width="10%">馆藏地</td>
					<td  bgcolor="#d8d8d8" class="greytext" width="10%">预约(到书)日</td>
					<td  bgcolor="#d8d8d8" class="greytext" width="10%">截止日期</td>
					<td  bgcolor="#d8d8d8" class="greytext" width="10%">取书地</td>
					<td  bgcolor="#d8d8d8" class="greytext" width="10%">状态</td>
					<td  bgcolor="#d8d8d8" class="greytext" width="10%">取消预约</td>
				</tr>
  				<tr>
					<td bgcolor="#FFFFFF" class="whitetext">TP393.092/2105<input type="hidden" name="call_no" value=TP393.092/2105></td>
					<td bgcolor="#FFFFFF" class="whitetext"><a class="blue" href="../opac/item.php?marc_no=0000792503">&#x0052;&#x0075;&#x0062;&#x0079;&#x0020;&#x006f;&#x006e;&#x0020;&#x0052;&#x0061;&#x0069;&#x006c;&#x0073;&#x0020;&#x0057;&#x0065;&#x0062;&#x5f00;&#x53d1;&#x5b66;&#x4e60;&#x5b9e;&#x5f55; </a></td>
					<td bgcolor="#FFFFFF" class="whitetext">&#x795d;&#x7ea2;&#x6d9b;&#x002c;&#x0020;&#x4e8e;&#x5229;&#x654f;&#x002c;&#x0020;&#x6b66;&#x8fea;&#x7f16;&#x8457;</td>
					<td bgcolor="#FFFFFF" class="whitetext">中文图书阅览室（4）</td>
					<td bgcolor="#FFFFFF" class="whitetext">2013-11-15</td>
					<td bgcolor="#FFFFFF" class="whitetext">2013-12-15</td>
					<td bgcolor="#FFFFFF" class="whitetext">九龙湖总借还处</td>
					<td bgcolor="#FFFFFF" class="whitetext">申请中</td>
					<td bgcolor="#FFFFFF" class="whitetext">
					<div id="1"><input type="button" value="取消" onclick="javascript:getInLib('0000792503','TP393.092/2105','1','90013');"/>
					</div><span id="TP393.092/2105_1"></span> </td>
				</tr>
 
		</table>
	'''
	soup = BeautifulSoup.BeautifulSoup(html)
	book_table = soup.find('table', {'width':"100%", 'border':"0", 'cellpadding':"5",
	                   'cellspacing':"1", 'bgcolor':"#CCCCCC"})

	# print book_table
	book_trs = book_table.findAll('tr')
	# print book_trs
	book_trs.remove(book_trs[0])
	# print book_trs
	b = book_trs[0]
	book_tds = b.findAll('td')
	# print book_tds[8].div.input['onclick']
	jscontent = "javascript:getInLib('0000792503','TP393.092/2105','1','90013');"
	# 转义的括号表示待匹配字符串的首尾是括号，
	# 无转义的括号表示正则的一部分为以单引号开始单引号结束以逗号分隔的部分重复三次，
	# 最后一部分最后没有逗号，且都是非贪婪匹配
	pattern = re.compile(r"\((\'.*\'?\,){3}(\'.*\'?)\)")
	match = pattern.search(jscontent)
	print match.group()
	print type(match.group())
	# 执行字符串中的python代码，此处是执行以后输出了python对象，是一个元组对象，原本只是普通的python字符串
	data_list = eval(match.group())
	print data_list
	print type(data_list)

if __name__ == '__main__':
	parseappointed()
	t = "%13.0f" % (time.time()*1000)
	print t
	response = '''<link type="text/css" rel="stylesheet" href="../tpl/css/mylib.css" /><font color=green>已取消</font>'''
	print len(response)
	# if not find return -1
	print response.find('已取消')