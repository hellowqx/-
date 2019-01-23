from bs4 import BeautifulSoup
import lxml, requests
from fake_useragent import UserAgent
import csv, re, time, random


# 得到解析页面
def soups(url):
    headers = {
        'User-Agent': UserAgent().random
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'gb2312'
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    return soup


# 筛选数据
def get_info(url):
    soup = soups(url)
    infor = soup.select('div[class="list"] > ul >li')
    print('本页数据量为', len(infor))
    for i in infor:
        name = i.select('h3 > span > a')[0].string.strip()
        link_detail= i.select('h3 > span > a')[0].attrs['href']
        try:
            intro = i.select('p')[2].string.strip()
            # intro = intro.replace('\n', '')
        except:
            intro = 'null'
        company = i.select('p')[-1].select('a')[0].string.strip()
        # print(name,company)
        # with open('csv/yiliaoqixie.csv','a+',encoding='utf-8',newline='') as f_w:
        #     writers=csv.writer(f_w,dialect='excel')
        #     writers.writerow([name,intro,company])
        get_product(link_detail)
    print('=' * 60)
    # 判断下一页

    # next_url=soup.find_all('a', text='下一页')
    next_url = soup.find_all(True, text='下一页')
    if len(next_url) == 1:
        next_url = next_url[0].attrs['href']
        # next_url = next_url[0]['href']
        # 正则匹配新的下一页
        # reg = r'(http://.*/)\d+.html'
        # url2 = re.findall(reg, url)[0]
        # next_urls = url2 + next_url

        # 新的下一页
        reg = re.compile('(\d+\.html)')
        url2 = reg.sub(next_url, url)
        next_urls=url2

        print('开始爬取第%s页' % next_url)
        print(next_urls, 222222222)
        time.sleep(random.random() * 5)
        get_info(next_urls)

def get_product(url):
    '''
    根据指定产品的url，提取产品的信息
    :param url:
    :return:
    '''
    soup=soups(url)
    #产品名称
    pname = soup.select_one('#main > dl > dt > h1').get_text()
    print("产品名称：",pname)
    purl = url
    print('url:',url)

    #封面url
    cover_url = soup.select_one('.img > a > img').attrs['src']
    print('封面：',cover_url)

    item = soup.select('#main > dl > dd > div > ul > li')
    cate_name = item[1].contents[-1].strip()
    print('产品分类：',cate_name)

    en_name = item[2].select('h3')
    if len(en_name) > 0:
        if en_name[0] != None:
            en_name = en_name[0].text
    else:
        en_name = '无'
    print('英文名称：',en_name)

    number = item[3].contents[1].text.strip()
    print("批准文号：",number)

    spec = item[4]
    if len(spec) == 2:
        spec = spec.contents[1].strip()
    else:
        spec = '无'
    print('主要规格:',spec)

    descr = soup.select('.text03')
    if len(descr) > 0:
        descr = descr[0].text.strip()
    else:
        descr = '无'
    print("产品说明：",descr)

    producter = soup.select_one('li.bgwhite.pt > h3 > a').text.strip()
    print('生产企业：',producter)

    proucter_url = soup.select_one('li.bgwhite.pt > h3 > a').attrs['href']
    print("企业页面：",proucter_url)

    contacter = soup.select(".text04 > ul > li")[2].text.split('：')[-1]
    print('联系人：',contacter)

    phone = soup.select(".text04 > ul > li")[3]
    phone = phone.contents[0].strip().split('：')
    if len(phone) == 2:
        phone = phone[1]
    else:
        phone = '空'
    print('联系电话：',phone)

    mobile = soup.select(".text04 > ul > li")[5]
    mobile = mobile.contents[0].strip().split('：')
    if len(mobile) == 2:
        mobile = mobile[1]
    else:
        mobile = '空'
    print('移动电话：', mobile)


    address = soup.select(".text04 > ul > li")[9]
    address = address.contents[0].strip().split('：')
    if len(address) == 2:
        address = address[1]
    else:
        address = '空'
    print('地址：', address)
    print('='*60)


def core(url):
    soup = soups(url)
    infos = soup.select('a[class="f12"]')
    print(len(infos))
    for i in infos[:-1]:
        link1 = url + i['href']
        print(link1)
        get_info(link1)
        print('一个模块存储完毕')


if __name__ == '__main__':
    url = 'http://www.chinamedevice.cn'
    core(url)
