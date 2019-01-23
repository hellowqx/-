import re,requests
import time,random
import csv
from fake_useragent import UserAgent

ua=UserAgent()

def htmls(url):
    headers={'User-Agent':ua.random}
    response=requests.get(url,headers=headers)
    response.encoding='gbk'
    html=response.text
    return html


def get_info(url):
    html=htmls(url)
    reg=re.compile(r'<div class="news_item">(.*?<div class="share".*?)</div>.*?</div>.*?</div>.*?</div>',re.S)
    item = reg.findall(html)
    # item=re.findall(reg,html)

    title_reg = re.compile(r'<h3>.*?<a href="(.*?)">', re.S)
    name_reg = re.compile(r'<div class="keywords">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>', re.S)
    num_reg = re.compile(r'<span class="icon">(.*?)</span>', re.S)


    for i in item:
        title=title_reg.search(i).group(1)
        name1=name_reg.search(i).group(1)
        name2=name_reg.search(i).group(2)
        name=name1+'|'+name2
        num=num_reg.search(i).group(1)

        with open('news.csv','a+',newline='',encoding='utf-8')as f_a:
            writer=csv.writer(f_a,dialect='excel')
            writer.writerow([title,name,num])
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
    get_info('http://sports.163.com/zc/')