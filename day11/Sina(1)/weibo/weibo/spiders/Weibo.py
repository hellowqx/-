# -*- coding: utf-8 -*-
import scrapy, time
from scrapy import Request, Spider
from ..items import User_info, UserRelationItem
import json



class WeiboSpider(scrapy.Spider):
    name = 'Weibo'
    allowed_domains = ['m.weibo.cn']
    # 用户主页URL
    user_index = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}'
    # 用户资料URL
    user_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}'
    user_info = 'https://m.weibo.cn/api/container/getIndex?containerid=230283{uid}_-_INFO&title=基本资料&luicode=10000011&lfid=230283{uid}'
    start_users = ['5309188650', '1669879400' , '1826792401', '5869525717', '1672384324', '1371731565', '1195242865']
    # 关注好友列表API
    follow_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&page={page}'
    # 粉丝列表API
    fans_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&page={page}'

    def start_requests(self):
        for uid in self.start_users:
            yield Request(self.user_url.format(uid=uid), callback=self.parse_info)

    def parse_info(self,response):
        """
        解析用户资料
        :param response:
        :return:
        """
        self.logger.debug(response)
        result = json.loads(response.text)
        time.sleep(3)
        if result.get('data').get('userInfo'):
            user_info = result.get('data').get('userInfo')
            user_item = User_info()
            field_map = {
                'id': 'id', 'name': 'screen_name', 'avatar': 'profile_image_url', 'description': 'description', 'certification':'verified_reason', 'fans_count': 'followers_count',
                'follows_count': 'follow_count', 'weibos_count': 'statuses_count', 'person_url':'profile_url', 'level':'urank'
            }
            for field, attr in field_map.items():
                user_item[field] = user_info.get(attr)
            id = user_item.get('id')
            yield Request(self.user_info.format(uid=id), callback=self.parse_user, meta={'uid':id, 'user_item':user_item})
            # 关注
            uid = user_info.get('id')
            yield Request(self.follow_url.format(uid=uid, page=1), callback=self.parse_follows,
                          meta={'page': 1, 'uid': uid})
            # 粉丝
            yield Request(self.fans_url.format(uid=uid, page=1), callback=self.parse_fans,
                          meta={'page': 1, 'uid': uid})

    def parse_user(self, response):
        """
        解析用户信息
        :param response: Response对象
        :return:
        """
        result = json.loads(response.text)
        time.sleep(4)
        try:
            if result.get('data').get('cards'):
                user_info = result.get('data').get('cards')
                info2 = user_info[1].get('card_group')
                gender = info2[1].get('item_content')
                local = info2[2].get('item_content')
                user_item = response.meta['user_item']
                user_item['local'] = local
                user_item['gender'] = gender
                yield user_item
        except Exception as e:
            print(e)


    def parse_follows(self, response):
        """
        解析用户的关注列表
        :param response:Response对象
        :return:
        """
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('card') and len(result.get('data').get('cards')) \
                and result.get('data').get('cards')[-1].get('card_group'):
            # 解析用户
            follows = result.get('data').get('cards')[-1].get('card_group')
            for follow in follows:
                if follow.get('user'):
                    uid = follow.get('user').get('id')
                    yield Request(self.user_url.format(uid=uid), callback=self.parse_info)

            # 关注列表
            uid = response.meta.get('uid')
            user_relation_item = UserRelationItem()
            follows = [{'id': follow.get('user').get('id')} for follow in
                       follows]
            user_relation_item['id'] = uid
            user_relation_item['follow'] = follows
            # user_relation_item['fans'] = []
            yield user_relation_item
            # 下一页关注的好友
            page = response.meta.get('page') + 1
            time.sleep(4)
            yield Request(self.follow_url.format(uid=uid, page=page), callback=self.parse_follows,
                          meta={'page': page, 'uid': uid})

    def parse_fans(self, response):
        """
        #  解析用户粉丝列表
        :param response: Response对象
        :return:
        """
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards') and len(result.get('data').get('cards')) and \
                result.get('data').get('cards')[-1].get(
                    'card_group'):
            # 解析用户
            fans = result.get('data').get('cards')[-1].get('card_group')
            for fan in fans:
                if fan.get('user'):
                    uid = fan.get('user').get('id')
                    yield Request(self.user_url.format(uid=uid), callback=self.parse_info)
            uid = response.meta.get('uid')
            # 粉丝列表
            user_relation_item = UserRelationItem()
            # fans = [{'id': fan.get('user').get('id')} for fan in
            #         fans]
            user_relation_item['id'] = uid
            # user_relation_item['fans'] = fans
            # user_relation_item['follows'] = []
            # yield user_relation_item
            # 下一页粉丝
            page = response.meta.get('page') + 1
            time.sleep(3)
            yield Request(self.fans_url.format(uid=uid, page=page),
                          callback=self.parse_fans, meta={'page': page, 'uid': uid})
