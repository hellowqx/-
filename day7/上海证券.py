import time,requests,json
from fake_useragent import UserAgent
import re
ua=UserAgent()
headers={
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie':'yfx_c_g_u_id_10000042=_ck19011610145414298572387134870; VISITED_MENU=%5B%228528%22%5D; yfx_f_l_v_t_10000042=f_t_1547604894415__r_t_1547604894415__v_t_1547604999938__r_c_0',
'Host':'query.sse.com.cn',
'Referer':'http://www.sse.com.cn/assortment/stock/list/share/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}
n=1547605000502
params={
'jsonCallBack':'jsonpCallback19182',
'isPagination':'true',
'stockType':'1',
'pageHelp.cacheSize':'1',
'pageHelp.beginPage':'2',
'pageHelp.pageSize':'25',
'pageHelp.pageNo':'2',
'pageHelp.endPage':'21',
'_':str(n),

}


def datas(url):
    response=requests.get(url,params=params,headers=headers)
    reg=re.compile(r'(\w+\()\{(.*?)\}(\))')
    data=reg.sub(r'{"data":[{\2}]}',response.text)
    datas=json.loads(data)['data']
    print(datas)





if __name__ == '__main__':
    url='http://query.sse.com.cn/security/stock/getStockListData2.do'
    datas(url)