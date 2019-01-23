# -*- coding: utf-8 -*-
import scrapy,os,time,random
from scrapy import cmdline
import requests,re
num1 = 0

class LiVideoSpider(scrapy.Spider):
    name = 'li_video'
    allowed_domains = ['pearvideo.com']
    start_urls = ['https://www.pearvideo.com/popular_loading.jsp?reqType=1&categoryId=&start=0&sort=0&mrd=0.30235557000626234']

    def parse(self, response):
        global num1
        base='https://www.pearvideo.com/'
        links=response.xpath("//li[@class='popularem clearfix']/a[@class='actplay']/@href").extract()
        for i in links:
            v_link=base+i
            print(v_link,11111111111111111)
            yield response.follow(v_link,self.video_download)

        #下一页

        num1 += 10
        num3=random.random()

        next_url='https://www.pearvideo.com/popular_loading.jsp?reqType=1&categoryId=&start='+str(num1)+'&sort='+str(num1)+'&mrd='+str(num3)
        if num1<=100:
            print('next_url:',next_url)
            time.sleep(random.random()*5)
            yield response.follow(next_url,self.parse)




    def video_download(self,response):
        # print(response.text)
        # reg=re.compile(r'srcurl="(.*?)"')
        # video_url=reg.search(response.text)
        video_url=re.findall(r'srcUrl="(.*?)"',response.text)[0]
        video_name=response.xpath("//div[@class='box-left clear-mar']/h1[@class='video-tt']/text()").extract()[0]
        print(video_url,video_name)
        if not os.path.exists('../video/'):
            os.makedirs('../video/')
        # with open('../video/'+video_name+'.mp4','wb')as f_w:
        #     # loaded=0
        #     # chunk_size=1024
        #     # print(response.headers['content-length'])
        #     # content_size=int(response.headers['content-length'])
        #     # print(content_size,2222222222222222)
        #     #
        #     # for j in response.iter_content(chunk_size=chunk_size):
        #     #     loaded+=(chunk_size/content_size)
        #     #     print('正在下载%s'%video_name)
        #     #     print('已下载{:.2f}%'.format(loaded * 100))
        #     #     f_w.write(requests.get(video_url).content)
        #     print('正在下载%s' % video_name)
        #     time.sleep(0.5)
        #     f_w.write(requests.get(video_url).content)

if __name__ == '__main__':
    cmd='scrapy crawl li_video'
    cmdline.execute(cmd.split())