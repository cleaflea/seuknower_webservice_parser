import cookielib
import urllib
import urllib2

def login():
	data = {
        'xh': "213101579",
        'mm': "8888888",
        'method': 'login'
    }
	cookieJar = cookielib.CookieJar()
	cookieHandler = urllib2.HTTPCookieProcessor(cookieJar)
	opener = urllib2.build_opener(cookieHandler)
	urllib2.install_opener(opener)
	reqLogin = urllib2.Request("http://58.192.114.239:8088/sms2/studentLogin.do", urllib.urlencode(data))
	resLogin = urllib2.urlopen(reqLogin, timeout=8)
	html = resLogin.read()

	print html
	print len(html)

def renrenbroadcast():
	REN_TYB_URL = "https://api.renren.com/v2/status/list?" \
              "access_token=241511|6.e9d163eb32a823d37609a396abe20618.2592000.1381683600-365328826" \
              "&ownerId=601258593"

	req = urllib2.Request(REN_TYB_URL)
	res = urllib2.urlopen(req, timeout=8)
	print res.read()

if __name__ == '__main__':
	# login()
	renrenbroadcast()