# -*- coding: utf-8 -*-
import cookielib
import urllib
import urllib2
import json

# use the renren api

app_id = 244206
app_key = 'bf9cb42781fd48f2b1a6739d7bffede9'
secret_key = '232840ccda984453804c35eeb48a7322'
refresh_token = '244206|0.uyE2sQqbHlNJlSwocrs5W0vTAI7GeH45.552031874.1384609588695'
access_token = '244206|6.4fdcb2410bcbe093dca4428757ece23e.2592000.1387216800-552031874'

def authorizeRequest():

	url = "https://graph.renren.com/oauth/authorize?" \
		  "client_id=bf9cb42781fd48f2b1a6739d7bffede9&redirect_uri=www.mrfruit.cn&response_type=code"
	
	uFile = urllib.urlopen(url)
	print uFile.read()

def refresh(rfs_token):
	# app_key
    client_id = 'bf9cb42781fd48f2b1a6739d7bffede9'
    # secret_key
    client_secret = '232840ccda984453804c35eeb48a7322'
    refresh_url = "https://graph.renren.com/oauth/token?grant_type=refresh_token&refresh_token=%s&client_id=%s&client_secret=%s"%(rfs_token, client_id, client_secret)
    result = urllib2.urlopen(refresh_url).read()
    result = json.loads(result)
    new_token = result['access_token']
    return new_token

def press(content, token):
	page_id = '601792587'
	# content += ' 来自微信'.decode('utf-8')
	data = {
	        'v':'1.0',
	        'access_token':token,
	        'format':'JSON',
	        'status':content.encode('utf-8'),
	        'page_id':page_id, 
	        'method':'status.set'
	        }
	data = urllib.urlencode(data)
	url = 'https://api.renren.com/restserver.do'
	req = urllib2.Request(url, data)
	result = urllib2.urlopen(req).read()
	if 'error_code' in result:
	    print result # 出错信息
	    return 'error'
	return 'okay'	

def getstatus(token):
	url = "https://api.renren.com/v2/status/list?" \
          "access_token=%s" \
          "&ownerId=601792587" % token
	print url
	uFile = urllib.urlopen(url)
	return json.loads(uFile.read())
	# print uFile.read()

def parsestatuslist():
	try:
		statuslist = getstatus(access_token)['response']
		print 'cleantha'
	except:
		new_access_token = refresh(refresh_token)
		print new_access_token
		statuslist = getstatus(new_access_token)['response']

	for status in statuslist:
		print '--------------------------'
		for key, value in status.items():
			# print unicode(key, 'utf-8') + '--->' + unicode(value, 'utf-8')
			print key + '--->' + (lambda x: str(x) if type(x) == int or type(x) == long else x)(value)


def getcheckinlist(token):
	# pass
	url = " https://api.renren.com/v2/checkin/list?" \
	      "access_token=%s" \
	      "&pageNo=%s&pageSize=%s" % (token, '1', '3')
	print url
	uFile = urllib.urlopen(url)
	return json.loads(uFile.read())

def parsecheckinlist():
	# pass
	try:
		checkinlist = getcheckinlist(access_token)
	except:
		new_access_token = refresh(refresh_token)
		checkinlist = getcheckinlist(new_access_token)

	print checkinlist

if __name__ == '__main__':
	# authorizeRequest()
	# output 1 2 3 4 5 not include 6
	# for i in xrange(1, 6):
	# 	print i
	# getstatus(new_access_token)
	# press('33', new_access_token)
		# print status
		# print 'id--->' + str(status['id']) + 'ownerId--->' + str(status['ownerId']) + \
		# 	  'content--->' + str(status['content']) + 'createTime--->' + str(status['createTime']) + \
		# 	  'shareCount--->' + str(status['shareCount']) + 'commentCount--->' + str(status['commentCount']) + \
		# 	  'sharedStatusId--->' + str(status['sharedStatusId']) + 'sharedUserId' + str(status['sharedUserId'])

	parsestatuslist()
	parsecheckinlist()

# https://graph.renren.com/oauth/authorize?client_id=bf9cb42781fd48f2b1a6739d7bffede9&redirect_uri=http://www.mrfruit.cn&response_type=code&scope=status_update+photo_upload+admin_page+read_user_status+read_user_blog+read_user_checkin+read_user_feed+read_user_guestbook+read_user_invitation+read_user_like_history+read_user_message+read_user_notification+read_user_photo+read_user_album+read_user_comment+read_user_share+read_user_request