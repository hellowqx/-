import requests,time,random
from fake_useragent import UserAgent
from lxml import etree
import pymysql,csv


def get_docs(url):
    ua=UserAgent()
    headers={'User-Agent':ua.random}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    html=response.text
    docs=etree.HTML(html)
    return docs



def get_info(url):
    docs=get_docs(url)
    allinfo=docs.xpath("//li[@class='clear LOGCLICKDATA']")
    print(len(allinfo))

    for i in allinfo:
        datas = list()
        houseinfo=i.xpath(".//div[@class='houseInfo']")[0].xpath('string(.)')
        addr=i.xpath(".//div[@class='flood']")[0].xpath('string(.)')
        prince=i.xpath(".//div[@class='priceInfo']/div[1]")[0].xpath('string(.)')
        oneprince=i.xpath(".//div[@class='priceInfo']/div[2]")[0].xpath('string(.)')
        datas=[houseinfo,addr,prince,oneprince]
        insertcsv(datas)
    print('本页储存完毕')

    #判断是否有下一页
    # while True:
    #     link = docs.xpath("//div[@class='page-box fr']//a[text()='下一页']/@href")
    #     print(len(link))
    #     if len(link) > 0:
    #         link=base_url + link[0]
    #
    #         get_info(link)
    #     else:
    #         break







def insertcsv(data):
    with open('data/lianjia3.csv','a+',encoding='ANSI',newline='')as f_w:
        file=csv.writer(f_w,dialect='excel')
        file.writerow(data)




if __name__ == '__main__':
    url='https://sh.lianjia.com/ershoufang/rs/'
    base_url='https://sh.lianjia.com'
    base_url2='https://sh.lianjia.com/ershoufang/pg1'
    base_url3='https://sh.lianjia.com/ershoufang/pg'
    get_info(base_url2)
    for i in range(2,101):
        next=base_url3+str(i)
        print(next)
        print('开始存储第%s页'%i)
        time.sleep(random.random()*3)
        get_info(next)
