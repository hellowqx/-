import requests,random
from lxml import etree


def logins():
    #登录后页面
    url2 = 'https://weibo.com/u/5458140274/home?wvr=5&lf=reg'
    url='https://login.sina.com.cn/signup/signin.php?entry=sso'
    data={
    'username':'17637938180','password':'2288'
    }
    headers={

    }
    head={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
# 'Cookie':'U_TRS1=00000099.ddc213c7.5c1aec70.3ba37d72; UOR=www.baidu.com,blog.sina.com.cn,; SINAGLOBAL=123.160.227.138_1545268337.85291; SGUID=1546847867834_38375165; lxlrttp=1546394618; Apache=172.16.138.142_1547027124.380911; ULV=1547027144859:7:6:6:172.16.138.142_1547027124.380911:1547027124099; U_TRS2=000000d3.e5c6560c.5c35c640.3bff2d6f; ULOGIN_IMG=gz-12a9318234b4ebc6d7f577fceb1ba3e9d3d8; SCF=Aiq9tOyFxIDc-RcUG48o22qj0HUFh-gshqUnSXMIPNIOA4VrPX31rlJlaWGio2Qv7IalGN--S--s_PgOq42CdFo.; SUB=_2A25xMazQDeRhGeNK7loQ9C7OzDiIHXVSRpkYrDV_PUNbm9BeLWfSkW9NSOOswnl-UxpQm59qnSkVgCLNziVv2lNM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFeAPKj12WUvM.YbH4gH5uJ5NHD95QfSh-ReKB7eoMXWs4DqcjDi--4i-8FiK.Ri--ci-2pi-2fi--fiKnNiKn4i--Xi-iFiKyFKsLVINet; ALF=1578569728; sso_info=v02m6alo5qztKWRk6SlkJSIpY6ToKWRk5ilkJOEpZCTlKWRk5SljoOcpY6DpKWRk5ClkKSIpY6EiYyalrmrnLKZtZqWkL2Nk5C1joOEtIyDiLeNgMDA',
'Host':'my.sina.com.cn',
'Upgrade-Insecure-Requests':' 1',
}
    sessions=requests.session()
    response=sessions.post(url,headers=head,data=data)
    print(response.cookies)
    # response1=sessions.get(url2,headers=head,cookies=response.cookies)
    # html=response1.text
    # print(html)

logins()
#-------------------------------------------------------------------
# def logins():
#     url='https://weibo.com/u/5458140274/home?wvr=5'
#     head={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
#         'Cookie':'Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e; login_sid_t=2ffb83d837ed33bccd9992f7e0c32471; cross_origin_proto=SSL; YF-V5-G0=f0aa2e6d566ccd1c288fae19df01df56; wb_view_log=1366*7681; _s_tentry=passport.weibo.com; Apache=8637094703946.824.1547028060054; SINAGLOBAL=8637094703946.824.1547028060054; ULV=1547028060063:1:1:1:8637094703946.824.1547028060054:; SUB=_2A25xMblvDeRhGeNK7loQ9C7OzDiIHXVSRq2nrDV8PUNbmtBeLUP1kW9NSOOswlOFuXgpNXNLi0vCJxb7_S_s_1DE; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFeAPKj12WUvM.YbH4gH5uJ5JpX5KzhUgL.Fo-XSKnpSh5ES0B2dJLoIE.LxK.LB-zL1KnLxKqLBK2LBK-LxK-L1hML1h.LxKBLB.zL12ieIg4uM7tt; SUHB=0KAxV5dPUKR5Bq; ALF=1578564799; SSOLoginState=1547028799; wvr=6; wb_view_log_5458140274=1366*7681; YF-Page-G0=e1a5a1aae05361d646241e28c550f987',
#
#     }
#     response=requests.get(url,headers=head)
#     html=response.text
#     print(html)
#
#
#
# logins()