# -*- coding: utf-8 -*-
# from BeautifulSoup import BeautifulSoup
import BeautifulSoup
import urllib
import re
import json
import urllib2, cookielib, urllib

def getbookrender():
	cj = cookielib.CookieJar()
	# save cookie to get another request which should login first
	# 登录之后只要每次都拿着带有sessionid的cookie去请求就可以去请求那些需要登录权限才能请求的页面了，其实浏览器也是这么干的
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	urllib2.install_opener(opener)
	data = {
		'number' : '08010422',
	    'passwd' : '08010422',
	    'select' : 'cert_no',
	    'returnUrl' : ''
	    }
	req = urllib2.Request("http://www.lib.seu.edu.cn:8080/reader/redr_verify.php", urllib.urlencode(data))
	req.add_header('User-Agent',
	                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
	res = urllib2.urlopen(req, timeout = 8)
	print res.read()

	result_url = "http://www.lib.seu.edu.cn:8080/reader/book_lst.php"
	urllib2.install_opener(opener)
	req = urllib2.Request(result_url)
	res = urllib2.urlopen(req, timeout=8)
	return res.read()

# 只要把不用remove处理过的打印出来看就行了，可以发现这些contents里有几个u'\n'，是要去除的
def __remove_navi_string(tag_list):
    '''Remove NavigableString in tag.contents especially u'\n'.

    Args:
        tag_list: the list of tags and nav_string gotten from tag.contents.
    '''

    tag_type = BeautifulSoup.Tag
    for tag in tag_list:
        if type(tag) is not tag_type:
            tag_list.remove(tag)
    return tag_list

def __get_book_tags(tag_list):
    __remove_navi_string(tag_list)
    # remove the titles see the source code of the web page you will find it
    tag_list.remove(tag_list[0])
    return tag_list

def decode_strange_str(s):
    s = s.replace('&#x','\u').replace(';','').replace('&nbsp','')
    u = s.decode('unicode-escape')
    return u

def parsebookrender():
	html = '''
			<table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#CCCCCC">
				<tr>
					<td bgcolor="#d8d8d8" class="greytext">条码号</td>
					<td bgcolor="#d8d8d8" class="greytext">题名/责任者</td>
					<td bgcolor="#d8d8d8" class="greytext">借阅日期</td>
					<td bgcolor="#d8d8d8" class="greytext">应还日期</td>
					<td bgcolor="#d8d8d8" class="greytext">续借次数</td>
					<td bgcolor="#d8d8d8" class="greytext">馆藏地</td>
					<td bgcolor="#d8d8d8" class="greytext">附件</td>
					<td bgcolor="#d8d8d8" class="greytext">续借</td>
				</tr>
				<tr>
					<td bgcolor="#FFFFFF" class="whitetext" width="10%">2287269</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="40%"><a class="blue" href="../opac/item.php?marc_no=0000651039">&#x950b;&#x5229;&#x7684;&#x006a;&#x0051;&#x0075;&#x0065;&#x0072;&#x0079;</a> / &#x5355;&#x4e1c;&#x6797;&#x002c;&#x0020;&#x5f20;&#x6653;&#x83f2;&#x002c;&#x0020;&#x9b4f;&#x7136;&#x7f16;&#x8457;</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%">2013-09-04</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%"><font color=red>2013-10-08        </font></td>
					<td bgcolor="#FFFFFF" class="whitetext" width="8%">0</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="15%">四牌楼中文自科书二室</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="13%">无</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="5%">
					<div id="1"><input type="button" value="续借" onclick="javascript:getInLib('2287269','1');"  disabled/>
					</div> <span id="2287269"></span> </td>
				</tr>
				<tr>
					<td bgcolor="#FFFFFF" class="whitetext" width="10%">2349068</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="40%"><a class="blue" href="../opac/item.php?marc_no=0000677535">&#x006a;&#x0051;&#x0075;&#x0065;&#x0072;&#x0079;&#x57fa;&#x7840;&#x6559;&#x7a0b;&#x002e;&#x7b2c;&#x0032;&#x7248;</a> / &#x0028;&#x7f8e;&#x0029;&#x0020;&#x004a;&#x006f;&#x006e;&#x0061;&#x0074;&#x0068;&#x0061;&#x006e;&#x0020;&#x0043;&#x0068;&#x0061;&#x0066;&#x0066;&#x0065;&#x0072;&#x002c;&#x0020;&#x004b;&#x0061;&#x0072;&#x006c;&#x0020;&#x0053;&#x0077;&#x0065;&#x0064;&#x0062;&#x0065;&#x0072;&#x0067;&#x8457;</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%">2013-09-04</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%"><font color=red>2013-10-08        </font></td>
					<td bgcolor="#FFFFFF" class="whitetext" width="8%">0</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="15%">四牌楼中文自科书二室</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="13%">无</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="5%">
					<div id="2"><input type="button" value="续借" onclick="javascript:getInLib('2349068','2');"  disabled/>
					</div> <span id="2349068"></span> </td>
				</tr>
				<tr>
					<td bgcolor="#FFFFFF" class="whitetext" width="10%">2382079</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="40%"><a class="blue" href="../opac/item.php?marc_no=0000687661">&#x9ed1;&#x5ba2;&#x0057;&#x0065;&#x0062;&#x811a;&#x672c;&#x653b;&#x51fb;&#x4e0e;&#x9632;&#x5fa1;&#x6280;&#x672f;&#x6838;&#x5fc3;&#x5256;&#x6790;</a> / &#x90dd;&#x6c38;&#x6e05;&#x7f16;&#x8457;</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%">2013-09-06</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%"><font color=red>2013-10-08        </font></td>
					<td bgcolor="#FFFFFF" class="whitetext" width="8%">0</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="15%">四牌楼中文自科书二室</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="13%">无</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="5%">
					<div id="3"><input type="button" value="续借" onclick="javascript:getInLib('2382079','3');"  disabled/>
					</div> <span id="2382079"></span> </td>
				</tr>
				<tr>
					<td bgcolor="#FFFFFF" class="whitetext" width="10%">2446733</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="40%"><a class="blue" href="../opac/item.php?marc_no=0000746565">&#x6df1;&#x5165;&#x6d45;&#x51fa;&#x004a;&#x0061;&#x0076;&#x0061;&#x0053;&#x0063;&#x0072;&#x0069;&#x0070;&#x0074;</a> / &#x004d;&#x0069;&#x0063;&#x0068;&#x0061;&#x0065;&#x006c;&#x0020;&#x004d;&#x006f;&#x0072;&#x0072;&#x0069;&#x0073;&#x006f;&#x006e;&#x8457;</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%">2013-09-04</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%"><font color=red>2013-10-08        </font></td>
					<td bgcolor="#FFFFFF" class="whitetext" width="8%">0</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="15%">四牌楼中文自科书二室</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="13%">无</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="5%">
					<div id="4"><input type="button" value="续借" onclick="javascript:getInLib('2446733','4');"  disabled/>
					</div> <span id="2446733"></span> </td>
				</tr>
				<tr>
					<td bgcolor="#FFFFFF" class="whitetext" width="10%">2452372</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="40%"><a class="blue" href="../opac/item.php?marc_no=0000750037">&#x0053;&#x0063;&#x0061;&#x006c;&#x0061;&#x7f16;&#x7a0b;</a> / &#x004d;&#x0061;&#x0072;&#x0074;&#x0069;&#x006e;&#x0020;&#x004f;&#x0064;&#x0065;&#x0072;&#x0073;&#x006b;&#x0079;&#x002c;&#x0020;&#x004c;&#x0065;&#x0078;&#x0020;&#x0053;&#x0070;&#x006f;&#x006f;&#x006e;&#x002c;&#x0020;&#x0042;&#x0069;&#x006c;&#x006c;&#x0020;&#x0056;&#x0065;&#x006e;&#x006e;&#x0065;&#x0072;&#x0073;&#x8457;</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%">2013-09-04</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%"><font color=red>2013-10-08        </font></td>
					<td bgcolor="#FFFFFF" class="whitetext" width="8%">0</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="15%">四牌楼中文自科书二室</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="13%">无</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="5%">
					<div id="5"><input type="button" value="续借" onclick="javascript:getInLib('2452372','5');"  disabled/>
					</div> <span id="2452372"></span> </td>
				</tr>
				<tr>
					<td bgcolor="#FFFFFF" class="whitetext" width="10%">2682621</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="40%"><a class="blue" href="../opac/item.php?marc_no=0000899305">&#x0048;&#x0054;&#x004d;&#x004c;&#x0020;&#x0026;&#x0020;&#x0043;&#x0053;&#x0053;&#x8bbe;&#x8ba1;&#x4e0e;&#x6784;&#x5efa;&#x7f51;&#x7ad9;</a> / &#x0028;&#x7f8e;&#x0029;&#x0020;&#x004a;&#x006f;&#x006e;&#x0020;&#x0044;&#x0075;&#x0063;&#x006b;&#x0065;&#x0074;&#x0074;&#x8457;</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%">2013-09-18</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%"><font color=red>2013-10-18        </font></td>
					<td bgcolor="#FFFFFF" class="whitetext" width="8%">0</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="15%">四牌楼中文自科书二室</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="13%">无</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="5%">
					<div id="6"><input type="button" value="续借" onclick="javascript:getInLib('2682621','6');"  disabled/>
					</div> <span id="2682621"></span> </td>
				</tr>
				<tr>
					<td bgcolor="#FFFFFF" class="whitetext" width="10%">2682685</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="40%"><a class="blue" href="../opac/item.php?marc_no=0000899373">&#x0069;&#x004f;&#x0053;&#x6e38;&#x620f;&#x7f16;&#x7a0b;&#x4e4b;&#x4ece;&#x96f6;&#x5f00;&#x59cb;&#x003a;&#x0043;&#x006f;&#x0063;&#x006f;&#x0073;&#x0032;&#x0064;&#x002d;&#x0078;&#x4e0e;&#x0063;&#x006f;&#x0063;&#x006f;&#x0073;&#x0032;&#x0064;&#x5f15;&#x64ce;&#x6e38;&#x620f;&#x5f00;&#x53d1;</a> / &#x674e;&#x534e;&#x660e;&#x7f16;&#x8457;</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%">2013-09-18</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="11%"><font color=red>2013-10-18        </font></td>
					<td bgcolor="#FFFFFF" class="whitetext" width="8%">0</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="15%">四牌楼中文自科书二室</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="13%">无</td>
					<td bgcolor="#FFFFFF" class="whitetext" width="5%">
					<div id="7"><input type="button" value="续借" onclick="javascript:getInLib('2682685','7');"  disabled/>
					</div> <span id="2682685"></span> </td>
				</tr>
			</table>
			'''
	soup = BeautifulSoup.BeautifulSoup(html)
	table = soup.findAll('table',{
		'width': "100%",
		'border': "0",
		'cellpadding': "5", 
		'cellspacing': "1",
		'bgcolor': "#CCCCCC"
	})

	# print table
	# print table[0]
	# print table[0].contents
	# print len(table[0].contents)
	# for content in table[0].contents:
	# 	print content

	# print '-----------------------------------------'

	book_tags = table[0].contents
	__get_book_tags(book_tags)	
	# for book_tag in book_tags:
	book_tag = book_tags[0]
	book_info_tags = book_tag.contents

	print book_info_tags
	__remove_navi_string(book_info_tags)

	print '------------------------'
	
	print book_info_tags
	# print book_info_tags[0].string.strip().encode('utf-8')
	# print decode_strange_str(book_info_tags[1].a.string).strip().encode('utf-8')
	# print decode_strange_str(book_info_tags[1].contents[1].string).strip().encode('utf-8')[1:].strip()
	# print book_info_tags[2].string.strip().encode('utf-8')
	# print book_info_tags[3].font.string.strip().encode('utf-8')
	# print book_info_tags[4].string.strip().encode('utf-8')
	# print book_info_tags[5].string.strip().encode('utf-8')
	# print book_info_tags[6].string.strip().encode('utf-8')

def innerfunction():
	def removeitem(list):
		list.remove(list[0])
		return list
	a = [0, 1, 2, 3, 4, 5, 6]

	# python中函数会改变传入的参数，就算不在外部获得返回值也是一样的效果
	# a = removeitem(a)
	removeitem(a)
	print a

if __name__ == '__main__':
	parsebookrender()
	# innerfunction()