from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import random
import time
from io import StringIO

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

def get_soup(url):
    plain_text = ''
    try:
        req = urllib.request.Request(url, headers=hds[0])
        source_code = urllib.request.urlopen(req).read().decode('utf-8')
        plain_text=str(source_code)
        # print('Get the plain_text! \n')
    except urllib.error.URLError:
        print('URLError!')
        return None
    soup = BeautifulSoup(plain_text,"html5lib")
    return soup

def get_one_comment(item):
	votes = item.find('span','votes').string

	infos = item.find('span','comment-info')
	user = infos.find('a')
	username = user.string
	user_link = user['href']
	score = int(infos.find('span','rating')['class'][0][-2:])/10
	time = infos.find('span', 'comment-time')['title']
	comment = item.find('p','').string.strip()
	print('user: ' + username)
	print('comment: ' + comment)
	print('rating: ' + str(score))
	print('votes: ' + votes)
	print('times: ' + time)

def get_all_comment(link):
    start = 0
    # unsign in user can only view top 200 comments
    while start <= 200:
        post_link = 'comments?start=' + str(start) + '&limit=20&sort=new_score&status=P&percent_type='
        url = link + post_link
        wait_time = random.random() * 3
        print('wait_time: ' + str(wait_time))
        time.sleep(wait_time)
        soup = get_soup(url)

        items = soup.find_all('div', 'comment-item')
        get_one_comment(items[0])
        start += 20
        break


def get_info(item):
    link = item.find('a')['href']
    print('link is: ' + link)
    title = item.find('span','title').string
    print('title is: ' + title)
    infos = item.find('div', 'star').find_all('span')
    rate_score = infos[1].string
    print('score is: ' + rate_score)
    rate_num = infos[3].string
    print('rate people is: ' + rate_num)

    get_all_comment(link)

def get_movies(url):
    soup = get_soup(url)

    if soup:
        soup_ls = soup.find('ol', 'grid_view')
        items = soup_ls.find_all('div', 'item')
        get_info(items[0])



if __name__ == '__main__':
    url = 'https://movie.douban.com/top250?start=0&filter='
    get_movies(url)
