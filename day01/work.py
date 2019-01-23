# 批量爬取贴吧数据
# 输入贴吧名称， 起始页码， 结束页码， 爬取贴吧数据， 以‘第x页.html’ 命名， 保存为html 文件

from urllib import request, parse
from fake_useragent import UserAgent
import chardet, json
import zlib

ua = UserAgent()
headers={
    'User-agent':ua.random,

}
name=input('请输入贴吧名称：')
data={
    'kw':name
}
data=parse.urlencode(data)
start_num= input('请输入起始页：')
end_num= input('请输入结束页：')
for i in range(int(end_num)):
    if i >= int(start_num)-1:

        url='http://tieba.baidu.com/f?'+data+'&ie=utf-8&pn='+str((int(i))*50)
        print(url)
        res = request.Request(url, headers=headers)
        resp = request.urlopen(res)
        html = resp.read().decode('utf-8','ignore')
        # encoding = chardet.detect(html)['encoding']
        # print(encoding)
        # html = html.decode(encoding, 'ignore')
        with open('pagess'+str(i+1)+'.html','w',encoding='utf-8')as f_r:
            f_r.write(html)


# _____________________________________________
# 通过代理ip爬取腾讯首页，打印爬取内容
# ua = UserAgent()
# headers = {
#     'User-agent': ua.random,
# }
#
# url = 'https://www.qq.com/'
# req = request.Request(url, headers=headers)
# my_header = request.ProxyHandler({'http': '180.118.86.177:9000'})
# # 创建open对象
# my_open = request.build_opener(my_header)
# response = my_open.open(req)
# html = response.read()
# encoding = response.info().get('Content-Encoding')
# print(encoding,11111)
# if encoding == 'gzip':
#     html = zlib.decompress(html, 16 + zlib.MAX_WBITS)
# elif encoding == 'deflate':
#     try:
#         html = zlib.decompress(html, -zlib.MAX_WBITS)
#     except zlib.error:
#         html = zlib.decompress(html)
# charset = chardet.detect(html)["encoding"]
# print(charset,2222222222)
# html=html.decode(charset, 'ignore')
# with open('腾讯2.html','w',encoding='gb2312')as f_w:
#     f_w.write(html)

#7.----------------------------------------------------------------
# ua=UserAgent()
# headers={'User-agent':ua.random}
#
# for i in range(1,6):
#
#     url='http://www.jokeji.cn/hot.asp?me_page='+str(i)
#     print(url)
#     req=request.Request(url,headers=headers)
#     response=request.urlopen(req)
#     html=response.read()
#     encoding=chardet.detect(html).get('encoding')
#     print(encoding)
#     html=html.decode(encoding,'ignore')
#     with open('笑话'+str(i)+'.html','w',encoding='utf-8')as f_w:
#         f_w.write(html)



#8----------------------------------------------------
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
for i in range(1,6):
    url='http://yunqi.qq.com/bk/so2/n10p'+str(i)
    print(url)
    req=request.Request(url,headers=headers)
    # my_header = request.ProxyHandler({'http':'123.162.168.192:37644'})
    # # 创建open对象
    # my_open = request.build_opener(my_header)
    # response = my_open.open(req)
    response=request.urlopen(req)
    html = response.read()

    encoding=chardet.detect(html)['encoding']
    html=html.decode(encoding,'ignore')
    # with open('书院' + str(i) + '.txt', 'w+', encoding='utf-8')as f_w:
    #      f_w.write(html)

    with open('书院' + '.txt', 'a+', encoding='utf-8')as f_w:
         f_w.write(html)
