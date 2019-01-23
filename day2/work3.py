#贴吧图片爬虫
#提取帖子中的图片，并保存images文件夹下 贴吧的名称_xx.png
from urllib import request, parse
from fake_useragent import UserAgent
import csv,time,os,requests,random
from lxml import etree
from PIL import Image
from io import BytesIO


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
base_url='https://tieba.baidu.com'

def get_docs(url):
    res = request.Request(url)
    resp = request.urlopen(res)
    htmls = resp.read().decode('utf-8', 'ignore')
    docs = etree.HTML(htmls)
    return docs

for i in range(int(end_num)):
    if i >= int(start_num)-1:

        url='http://tieba.baidu.com/f?'+data+'&ie=utf-8&pn='+str((int(i))*50)
        docs=get_docs(url)
        infos=docs.xpath("//div[contains(@class,'col2_right j_threadlist_li_right')]")
        print(len(infos))
        #每页包含需要信息的所有div
        for i in infos:
            link=base_url+i.xpath('.//a/@href')[0]
            docs=get_docs(link)
            #标题的所有链接
            imgs=docs.xpath('//div[@class="d_post_content j_d_post_content "]')
            for j in imgs:
                #帖子详情的图片链接
                img=j.xpath('.//img[@class="BDE_Image"]/@src')
                if len(img) ==1:
                    time.sleep(1)
                    if not os.path.exists('imgs/'+name):
                        os.makedirs('imgs/'+name)
                    time1=time.time()
                    htmlss=requests.get(img[0])
                    image = Image.open(BytesIO(htmlss.content))
                    image.save( 'imgs/'+name+'/'+str(time1)+'.png')
                    print('一张图片保存完毕')
                    #随机睡眠
                    time.sleep(random.random() * 3)

            print('这个帖子保存图片完毕')

        print(('第%s页保存完毕')%(i))

