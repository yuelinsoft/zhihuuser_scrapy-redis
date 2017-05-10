# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    # define the fields for your item here like:
    _id = Field()
    name = Field()
    gender = Field()
    locations = Field()
    business = Field()
    educations = Field()
    description = Field()
    employments = Field()
    following_count = Field()
    follower_count = Field()
    voteup_count = Field()
    thanked_count = Field()
    favorited_count = Field()
    following_columns_count = Field()
    following_favlists_count = Field()
    following_question_count = Field()
    following_topic_count = Field()
    answer_count = Field()
    question_count = Field()
    articles_count = Field()
    favorite_count = Field()
    logs_count = Field()
    url_token = Field()



