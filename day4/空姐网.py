import requests, time, csv, random, os
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def soups(url):
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'
    htmls = response.text
    soup = BeautifulSoup(htmls, 'lxml')
    return soup


def get_info(url):
    soup = soups(url)
    # 外部相册链接
    link_out = soup.select('div[class="c"] a')
    print(len(link_out))
    for i in link_out:
        link1 = i['href']
        print(link1, 1111111111111111)
        soup1 = soups(link1)
        # 内部相册链接
        link_inner = soup1.select('div[class="c"] p a')
        print(len(link_inner), '内部相册个数')
        # 判断内部相册个数
        if len(link_inner) == 0:
            continue
        for j in link_inner:
            link2 = j['href']
            name2 = j['title']
            print(link2, 2222222222222222222, name2)
            soup2 = soups(link2)
            link_img = soup2.select('ul[class="ptw ml mlp cl"] li a img')
            print(len(link_img), '相册内照片数量')
            # 爬取一个相册后随机睡眠
            time.sleep(random.random() * 5)

            for index, k in enumerate(link_img):
                link_pic = k['src']
                print('照片连接', link_pic)
                if os.path.exists('imgs/' + name2 + '/') == False:
                    os.makedirs('imgs/' + name2 + '/')
                with open('imgs/' + name2 + '/' + str(index) + '.JPG', 'wb')as f_w:
                    f_w.write(requests.get(link_pic).content)

    # 外部相册下一页是否存在
    while True:
        next_page = soup.find_all(True, text="下一页")
        print(len(next_page), type(next_page))
        if len(next_page) == 1:
            next_url = next_page[0]['href']
            print(next_url, '外部下一页连接')
            get_info(next_url)

        break


if __name__ == '__main__':
    url = 'http://www.kongjie.com/home.php?mod=space&do=album&view=all&page=1'
    get_info(url)
