import time
import json,requests
from fake_useragent import UserAgent

params={
        'sort': 'U',
        'range': '0, 10',
        'tags': '电影, 搞笑',
        'start': '20',
        'genres': '喜剧',
        'countries': '中国大陆',
        'year_range': '2018, 2018'
}
ua=UserAgent()
headers={
    'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
}
def crawl(url):
    response=requests.get(url,params=params,headers=headers)
    if response.status_code == 200:
        print(type(response.text))
        data=json.loads(response.text)['data']
        print((data))




if __name__ == '__main__':
    base_url='https://movie.douban.com/j/new_search_subjects'
    url='https://movie.douban.com/tag/#/'

    crawl(base_url)

