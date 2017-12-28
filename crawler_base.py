from bs4 import BeautifulSoup
import urllib.request
import urllib.error

def get_info(item):
	page = item.find('a')['href']
	print('link is: ' + page)
	title = item.find('span','title').contents[0]
	print('title is: ' + title)
	infos = item.find('div', 'star').find_all('span')
	rate_score = infos[1].contents[0]
	print('score is: ' + rate_score)
	rate_num = infos[3].contents[0]
	print('rate people is: ' + rate_num)


hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]


url = 'https://movie.douban.com/'
url2 = 'https://movie.douban.com/top250?start=0&filter='

plain_text = ''

try:
	req = urllib.request.Request(url2, headers=hds[0])
	source_code = urllib.request.urlopen(req).read().decode('utf-8')
	plain_text=str(source_code)
	print('Get the plain_text! \n')
except urllib.error.URLError:
	print('URLError!')

# print(plain_text)

soup = BeautifulSoup(plain_text,"html5lib")
# print(soup)
soup_ls = soup.find('ol', 'grid_view')
items = soup_ls.find_all('div', 'item')

# print(items[0])
get_info(items[0])
# for item in items:




