import re,requests
from fake_useragent import UserAgent

ua=UserAgent()

def htmls(url):
    headers={'User-Agent':ua.random}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    html=response.text
    return html


def get_info(url):
    html=htmls(url)
    reg=re.compile(r'<div class="text-column-item box box-790">(.*?<div\s+class="view".*?)</div>.*?</div>.*?</div>',re.S)
    # item=re.findall(reg,html)
    item=reg.findall(html)
    print(len(item))




if __name__ == '__main__':
    get_info('https://www.neihan8.com/article/index.html')