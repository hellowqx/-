import urllib ,chardet,json
from fake_useragent import UserAgent
from urllib import parse,request


ua=UserAgent()
headers={
    'User-Agent':ua.random
}
url='https://fanyi.baidu.com/transapi'
data={
'from':'en' ,
'to': 'zh',
'query':'tom',
'transtype': 'translang',
'simple_means_flag':'3',
'sign': '228056.498153',
'token': '29e6ef7c2fec8903f9dd9640b426b76f',
}

data=parse.urlencode(data).encode('utf-8')
print(data)
res=request.Request(url,headers=headers)
response=request.urlopen(res,data=data)

html=response.read()
print(type(html))
encoding=chardet.detect(bytes(html))['encoding']
print(encoding)
html=html.decode(encoding,'ingore')
print(html)
results=json.loads(html)
print(results)
result = results['data'][0]['dst']
# 打印翻译结果
print('翻译的结果：',result)



url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data={
'i': '你好',
'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': '15468706607630',
'sign': 'f2ff7ca39e4138141a42e2910546a8f5',
'ts': '1546870660763',
'bv': '6dfac01e4ee085fbf06475a5a3c2a9c2',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTIME',
'typoResult': 'false',
}

data=parse.urlencode(data).encode('utf-8')
print(data)
res=request.Request(url,headers=headers)
response=request.urlopen(res,data=data)

html=response.read().decode()
print(html,1111111111)
results=json.loads(html)
print(results)
result = results['translateResult'][0][0]['tgt']
# 打印翻译结果
print('翻译的结果：',result)
