# -*- coding: utf-8 -*-
from pymongo import MongoClient
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pyodbc

class ZhihuuserPipeline(object):
    conn = MongoClient('mongodb://localhost:27001/')
    db = conn.test
    db.authenticate("hello", "java")
    def process_item(self, item, spider):
        #print('#############',item)
        self.db.zhihu.insert(item)
        locations = '无'
        business = '无'
        school = '无'
        major = '无'
        description = '无'
        job_expreience = '无'

        name = item.get('name')
        print('姓名： ', name)
        # 性别
        gender = item.get('gender')
        print('性别： ', gender)
        # 居住地
        if len(item.get('locations')) != 0:
            locations = item.get('locations')[0].get('name')
        print('居住地： ', locations)
        # 所在行业
        if item.get('business') != None:
            business = item.get('business').get('name')
        print('所在行业： ', business)
        # 教育经历
        if len(item.get('educations')) > 0:
            if 'school' in item.get('educations')[0].keys():
                school = item.get('educations')[0].get('school').get('name')
            if 'major' in item.get('educations')[0].keys():
                major = item.get('educations')[0].get('major').get('name')
        print('学校：', school)
        print('专业： ', major)
        # 个人简介
        if item.get('description') != '':
            description = item.get('description')
        print('个人简介： ', description)
        # 从业经历
        if len(item.get('employments')) != 0:
            if 'company' in item.get('employments')[0].keys() and 'job' in item.get('employments')[0].keys():
                job_expreience = item.get('employments')[0].get('company').get('name') + item.get('employments')[0].get('job').get('name')
            elif 'company' in item.get('employments')[0].keys():
                job_expreience = item.get('employments')[0].get('company').get('name')
            elif 'job' in item.get('employments')[0].keys():
                job_expreience = item.get('employments')[0].get('job').get('name')
        print('工作经历： ', job_expreience)
        # 关注了多少人
        following_count = item.get('following_count')
        print('关注多少人：', following_count)
        # 被多少人关注
        follower_count = item.get('follower_count')
        print('被多少人关注： ', follower_count)
        # 获得的赞同数
        voteup_count = item.get('voteup_count')
        print('获得的赞同： ', voteup_count)
        # 获得的感谢数
        thanked_count = item.get('thanked_count')
        print('获得的感谢数： ', thanked_count)

        # 被收藏数
        favorited_count = item.get('favorited_count')
        print('被收藏数： ', favorited_count)
        # 关注的专栏数
        following_columns_count = item.get('following_columns_count')
        print('关注的专栏数： ', following_columns_count)
        # 关注的收藏夹
        following_favlists_count = item.get('following_favlists_count')
        print('关注的收藏夹： ', following_favlists_count)
        # 关注的问题数
        following_question_count = item.get('following_question_count')
        print('关注的问题数： ', following_question_count)
        # 关注的话题
        following_topic_count = item.get('following_topic_count')
        print('关注的话题数： ', following_topic_count)
        # 回答数
        answer_count = item.get('answer_count')
        print('回答数： ', answer_count)
        # 提问数
        question_count = item.get('question_count')
        print('提问数： ', question_count)
        # 分享数
        articles_count = item.get('articles_count')
        print('分享数： ', articles_count)
        # 收藏数
        favorite_count = item.get('favorite_count')
        print('收藏数： ', favorite_count)
        # 参与公共编辑数
        logs_count = item.get('logs_count')
        print('参与公共编辑数： ', logs_count)
        # 个人主页url
        personal_url = 'https://www.zhihu.com/people/' + item.get('url_token')
        print('个人主页： ', personal_url)

        # url_token
        token = item.get('url_token')
        print('url_token： ', token)
        print('======================帅气的分隔符========================')

        #return item

