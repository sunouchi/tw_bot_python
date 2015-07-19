# coding: utf-8
import datetime
import time
import twitter
import pprint
import random
import re
import t_key


# twitter dev key
consumerKey = t_key.dict['cons_key']
consumerSecret = t_key.dict['cons_sec']
accessToken = t_key.dict['acc_token']
accessSecret = t_key.dict['acc_sec']
api = twitter.Api(consumerKey, consumerSecret, accessToken, accessSecret)


# # ユーザーの過去のツイートを取得する
# tlAry = api.GetUserTimeline('snch_dev', count=10)
# tweetlist = []

# for s in tlAry:
#     if s.text[0] != '@':
#         print s.text
#         tweetlist.append(s.text)


def post(text, reply_to=None, hashtag=None, url=None):
    if reply_to:
        content = u'@' + reply_to + u' ' + text
    else:
        content = text

    if hashtag:
        content += u' ' + hashtag
    if url:
        content += u' ' + url

    api.PostUpdates(status=content)
