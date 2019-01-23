from lxml import etree
import requests, csv
from fake_useragent import UserAgent


# 得到可以被xpath解析的页面
def get_docs(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    response.encoding = 'gb2312'
    htmls = response.text
    docs = etree.HTML(htmls)
    return docs

#得到信息
def get_info(url):
    base_url = 'http://www.jokeji.cn'
    docs = get_docs(url)
    allinfo = docs.xpath('//table[contains(@width,"646")]')
    for i in allinfo:
        title = i.xpath(".//tr/td[2]/a[@class='main_14']/text()")
        link = base_url + i.xpath(".//tr/td[2]/a[@class='main_14']/@href")[0]
        print(link)
        count = i.xpath(".//tr/td[3]/text()")
        time = i.xpath(".//tr/td[4]/span/text()")
        #将新的连接，得到笑话内容页面
        new_docs = get_docs(link)
        content1 = new_docs.xpath('//span[@id="text110"]/p/font/text()')
        content = new_docs.xpath('//span[@id="text110"]/p/text()')
        content2 = new_docs.xpath('//span[@id="text110"]/font/text()')
        content4 = new_docs.xpath('//span[@id="text110"]/p/font/text()')
        content3 = new_docs.xpath('//span[@id="text110"]/font/p/font/text()')
        li = list()
        #筛选数据的语法列表
        li.append(content)
        li.append(content1)
        li.append(content2)
        li.append(content3)
        li.append(content4)
        for x in li:
            if len(x) == 0:
                continue
            else:
                content = x
        for j in content:
            with open('data/joke.csv', 'a+', encoding='utf-8') as f:
                writer = csv.writer(f, dialect='excel')
                writer.writerow([j])


if __name__ == '__main__':
    url = 'http://www.jokeji.cn/hot.htm'
    get_info(url)
