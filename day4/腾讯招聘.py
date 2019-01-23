from bs4 import BeautifulSoup
import lxml,requests
from fake_useragent import UserAgent

def soups(url):
    headers={
        'User-Agent':UserAgent().random
    }
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    html=response.text
    soup = BeautifulSoup(html, 'lxml')
    return soup

def core(url):
    soup=soups(url)
    infos=soup.select('table[class="tablelist"] > tr')[1:-1]
    print(len(infos))
    for i in infos:
        name=i.select('td > a')[0].text
        num=i.select('td')[2].text
        addr=i.select('td')[3].text
        time=i.select('td')[4].text
        print(name,num,addr,time)




if __name__ == '__main__':
    url='https://hr.tencent.com/position.php?&start=0#a'
    core(url)





