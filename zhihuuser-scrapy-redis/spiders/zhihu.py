# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
import json
import multiprocessing
import pyodbc
from zhihuuser.items import UserItem


class ZhihuSpider(RedisSpider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    start_user = 'yulin-wu-97'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    #关注他的人
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), callback=self.parse_user)

        url = self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20)
        yield Request(url, callback=self.parse_follows)

        #关注他的人
        foll_url = self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20)
        yield Request(foll_url, callback=self.parse_followers)

    def parse_user(self, response):
        # 返回的信息是json格式，所以要解析

        results = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in results.keys():
                item[field] = results.get(field)
        yield item


        yield Request(self.follows_url.format(user=results.get('url_token'), include=self.follows_query, offset=0, limit=20), self.parse_follows)
        yield Request(self.followers_url.format(user=results.get('url_token'), include=self.followers_query, offset=0, limit=20), self.parse_followers)


    def parse_follows(self, response):
        results = json.loads(response.text)

        #获取到用户的url，然后进行请求
        if 'data' in results.keys():
            for result in results.get('data'):
                url_token = result.get('url_token')
                if url_token != None:
                    yield Request(self.user_url.format(user=url_token, include=self.user_query), self.parse_user)

        #判断如果不是最后一页，将获取到下一页的url
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_follows)

    #parse_followers
    def parse_followers(self, response):
        results = json.loads(response.text)

        #获取到用户的url，然后进行请求
        if 'data' in results.keys():
            for result in results.get('data'):
                url_token = result.get('url_token')
                if url_token != None:
                    yield Request(self.user_url.format(user=url_token, include=self.user_query), self.parse_user)

        #判断如果不是最后一页，将获取到下一页的url
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_followers)
            

