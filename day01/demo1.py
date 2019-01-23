from urllib import request
import re
import chardet
from fake_useragent import UserAgent

ua=UserAgent()
headers={'User-Agent':ua.random}
response=request.Request('https://www.sina.com.cn/',headers=headers)
response=request.urlopen(response)
html=response.read()
encoding=chardet.detect(html)['encoding']
print(encoding)
html=html.decode(encoding,'ignore')
# print(html)

#
# from urllib import parse
# ua=UserAgent()
# headers={'User-agent':ua.random}
# url='https://www.baidu.com/s?'
# wd={'wd':'王庆祥'}
# url1=parse.urlencode(wd)
# print(type(url1))
# url2=url+url1
# print(url2)
# response=request.Request(url2,headers=headers)
#
# my_hander=request.ProxyHandler({'http':'180.118.86.177:9000'})
#
# #创建 Opener 对象
# my_opener = request.build_opener(my_hander)
# resp=my_opener.open(response)
#
# html = resp.read()
# encoding=chardet.detect(html)['encoding']
# print(encoding)
# html=html.decode(encoding)
# print(html)

#
# from urllib import parse
# word = {'name':'zzy'}
# url1=parse.urlencode(word)
# print(url1)
# url2=parse.unquote(url1)
# print(url2)