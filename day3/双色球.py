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

    docs=get_docs(url)
    allinfo=docs.xpath("//table[@class='fzTab nbt']//tr[contains(@onmouseover,'this')]")
    for i in allinfo:
        data = dict()
        qihao=i.xpath('./td[1]/text()')[0]
        kaijiang=i.xpath('./td[2]/text()')[0]
        red=i.xpath('./td[@class="redColor sz12"]/text()')[0:-2]
        reds=''.join(red)
        blue=i.xpath('./td[@class="blueColor sz12"]/text()')[0]
        num=i.xpath('./td[10]/text()')[0]
        data['qihao']=qihao
        data['kaijiang']=kaijiang
        data['red']=reds
        data['blue']=blue
        data['num']=num
        insertdb(data)


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
    sql="insert into ssqs (qihao,kaijiang,red,blue,num) values(%s,%s,%s,%s,%s) "
    cursor.execute(sql,(data['qihao'],data['kaijiang'],data['red'],data['blue'],data['num']))
    connet.commit()
    print('写入成功')
    cursor.close()
    connet.close()


if __name__ == '__main__':
    url='http://zst.aicai.com/ssq/openInfo/'
    get_info(url)


#十分钟4000条左右 一小时24000条