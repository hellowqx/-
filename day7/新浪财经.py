import time, requests, json
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import re, math, pymysql, random

proxies = {
    "http": "http://111.177.183.206:9999"
}

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-type': 'application/x-www-form-urlencoded',
    'Cookie': 'U_TRS1=00000099.ddc213c7.5c1aec70.3ba37d72; UOR=www.baidu.com,blog.sina.com.cn,; SINAGLOBAL=123.160.227.138_1545268337.85291; SGUID=1546847867834_38375165; lxlrttp=1546394618; SCF=Aiq9tOyFxIDc-RcUG48o22qj0HUFh-gshqUnSXMIPNIOA4VrPX31rlJlaWGio2Qv7IalGN--S--s_PgOq42CdFo.; SUB=_2AkMrYdTZdcPxrAZVnfAUyGvga4lH-jyYtL0vAn7tJhMyAhgv7l1WqSVutBF-XBGtu8NNsDF39VZ8zCQGkI3k9k5u; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WFeAPKj12WUvM.YbH4gH5uJ5JpVF02NSoeN1KeReKn7; U_TRS2=00000060.dc6f9de4.5c3e9856.d3a819f7; Apache=123.160.224.96_1547606104.515865; ULV=1547631699921:11:10:4:123.160.224.96_1547606104.515865:1547606102327',
    'Host': 'vip.stock.finance.sina.com.cn',
    'Referer': 'http://vip.stock.finance.sina.com.cn/mkt/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}


def get_data(n, node):
    # 自定义请求数据
    params = {
        'page': n,
        'num': '40',
        'sort': 'symbol',
        'asc': '1',
        'node': node,
        'symbol': '',
        '_s_r_a': 'init',
    }
    insert_data = dict()
    base_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'

    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code == 200:
        reg = re.compile(r'(.*)')
        data = reg.sub(r'{data:\1}', response.text)
        reg2 = re.compile(r'([a-z]+):')
        datas = reg2.sub(r'"\1":', data)
        # print(datas)
        data = json.loads(datas)['data']
        print(len(data), '每页数据量')

        for i in data:
            insert_data['name'] = i['name']
            insert_data['new_price'] = i['trade']
            insert_data['daima'] = i['symbol']
            insert_data['zhangdie'] = i['pricechange']
            insert_data['zhangdiefu'] = i['changepercent']
            insert_data['buy'] = i['buy']
            insert_data['sell'] = i['sell']
            insert_data['zuoshou'] = i['settlement']
            insert_data['jinkai'] = i['open']
            insert_data['zuigao'] = i['high']
            insert_data['zuidi'] = i['low']
            insert_data['chengjiaoliang'] = i['volume']
            insert_data['chengjiaoe'] = i['amount']
            print(insert_data)
            # inser(insert_data)

        # 内部页数
        res = requests.get(
            url='http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node='+node)
        res = res.text
        page = re.search(r'(\d+)', res).group(1)
        # 向上取整
        page = math.ceil(int(page) / 40)
        print(page,'总页数')
        print(n, '上面正在爬取页码数')
        print('==' * 60)
        return n,page,node

def loop(n,page,node):

    for j in range(page - 1):
        n += 1
        print('第%s循环' % n)
        if n < page + 1:
            time.sleep(random.random() * 5)
            get_data(n, node)
        else:
            break
    return

def inser(insert_data):
    con = pymysql.Connect(
        host='localhost',
        port=3306,
        db='sina',
        user='root',
        password='root',
        charset='utf8')
    cursor = con.cursor()
    sql = 'insert into caijing values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, (0, insert_data['daima'], insert_data['name'], insert_data['new_price'],
                         insert_data['zhangdie'], insert_data['zhangdiefu'], insert_data['buy'], insert_data['sell'],
                         insert_data['zuoshou'], insert_data['jinkai'], insert_data['zuigao'], insert_data['zuidi'],
                         insert_data['chengjiaoliang'], insert_data['chengjiaoe']))
    con.commit()
    print('写入成功')
    # cursor.close()
    # con.close()


if __name__ == '__main__':
    chrome = webdriver.Chrome()
    chrome.get('http://vip.stock.finance.sina.com.cn/mkt/')

    fenlei = chrome.find_element_by_link_text('分类')
    time.sleep(2)
    action = ActionChains(chrome)
    # 鼠标移动到分类
    action.move_to_element(fenlei).perform()
    time.sleep(2)
    hushiagu = chrome.find_elements_by_xpath("//li[@class='active']/div[@class='lv_1']//dd")
    # 外部导航栏模块

    for index, i in enumerate(hushiagu):
        i.click()
        time.sleep(3)
        print('**' * 60)
        print('正在爬取%s模块' % (index + 1))
        url = chrome.current_url
        print(url)
        # 获取模块名称，传给函数
        node = re.search(r'/#([a-z_]+)', url).group(1)
        print(node)
        n,page,node=get_data(1, node)
        #内部页码循环
        loop(n,page,node)
        # 鼠标移动到分类
        action.move_to_element(fenlei).perform()
        time.sleep(2)
        hushiagu = chrome.find_elements_by_xpath("//li[@class='active']/div[@class='lv_1']//dd")
