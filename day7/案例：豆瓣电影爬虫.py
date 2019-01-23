
import requests
import json

def crawl(index):
    '''
    豆瓣电影的爬取
    :param index:
    :return:
    '''
    base_url = 'https://movie.douban.com/j/new_search_subjects'
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    keywords ={
        'sort': 'U',
        'range': '0, 10',
        'tags': '电影, 搞笑',
        'start': '20',
        'genres': '喜剧',
        'countries': '中国大陆',
        'year_range': '2018, 2018'
    }
    response = requests.get(base_url,params=keywords,headers=headers)
    if response.status_code ==200:
        print(response.text)
        data = json.loads(response.text)["data"]

        print(len(data))
        for item in data:
            # {"directors": ["朱延平"],
            #  "rate": "3.6",
            #  "cover_x": 1072,
            #  "star": "20",
            #  "title": "新乌龙院之笑闹江湖",
            #  "url": "https:\/\/movie.douban.com\/subject\/26309969\/",
            #  "casts": ["王宁", "孔连顺", "王智", "吴孟达", "梁超"],
            #  "cover": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2529762680.jpg",
            #  "id": "26309969",
            #  "cover_y": 1500}
            directors = ','.join(item["directors"])
            rate = item["rate"]
            star = item['star']
            title = item['title']
            url = item['url']
            casts = ','.join(item["casts"])
            cover = item['cover']
            id = item['id']
            print("directors:",directors)
            print("rate:", rate)
            print("star:", star)
            print("title:", title)
            print("url:", url)
            print("casts:", casts)
            print("cover:", cover)
            print("id:", id)
            print('='*60)


if __name__ == '__main__':
    for i in range(3):
        crawl(i)

