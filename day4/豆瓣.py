import requests, time, csv, random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def soups(url):
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    htmls = response.text
    soup = BeautifulSoup(htmls, 'lxml')
    return soup


def getinfor(url):
    baseurl = 'https://book.douban.com'
    soup = soups(url)
    links = soup.select('table[class="tagCol"] tr td a')
    print(len(links))
    for i in links:
        link = baseurl + i['href']
        save_info(link)
        print('=' * 60)


def save_info(url):
    global n
    n += 1
    soup = soups(url)
    all = soup.select('li[class="subject-item"]')
    for i in all:
        name = i.select('div[class="info"] h2 a ')[0].text.split()
        name = ''.join(name)
        intro = i.select('div[class="pub"]')[0].string
        content = i.select('div[class="info"] p')
        content = content[0].string if len(content) > 0 else '空'
        num = i.select('span[class="rating_nums"]')
        num = num[0].string if len(num) > 0 else '空'
        with open('csv/douban.csv', 'a+', encoding='utf-8', newline='') as f_w:
            writers = csv.writer(f_w, dialect='excel')
            writers.writerow([name, intro, num])
    print('一页存储完毕')


    next_page = soup.select('span[class="next"] a')
    if len(next_page) > 0:
        next_url = base_url + next_page[0]['href']
        print('开始爬取第%s' % n)
        print(next_url)
        time.sleep(random.random() * 5)
        save_info(next_url)



if __name__ == '__main__':
    n = 1
    url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    base_url = 'https://book.douban.com'
    getinfor(url)
