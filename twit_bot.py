import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://www.pexels.com/popular-photos/'
page = requests.get(url)
soup = bs(page.text, 'html.parser')
image_tags = soup.findAll('img')

if not os.path.exists('pics'): 
	os.makedirs('pics')

os.chdir('pics')

x = 0
for image in image_tags: 
	try: 
		url = image['src']
		source = requests.get(url)
		if source.status_code == 200
			with open 'img-' + str(x) + '.jpg', 'wb') as f:
				f.write(requests.get(url).content)
				f.close()
				x +=1
	except: 
		pass