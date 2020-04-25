import bs4
import requests
import myscrap
import csv
import sys
import download_image
import urllib

reload(sys)
sys.setdefaultencoding('utf8')

big_url = 'https://en.wikipedia.org/wiki/List_of_Indian_film_actors'
ini_url = 'https://en.wikipedia.org'

r = requests.get(big_url)
r = r.text

soup = bs4.BeautifulSoup(r, 'lxml')
i = 0
for anchor in soup.findAll('a'):
  last_url = anchor.get('href')
  final_url = ini_url+str(last_url)
  if len(final_url) > 40 and len(final_url) < 50:
  	i += 1
  	if i > 7:
  		print final_url
  		img_src_url = download_image.image_func(final_url)
  		img_name = 'i' + '.jpg'                                                   
  		urllib.urlretrieve(img_src_url, img_name)
  	#print myscrap.make_card(final_url)
  	print 'done'

	with open('traits.csv', 'ab') as myfile:
	    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	    wr.writerow(myscrap.make_card(final_url))

  if 'Zubeen_Garg' in final_url:
  	break