import urllib, ssl
import re, sqlite3, time, sys, socket
import http.cookiejar
import socks	# pip install pysocks


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
REQUEST_TIMEOUT = 5
ERROR_RETRY = 99

cj = http.cookiejar.CookieJar()
ssl._create_default_https_context = ssl._create_unverified_context

def http_get (hyperlink):
	#ssl._create_default_https_context = ssl._create_unverified_context
	#ctx = ssl.create_default_context()
	#ctx.check_hostname = False
	#ctx.verify_mode = ssl.CERT_NONE
	for i in range(ERROR_RETRY):
		try:
			req = urllib.request.Request(hyperlink, headers={'User-Agent': USER_AGENT}, data=None)
			#response = urllib.request.urlopen(req, context=ctx, timeout=REQUEST_TIMEOUT)
			response = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)).open(req, timeout=REQUEST_TIMEOUT)
			#print(response.geturl())
			return response.read().decode('utf-8')
		except Exception as e:
			#sys.stderr.write(str(e)+'\n')
			raise(str(e))
			time.sleep(2)

# params: {'key1':'val1','key2':'val2'}
def http_post (hyperlink, params):
	#ssl._create_default_https_context = ssl._create_unverified_context
	#ctx = ssl.create_default_context()
	#ctx.check_hostname = False
	#ctx.verify_mode = ssl.CERT_NONE
	for i in range(ERROR_RETRY):
		try:
			req = urllib.request.Request(hyperlink, headers={'User-Agent': USER_AGENT}, data=urllib.parse.urlencode(params).encode() )
			#response = urllib.request.urlopen(req, context=ctx, timeout=REQUEST_TIMEOUT)
			response = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)).open(req, timeout=REQUEST_TIMEOUT)
			return response.read().decode('utf-8')
		except Exception as e:
			#sys.stderr.write(str(e)+'\n')
			raise(str(e))
			time.sleep(2)




############
### MAIN ###
############

#if __name__ == "__main__":
	#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
	#socket.socket = socks.socksocket

	#data = {
	#	'param1':'value1',
	#	'param2':'value2',
	#}

	#text_res = http_post('http://localhost/', data)
	#print(text_res)


	#text_res = http_get('http://localhost/')
	#print(text_res)





