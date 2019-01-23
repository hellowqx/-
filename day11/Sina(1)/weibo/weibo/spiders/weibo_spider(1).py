# -*- coding: utf-8 -*-
import scrapy
import json, time
# from ..items import User_info, User_id
from weibo_redis.items import User_id, User_info
from scrapy import Request, Spider
from scrapy_redis.spiders import RedisSpider


class WeiboSpiderSpider(RedisSpider):
    name = 'weibo_spider'
    redis_key = 'weibospider:start_urls'
    # allowed_domains = ['m.weibo.cn']
    # start_urls = ['http://m.weibo.cn/']
    # 用户主页URL
    user_index = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}'
    # 用户资料URL
    user_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}'
    user_info = 'https://m.weibo.cn/api/container/getIndex?containerid=230283{uid}_-_INFO&title=基本资料&luicode=10000011&lfid=230283{uid}'
    # 关注好友列表API
    follow_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&page={page}'
    # 粉丝列表API
    fans_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&page={page}'
    # lpush weibospider:start_urls https://m.weibo.cn/api/container/getIndex?uid=1826792401&type=uid&value=1826792401&containerid=1005051826792401

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(WeiboSpiderSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        """
        解析用户资料
        :param response:
        :return:
        """
        result = json.loads(response.text)
        time.sleep(3)
        if result.get('data').get('userInfo'):
            user_info = result.get('data').get('userInfo')
            id = user_info.get('id')
            name = user_info.get('screen_name')
            avatar = user_info.get('profile_image_url')
            description = user_info.get('description')
            certification = user_info.get('verified_reason')
            fans_count = user_info.get('followers_count')
            follow_me = user_info.get('follow_me')
            follows_count = user_info.get('follows_count')
            weibos_count = user_info.get('statuses_count')
            person_url = user_info.get('profile_url')
            level = user_info.get('urank')
            following = user_info.get('following')
            user_item = User_info(id=id, name=name, avatar=avatar, description=description, certification=certification,
                                  fans_count=fans_count, follow_me=follow_me, follows_count=follows_count, weibos_count=weibos_count,
                                  person_url=person_url, level=level, following=following)
            print(user_item)
            yield response.follow(self.user_info.format(uid=id), callback=self.parse_user,
                                  meta={'uid': id, 'user_item': user_item})
            # # 关注
            yield Request(self.follow_url.format(uid=id, page=1), callback=self.parse_follows,
                          meta={'page': 1, 'uid': id})
            # 粉丝
            # yield Request(self.fans_url.format(uid=id, page=1), callback=self.parse_fans,
            #               meta={'page': 1, 'uid': id})

    def parse_user(self, response):
        """
        解析用户信息
        :param response: Response对象
        :return:
        """
        result = json.loads(response.text)
        print(result)
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
        # 关注
        user_item = response.meta['user_item']
        uid = user_item.get('id')
        yield Request(self.follow_url.format(uid=uid, page=1), callback=self.parse_follows,dont_filter=True,
                      meta={'page': 1, 'uid': uid})

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
                    yield Request(self.user_url.format(uid=uid), callback=self.parse)

            # 关注列表
            uid = response.meta.get('uid')
            user_relation_item = User_id()
            follows = [{'id': follow.get('user').get('id')} for follow in
                       follows]
            user_relation_item['id'] = uid
            user_relation_item['follow'] = follows
            # user_relation_item['fans'] = []
            yield user_relation_item
            # 下一页关注的好友
            page = response.meta.get('page') + 1
            time.sleep(4)
            # yield Request(self.follow_url.format(uid=uid, page=page), callback=self.parse_follows,
            #               meta={'page': page, 'uid': uid})
