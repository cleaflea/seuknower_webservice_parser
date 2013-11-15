# -*- coding: utf-8 -*-
# from BeautifulSoup import BeautifulSoup
import book
import BeautifulSoup
import urllib
import re
import json
import urllib2, cookielib, urllib

def parsebookappointinfo():
  html = '''<table width="98%" border="0" align="center" cellpadding="2" cellspacing="1" bgcolor="#CCCCCC" class="table-line">
           <form action="userpreg_result.php" method="get" name="form1">
          <input type="hidden" name="marc_no" value="0000792503" />
          <input type="hidden" name="count" value="1" />
          
                    <tr>
              <td align="center" bgcolor="#d8d8d8" class="greytext1">索书号</td>
              <td align="center" bgcolor="#d8d8d8" class="greytext1">馆藏地</td>
              <td align="center" bgcolor="#d8d8d8" class="greytext1">可借复本</td>
              <td align="center" bgcolor="#d8d8d8" class="greytext1">在馆复本</td>
              <td align="center" bgcolor="#d8d8d8" class="greytext1">已预约数</td>
              <td align="center" bgcolor="#d8d8d8" class="greytext1">可否预约</td>
              <td align="center" bgcolor="#d8d8d8" class="greytext1">取书地</td>
              <td align="center" bgcolor="#d8d8d8" class="greytext1">预约</td>
      </tr>
      
            <tr>
                <td align="center" bgcolor="#FFFFFF" class="whitetext" width="15%">TP393.092/2105</td>
                <td align="center" bgcolor="#FFFFFF" class="whitetext" width="20%">中文图书阅览室（4）</td>
                <td align="center" bgcolor="#FFFFFF" class="whitetext" width="5%">2</td>
                <td align="center" bgcolor="#FFFFFF" class="whitetext" width="5%">0</td>
                <td align="center" bgcolor="#FFFFFF" class="whitetext" width="5%">0</td>
                <td align="center" bgcolor="#FFFFFF" class="whitetext" width="30%">预约纪录保留天数(最多30天)<input name="preg_days1" size="1" value="30" /></td>
                <td align="center" bgcolor="#FFFFFF" class="whitetext" width="15%"><select style="width:120px" name="take_loca1"> <option value="90001">九龙湖总借还处</option><option value="00916">丁家桥中文借书处</option><option value="00940">四牌楼总借还处</option></select></td>
                <td align="center" bgcolor="#FFFFFF" class="whitetext" width="5%">
                  <input type="hidden" name="callno1" value="TP393.092/2105" />
                  <input type="hidden" name="location1" value="90013" />
                  <input type="hidden" name="pregKeepDays1" value="7" />
                  <input type="radio" name="check" value="1"  />
                </td>
             </tr>
            <tr>
        <td  colspan="7" align="center" >
                        <span id="emailzone">
                  便于更好地为您服务，请补充您的Email：<input type="text" id="email" />
                  <input type="button" onclick="updateEmail();" value="更新" />
                  </span>
                      </td>
        <td >
          <input type="submit" value="执行预约" />
        </td>
      </tr>
            </form>
       </table> 
       '''

  soup = BeautifulSoup.BeautifulSoup(html)
  renew_table = soup.find('table', {'width':"98%", 'border':"0", 'align':"center",
                                    'cellpadding':"2", 'cellspacing':"1",
                                    'bgcolor':"#CCCCCC", 'class':"table-line"})
  items = renew_table.findAll('tr')
  # print items
  # print items[1]
  td_items = items[1].findAll('td')
  # for td_item in td_items:
  #   print td_item

  # print td_items[0]  

  html = '''<td align="center" bgcolor="#FFFFFF" class="whitetext" width="30%">预约纪录保留天数(最多30天)<input name="preg_days1" size="1" value="30" /></td>'''
  soup = BeautifulSoup.BeautifulSoup(html)
  for content in soup.td.contents:
    print content
  #print items
  # appoint_item_list = []
  # for i in range(1, len(items)-1):
  #     item = items[i]
  #     td_items = item.findAll('td')
  #     print item
  #     print '-----------------'
  #     places = []
  #     # 应该是又有一个'\n'所以是第七个元素而不是第六个
  #     # 馆藏地编号和校区编号由图书馆代码得来，take_loca:
  #     # 90001-九龙湖总借还处, 00916-丁家桥中文借书处, 00940-四牌楼总借还处
  #     # 就是从这几个option中得到的，直接明文写在html页面中了
  #     tmp = td_items[6].findAll('option')
  #     for tag in tmp:
  #         places.append(tag['value'].encode('utf-8').strip())
  #     appoint_item = book.AppointInfoItem(
  #         td_items[0].string.encode('utf-8').strip(),
  #         td_items[1].string.encode('utf-8').strip(),
  #         td_items[7].findAll('input')[1]['value'].encode('utf-8').strip(),
  #         td_items[2].string.encode('utf-8').strip(),
  #         td_items[3].string.encode('utf-8').strip(),
  #         td_items[4].string.encode('utf-8').strip(),
  #         extract_string(td_items[5]).encode('utf-8').strip(),
  #         places,
  #         td_items[7].findAll('input')[3]['disabled'].encode('utf-8').strip()
  #     )
  #     print appoint_item
  #     appoint_item_list.append(appoint_item)
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


def test():
  html = '''
        <table width="98%" border="0" align="center" cellpadding="2" cellspacing="1" bgcolor="#CCCCCC" class="table-line">
             <form action="userpreg_result.php" method="get" name="form1">
            <input type="hidden" name="marc_no" value="0000792503" />
            <input type="hidden" name="count" value="1" />
            
                      <tr>
                <td align="center" bgcolor="#d8d8d8" class="greytext1">索书号</td>
                <td align="center" bgcolor="#d8d8d8" class="greytext1">馆藏地</td>
                <td align="center" bgcolor="#d8d8d8" class="greytext1">可借复本</td>
                <td align="center" bgcolor="#d8d8d8" class="greytext1">在馆复本</td>
                <td align="center" bgcolor="#d8d8d8" class="greytext1">已预约数</td>
                <td align="center" bgcolor="#d8d8d8" class="greytext1">可否预约</td>
                <td align="center" bgcolor="#d8d8d8" class="greytext1">取书地</td>
                <td align="center" bgcolor="#d8d8d8" class="greytext1">预约</td>
        </tr>
        
              <tr>
                  <td align="center" bgcolor="#FFFFFF" class="whitetext" width="15%">TP393.092/2105</td>
                  <td align="center" bgcolor="#FFFFFF" class="whitetext" width="20%">中文图书阅览室（4）</td>
                  <td align="center" bgcolor="#FFFFFF" class="whitetext" width="5%">2</td>
                  <td align="center" bgcolor="#FFFFFF" class="whitetext" width="5%">0</td>
                  <td align="center" bgcolor="#FFFFFF" class="whitetext" width="5%">0</td>
                  <td align="center" bgcolor="#FFFFFF" class="whitetext" width="30%">预约纪录保留天数(最多30天)<input name="preg_days1" size="1" value="30" /></td>
                  <td align="center" bgcolor="#FFFFFF" class="whitetext" width="15%"><select style="width:120px" name="take_loca1"> <option value="90001">九龙湖总借还处</option><option value="00916">丁家桥中文借书处</option><option value="00940">四牌楼总借还处</option></select></td>
                  <td align="center" bgcolor="#FFFFFF" class="whitetext" width="5%">
                    <input type="hidden" name="callno1" value="TP393.092/2105" />
                    <input type="hidden" name="location1" value="90013" />
                    <input type="hidden" name="pregKeepDays1" value="7" />
                    <input type="radio" name="check" value="2" />
                  </td>
               </tr>
              <tr>
          <td  colspan="7" align="center" >
                          <span id="emailzone">
                    便于更好地为您服务，请补充您的Email：<input type="text" id="email" />
                    <input type="button" onclick="updateEmail();" value="更新" />
                    </span>
                        </td>
          <td >
            <input type="submit" value="执行预约" />
          </td>
        </tr>
              </form>
         </table> 
         '''

  soup = BeautifulSoup.BeautifulSoup(html)
  renew_table = soup.find('table', {'width':"98%", 'border':"0", 'align':"center",
                                    'cellpadding':"2", 'cellspacing':"1",
                                    'bgcolor':"#CCCCCC", 'class':"table-line"})
  items = renew_table.findAll('tr')
  #print items
  appoint_item_list = []
  # 会根据馆藏地又多个而有多个<tr></tr>
  for i in range(1, len(items)-1):
      item = items[i]
      td_items = item.findAll('td')
      print item
      print '-----------------'

      print 'cleantha'

      places = []
      # 馆藏地编号和校区编号由图书馆代码得来，take_loca:
      # 90001-九龙湖总借还处, 00916-丁家桥中文借书处, 00940-四牌楼总借还处
      # 就是从这几个option中得到的，直接明文写在html页面中了
      tmp = td_items[6].findAll('option')
      for tag in tmp:
          places.append(tag['value'].encode('utf-8').strip())
      appoint_item = book.AppointInfoItem(
          td_items[0].string.encode('utf-8').strip(),
          td_items[1].string.encode('utf-8').strip(),
          td_items[7].findAll('input')[1]['value'].encode('utf-8').strip(),
          td_items[2].string.encode('utf-8').strip(),
          td_items[3].string.encode('utf-8').strip(),
          td_items[4].string.encode('utf-8').strip(),
          extract_string(td_items[5]).encode('utf-8').strip(),
          places,
          # td_items[7].findAll('input')[3]['disabled'].encode('utf-8').strip()
          (lambda x : 1 if x==3 else 0)(len(td_items[7].findAll('input')[3].attrs))
          # len(td_items[7].findAll('input')[3].attrs) == 3 ? 1 : 0
      )
      # print appoint_item
      appoint_item_list.append(appoint_item)
  return appoint_item_list
      # print td_items[7].findAll('input')[3]['disabled'].encode('utf-8').strip()
      # print td_items[7].findAll('input')[3].attrs
      # if "(u'disabled', u'disabled')" in td_items[7].findAll('input')[3].attrs:
      #   print 'true'
      # else:
      #   print 'false'
      # print len(td_items[7].findAll('input')[3].attrs) == 3 ? 1 : 0

if __name__ == '__main__':
  # parsebookappointinfo()
  print str(test()[0])

  # 反斜杠就是续行符用于连接字符串
  s = 'cleantha' + \
      'clea' + \
      'kkk'
  print s
  print (lambda x: 1 if x==3 else 0)(4)