
import sys
import crawler
import xml.etree.ElementTree as ET



def alexa_rank(website):
	text_res = crawler.http_get('http://data.alexa.com/data?cli=10&url=' + website)
		
	#print(text_res)
	
	tree = ET.ElementTree(ET.fromstring(text_res))
	root = tree.getroot()

	#web = root.find('SD/POPULARITY').get('URL')
	#web = web[0:-1]
	global_rank = root.find('SD/POPULARITY').get('TEXT')
	local_country = root.find('SD/COUNTRY').get('NAME')
	local_rank = root.find('SD/COUNTRY').get('RANK')
	
	
	print("{} Global rank: {}".format(website, global_rank))
	print("{} {} rank: {}".format(website, local_country, local_rank))
	

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

#argv = ['matahari.com', 'tokopedia.com']

if __name__ == '__main__':
	if len(sys.argv) <= 1:
	#if len(argv) <= 1:
		print('usage: \n  alexa website1.com website2.com')
	else:
		#for i in argv:
		for i in sys.argv[1:]:
			alexa_rank(i)
			#alexa_rank(sys.argv[i])
			#print(i)




#print(root.findall('.//POPULARITY'))

#for type_tag in root.findall('SD/POPULARITY'):
#	value = type_tag.get('URL')
#	print(value)


'''
https://www.alexa.com/minisiteinfo/matahari.com

http://data.alexa.com/data?cli=10&url=matahari.com
http://data.alexa.com/data?cli=10&dat=snbamz&url=matahari.com


'''
