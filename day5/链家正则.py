import re,requests
import time,random
import csv
from fake_useragent import UserAgent

ua=UserAgent()

def htmls(url):
    headers={'User-Agent':ua.random}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    html=response.text
    return html


def get_info(url):
    html=htmls(url)
    reg=re.compile(r'<div class="info clear">(.*?<div class="unitPrice".*?)</span>.*?</div>.*?</div>.*?</div>',re.S)
    item = reg.findall(html)
    # item=re.findall(reg,html)


    price_reg = re.compile(r'<div class="totalPrice">.*?<span>(.*?)</span>.*?</div>', re.S)
    title_reg= re.compile(r'<div class="title">.*?<a.*?>(.*?)</a>.*?</div>', re.S)
    # oneprice_reg = re.compile(r'<div class="unitPrice".*?>(.*?)</div>', re.S)
    oneprice_reg = re.compile(r'<div class="priceInfo".*?<div class="unitPrice".*?<span>(.*?)</span>.*?</div>.*?</div>.*?</div>',re.S|re.M)

    print(len(item))
    for i in item:
        title=title_reg.search(i).group(1)
        price=price_reg.search(i).group(1)

        oneprice=oneprice_reg.search(i)
        # name=name1+'|'+name2
        # num=num_reg.search(i).group(1)
        print(title,price,oneprice)
        # with open('news.csv','a+',newline='',encoding='utf-8')as f_a:
        #     writer=csv.writer(f_a,dialect='excel')
        #     writer.writerow([title,name,num])
    print('本页存储完毕')
    #下一页
    next_reg=re.compile(r'<a href="(.*?)".*?class="next">')
    next_page=next_reg.search(html).group(1)
    if len(next_page) > 1:
        print(next_page,'下一页')

        get_info(next_page)
    else:
        print('存储完毕')







if __name__ == '__main__':
    get_info('https://sh.lianjia.com/ershoufang/')