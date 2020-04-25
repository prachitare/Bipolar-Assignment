from bs4 import BeautifulSoup
import requests
import time

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def make_card(url):
	time.sleep(5)
	r = requests.get(url)
	r = r.text

	soup = BeautifulSoup(r, 'html.parser')
	table = soup.table
	heads = table.findAll('tr')
	info_box = []

	for head in heads[:7]:
		info_box.append(head.get_text())

	#non reg ex way of dealing with expressions
	def removeNestedParentheses(s):
	    ret = ''
	    skip = 0
	    for i in s:
	        if i == '[':
	            skip += 1
	        elif i == ']'and skip > 0:
	            skip -= 1
	        elif skip == 0:
	            ret += i
	    return ret

	print len(info_box)
	if len(info_box) > 2:
		for x in range(7):
			info_box[x] = removeNestedParentheses(info_box[x])
		return info_box[2:]
	else:
		return " "
	# return info_box

# url = 'https://en.wikipedia.org/wiki/Amitabh_Bachchan'
# print make_card(url)