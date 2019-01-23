# import requests
# from selenium import webdriver
#
# chrome=webdriver.Chrome()
# chrome.get('https://passport.bilibili.com/login')
# print(type(chrome.page_source))
#
# rep=requests.get('https://passport.bilibili.com/login')
# print(type(rep.text))


import time
from datetime import datetime
from urllib import parse

# # a=time.localtime()
# b=time.strftime("%a %b %d %Y %H:%M:%S GMT 0800 (中国标准时间)",time.localtime())
# print(type(b))
# #Thu Jan 17 2019 15:56:22 GMT 0800 (中国标准时间):
# # stampThu%20Jan%2017%202019%2015:56:22%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)
# GMT_FORMAT = '%a %d %b %Y %H:%M:%S GMT'
# # 生成Thu Dec 13 2018 08:45:30 GMT 0800格式的datetime对象
# date_time = datetime.utcnow().strftime(GMT_FORMAT)
# print(date_time)
b=datetime.now().strftime('%a %b %d %Y %X') + ' GMT 0800 (中国标准时间)'
a=datetime.now().strftime('%a %b %d %Y %H:%M:%S')+' GMT 0800 (中国标准时间)'

print(b)
print(a)

word = parse.urlencode({"stamp": datetime.now().strftime('%a %b %d %Y %X') + 'GMT 0800 (中国标准时间)'})
print(word)


