from fake_useragent import UserAgent
import time, random
import requests, chardet, csv
from lxml import etree


# 登录
def longins(url):
    login_url = 'https://www.zhihu.com/signin?next=%2F'
    authorization = {'username': '741599771@qq.com', 'password': 'wswqx2288'}
    sessions = requests.session()
    response = sessions.post(url=login_url, headers=headers, data=authorization)
    response.encoding = 'utf-8'
    print(response.cookies)
    res = sessions.get(url,headers=headers,cookies=response.cookies)
    res = res.text
    print(res)


if __name__ == '__main__':
    head={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',

    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        # 'Cookie': '_zap=a8055adb-04a8-4635-83fe-bcb3e0f71dbd; _xsrf=k2IGac4UmvJPvywS96kPPmEMqOMj8FRo; d_c0="AKBjUPYzzA6PTi5950poz_hrfGsd_E7sQxs=|1547001998"; q_c1=8cc09a56b0714206b24d7f80c257acaa|1547005798000|1547005798000; __gads=ID=1d1e8befe950b0c7:T=1547006740:S=ALNI_MZvlVJGTvHTYBeXOFrJjRZEYkjvKA; capsion_ticket="2|1:0|10:1547018401|14:capsion_ticket|44:YTU2OThlMjBjYTJhNDM4MDhlOGI3OGVhMmQwMTA4OTE=|88e02f980e3f1336596e392380f5bee03961d5599df466d316ac88ecf45539c3"; z_c0="2|1:0|10:1547018402|4:z_c0|92:Mi4xYkNReEJ3QUFBQUFBb0dOUTlqUE1EaVlBQUFCZ0FsVk5vdTRpWFFBd2F6WlJ3Q0wwWllCWDl5N19wM25SUXZkNS1n|5394ce429ae03dd2e23c6beb9dcd3ee4855a4a91db8c77c636c1dd18a5e92b74"; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c; __utma=155987696.201660773.1547026058.1547026058.1547026058.1; __utmb=155987696.0.10.1547026058; __utmc=155987696; __utmz=155987696.1547026058.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tst=h',
        'Host': 'www.zhihu.com',
        'Origin': 'https://www.zhihu.com',
        'Referer': 'https://www.zhihu.com/people/wang-yi-bo-23-20/activities',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
        'X-Ab-Param': 'top_recall_query=1;tp_sticky_android=1;se_webrs=0;top_feedre_itemcf=31;gw_guide=0;top_billvideo=0;top_yhgc=0;tp_discussion_feed_type_android=2;top_source=0;top_gif=0;top_root_mg=1;zr_art_rec=new;top_brand=1;top_recall_tb_long=51;tp_header_style=0;top_recall=1;top_recall_tb_follow=71;tp_related_topics= a;qa_video_answer_list=0;top_f_r_nb=1;top_quality=0;li_gbdt=default;ls_new_video=1;top_limit_num=0;top_topic_feedre=21;top_user_gift=0;se_correct_ab=0;top_newuser_feed=1;top_new_user_gift=0;top_card=-1;top_round_table=0;se_consulting_switch=off;soc_zero_follow=0;top_promo=1;top_question_ask=1;tp_qa_metacard=1;se_majorob_style=0;top_accm_ab=1;top_recall_exp_v1=3;top_no_weighing=1;tp_dis_version=0;se_time_search=new;se_prf=0;tp_related_tps_movie=a;top_native_answer=1;top_recall_exp_v2=5;top_recall_tb_short=61;se_consulting_price=n;top_follow_reason=0;top_thank=1;se_auto_syn=1;se_billboardsearch=0;tp_answer_meta_guide=0;se_click2=1;se_filter=1;top_new_user_rec=0;top_rerank_video=-1;se_engine=1;top_ab_validate=4;top_feedre_cpt=101;top_followtop=1;top_root=1;top_vd_gender=0;ls_is_use_zrec=1;top_login_card=1;se_webtimebox=0;top_rerank_reformat=2;qa_answerlist_ad=0;ug_zero_follow=0;top_fqai=0;top_newfollow=0;se_daxuechuisou=new;se_search_feed=Y;se_entity=on;se_wiki_box=1;top_new_feed=2;top_test_4_liguangyi=1;se_likebutton=1;top_billab=0;top_video_score=1;zr_ans_rec=gbrank;top_mt=0;zr_article_rec_rank=base;top_recall_tb=3;ls_new_score=1;pf_creator_card=1;se_minor_onebox=d;top_scaled_score=0;ls_topic_is_use_zrec=1;se_websearch=3;top_recall_core_interest=81;qa_test=0;soc_brandquestion=1;se_colos=1;top_recall_follow_user=91;top_newfollowans=0;top_reason=1;pin_ef=orig;top_distinction=0;top_is_gr=0;top_feedre_rtt=41;top_ydyq=X;se_webmajorob=0;top_billpic=0;top_root_ac=1;top_sj=2;pf_newguide_vertical=0;pin_efs=orig;se_backsearch=0;top_ebook=0;top_universalebook=1;se_mfq=0;top_ntr=1;top_wonderful=1;tp_qa_metacard_top=0;top_cc_at=1;top_bill=0;tp_sft=a;se_bert=0;top_recall_deep_user=1;top_30=0;top_feedre=1;top_root_web=0;se_ad_index=10;top_video_rerank=1;tp_favsku=a;se_spb309=0;top_raf=y;top_tr=0;top_yc=0;top_billupdate1=3;top_hotlist=1;top_nad=1;se_new_market_search=on;top_nucc=3;tp_write_pin_guide=3;zr_art_rec_rank=base;se_gemini_service=content;top_core_session=-1;top_rank=9;tp_discussion_feed_card_type=2;zr_video_rec=zr_video_rec:base;top_v_album=1;se_major_onebox=major;tp_m_intro_re_topic=0;top_root_few_topic=0',
        'x-requested-with': 'fetch',
        'X-UDID': 'AKBjUPYzzA6PTi5950poz_hrfGsd_E7sQxs=',
        'x-xsrftoken': 'k2IGac4UmvJPvywS96kPPmEMqOMj8FRo',
        'X-Zse-83': '3_1.1',
        'X-Zse-84': 'jkrkM__lQgraRorlgg9k0KtkK9baPg8klc8xQCdkMk8a8xNwnkrlSWtwMce_Ooem',
    }
    url = 'https://www.zhihu.com/people/liang-shui-28-60/activities'
    longins(url)
