from fake_useragent import UserAgent
import requests,chardet,csv
from lxml import etree,html


ua=UserAgent()
def get_html(url):
    headers={'User-Agent':ua.random}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'

    htmls=response.text
#返回换成符合 HTML 规则的结构化数据对象
    docs=etree.HTML(htmls)
    # docs=etree.HTML(htmls)
    return docs
def save_img():
    pass

if __name__ == '__main__':
    base_url='https://www.qiushibaike.com'
    docs=get_html('https://www.qiushibaike.com/8hr/page/1/')
    allinfo=docs.xpath("//div[@class='recommend-article']/ul/li")
    for i in allinfo:
        a=i.xpath(".//div[@class='recmd-right']/a/text()")
        if len(a) == 0:
            continue
        title=i.xpath(".//div[@class='recmd-right']/a/text()")[0]
        link=i.xpath(".//div[@class='recmd-right']/a[@class='recmd-content']/@href")[0]
        url=base_url+link
        save_img()
        #判断评论为空
        pinglun=i.xpath(".//div[@class='recmd-num']/span[4]/text()")
        pinglun = pinglun[0] if len(pinglun) > 0 else None
        zan=i.xpath(".//div[@class='recmd-num']/span[1]/text()")[0]
        #判断赞为空
        zan = zan[0] if len(zan) > 0 else None
        author=i.xpath(".//a[@class='recmd-user']/span/text()")[0]
        with open('data/糗事.csv','a+',encoding='utf-8')as f_w:
            writer=csv.writer(f_w)
            writer.writerow(['作者:',author,'标题:',title,'点赞：',zan,'评论',pinglun,'标题连接:',url])



