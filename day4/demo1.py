#
#
#
#
# import requests
#
#
# def download_file(url, path):
#     loaded = 0
#     with requests.get(url, stream=True) as r:
#         chunk_size = 10240
#         content_size = int(r.headers['content-length'])
#         print(content_size,1111111111)
#         print('下载开始。。。')
#         with open(path, "wb") as f:
#             for chunk in r.iter_content(chunk_size=chunk_size):
#                 loaded +=(chunk_size / content_size)
#                 f.write(chunk)
#                 print('已下载{:.2f}%'.format(loaded*100))
#     print('下载结束。。。')
#
#
# if __name__ == '__main__':
#     url ='http://qiubai-video-web.qiushibaike.com/XD3XOK7IM9QVTDBE_hd.mp4'
#     path = './video/v.mp4'
#     download_file(url, path)
#
# import re
# a='http://www.chinamedevice.cn/product/1219/1/1.html'
# reg=r'(http://.*?/)\d+.html'
# print(re.findall(reg,a))


import requests
from bs4 import BeautifulSoup


url='http://www.chinamedevice.cn'

response=requests.get(url).text
soup=BeautifulSoup(response,'lxml')

a=soup.select('div[class="type"]  h3:nth-child(even)')
print(len(a))