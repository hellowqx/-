import requests,time,random
from fake_useragent import UserAgent
from lxml import etree
import pymysql


def get_docs(url):
    ua=UserAgent()
    headers={'User-Agent':ua.random}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    html=response.text
    docs=etree.HTML(html)
    return docs



def get_info(url):
    data = dict()
    docs=get_docs(url)
    allinfo=docs.xpath("//div[@class='mdui-row mdui-typo']")
    print(len(allinfo))
    for i in allinfo:
        title=i.xpath(".//h3[@class='mdui-m-t-0 mdui-m-l-1']/a")[0].xpath("string(.)").strip()

        author=i.xpath(".//div[@class='mdui-col-xs-12 mdui-col-md-9 mdui-typo'][1]/div[@class='mdui-col-xs-12']/span[1]/text()")[0]
        time=i.xpath(".//div[@class='mdui-col-xs-12 mdui-col-md-9 mdui-typo'][1]/div[@class='mdui-col-xs-12']/span[4]/text()")[0]
        content=i.xpath(".//div[@class='mdui-col-xs-12 mdui-typo']/p")[0].xpath("string(.)").strip()


        data['time']=time
        data['content']=content
        data['author']=author
        data['title']=title

        insertdb(data)

        print(title,author,time,content)



#
#
def insertdb(data):
    connet=pymysql.Connect(
        host='localhost',
        port=3306,
        db='ssq',
        user='root',
        password='root',
        charset='utf8'
    )
    cursor=connet.cursor()
    sql="insert into zhiwang (title,author,time,content) values(%s,%s,%s,%s) "
    cursor.execute(sql,(data['title'],data['author'],data['time'],data['content']))
    connet.commit()
    print('写入成功')
    cursor.close()
    connet.close()


if __name__ == '__main__':
    url='https://search.ehn3.com/search?keyword=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&db=SCDB'
    get_info(url)