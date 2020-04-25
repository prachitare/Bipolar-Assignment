from bs4 import BeautifulSoup as bs
import urllib2

def image_func(url):
	imgurl = url
	page = urllib2.urlopen(imgurl)

	soup = bs(page, "lxml")
	for a in soup.find_all('a', {"class": "image"}):
	    #if a.img:
	   	load_url = a.img['src'][2:]
	   	if load_url == None:
	   		return 'https://miro.medium.com/max/560/1*MccriYX-ciBniUzRKAUsAw.png'
		if 'svg' not in load_url:
			print(load_url)
			return(load_url)