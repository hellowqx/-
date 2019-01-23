import time,requests,json,re
from urllib import parse
from datetime import datetime


# datas={'stamp':datetime.now().strftime('%a %b %d %Y %H:%M:%S')+' GMT 0800 (中国标准时间)'}
datas={'stamp':time.strftime('%a %b %d %Y %H:%M:%S',time.localtime())+' GMT 0800 (中国标准时间)'}
datas=parse.urlencode(datas)

url='http://pic.haibao.com/ajax/image:getHotImageList.json?'+datas
print(url)
headers={
"Cookie":"hbUnregUserId=505A9979-9DE6-4ACE-8868-FEB8BF92C75B;captcha_comment=9scUS7Mt2KOZ4JF6FffA7cXSWIsNRPNLAl3YBf7Ff0c%3D; MW8x_a166_saltkey=ydR3xfZq; MW8x_a166_lastvisit=1547534324; __captcha=ugpw%2BzZqT2kHlH8bnm2k1uDh%2F%2BpiRV6c7bFg%2Fjxi2Kk%3D; Hm_lvt_9448a813e61ee0a7a19c41713774f842=1545267496,1547002481,1547535384,1547690546; Hm_lvt_06ffaa048d29179add59c40fd5ca41f0=1545267496,1547002481,1547535384,1547690546; Hm_lvt_793a7d1dd685f0ec4bd2b50e47f13a15=1545267496,1547002481,1547535384,1547690546; Hm_lpvt_793a7d1dd685f0ec4bd2b50e47f13a15=1547690580; Hm_lpvt_06ffaa048d29179add59c40fd5ca41f0=1547690580; Hm_lpvt_9448a813e61ee0a7a19c41713774f842=1547690580",
"Referer":"http://pic.haibao.com/hotimage/",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
}

def skips(n):
    num = 0
    for i in range(int(n)):
        data = {'skip': num}
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            res = response.text
            result = json.loads(res)['result']['html']
            links = re.findall(r'originUrl="(.*?)">', result)
            names = re.findall(r'alt="(.*?)"', result)
            print()
            print(len(links),'链接个数')
            print(len(names),'名字个数')
            #更改skip的值
            num+=len(links)
            print('skip:',num)
            #存储照片
            x=0
            for i,j in zip(links,names):
                x+=1
                print(j,i)
                save(i,j,x)

def save(link,name,x):
    with open('imgs/'+name+str(x)+'.JPG','wb') as f_w:
        f_w.write(requests.get(link).content)
        print('一张图片存储完毕')

if __name__ == '__main__':
    n=input('输入点击次数')
    skips(n)