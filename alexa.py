import urllib.request, ssl
import re, sqlite3, time, sys, socket
#import socks	# pip install pysocks

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request_timeout = 5
error_retry = 99

def http_get(hyperlink):
	#ssl._create_default_https_context = ssl._create_unverified_context
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	for i in range(error_retry):
		try:
			req = urllib.request.Request(hyperlink, headers={'User-Agent': user_agent}, data=None)
			response = urllib.request.urlopen(req, context=ctx, timeout=request_timeout)
			return response.read().decode('utf-8')
		#except (urllib.error.HTTPError, urllib.error.URLError) as e:
		except Exception as e:
			sys.stderr.write('error: http_get()\n')
			time.sleep(2)

# params: {'key1':'val1','key2':'val2'}
def http_post(hyperlink, params):
	#ssl._create_default_https_context = ssl._create_unverified_context
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	for i in range(error_retry):
		try:
			req = urllib.request.Request(hyperlink, headers={'User-Agent': user_agent}, data=urllib.parse.urlencode(params).encode() )
			response = urllib.request.urlopen(req, context=ctx, timeout=request_timeout)
			return response.read().decode('utf-8')
		#except (urllib.error.HTTPError, urllib.error.URLError) as e:
		except Exception as e:
			sys.stderr.write('error: http_post()\n')
			time.sleep(2)




############
### MAIN ###
############


#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
#socket.socket = socks.socksocket

#data = {
#	'param1':'value1',
#	'param2':'value2',
#}

#text_res = http_post('https://test.com/search.php', data)
#print(text_res)


def alexa_rank(website):
	text_res = http_get('https://www.alexa.com/siteinfo/' + website)
	#text_res = http_get('https://www.alexa.com/siteinfo/' + sys.argv[1])

	global_rank = 0
	us_rank = 0

	m1 = re.search(r'"global": (\d+?),', text_res, re.MULTILINE | re.IGNORECASE | re.DOTALL)
	if m1:
		global_rank = m1.group(1)
		print(website, 'Global rank:', global_rank, sep=' ')
	
	s1 = re.findall(r'<li data-value="([\d,]+?)">\W*? ([\w ]+?) <', text_res, re.MULTILINE | re.IGNORECASE | re.DOTALL)
	if s1:
		for i in range(0, len(s1)):
			country_rank, country_name = s1[i]
			print(website, country_name + ' rank:', country_rank, sep=' ')
	
	if not m1:
		print(website, 'not ranked', sep=' ')










