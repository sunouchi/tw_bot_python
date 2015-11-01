# coding: utf-8

# modules
import twitter
import sys
import codecs
import dateutil.parser
import datetime
import MySQLdb
import time
from peewee import *
import random
import re
import math
import atexit

# my library
import config
import lib.post
import lib.stream


# DBにログイン
connection = MySQLdb.connect(db=config.DB_NAME,
                             user=config.DB_USER,
                             passwd=config.DB_PASSWD)

# db = SqliteDatabase('db/twitter_stream.db')

api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN,
                  access_token_secret=config.ACCESS_SECRET)
replies = [
    {
        'text': '0です',
        'media': 'images/0.jpg'
    },
    {
        'text': '1です',
        'media': 'images/01.jpg'
    },
    {
        'text': '2です',
        'media': 'images/02.jpg'
    },
    {
        'text': '3です',
        'media': 'images/03.jpg'
    },
    {
        'text': '4です',
        'media': 'images/04.jpg'
    },
    {
        'text': '5です',
        'media': 'images/05.jpg'
    },
    {
        'text': '6です',
        'media': 'images/06.jpg'
    },
    {
        'text': '7です',
        'media': 'images/07.jpg'
    },
    {
        'text': '8です',
        'media': 'images/08.jpg'
    },
    {
        'text': '9です',
        'media': 'images/09.jpg'
    }
]


# class Twitte(Model):
#     createAt = DateTimeField(index=True)
#     idStr = CharField(index=True)
#     contents = CharField()

    # class Meta:
    #     database = db


# def random_tweet():
#     '''ランダムに画像付きツイートをする'''

#     num = int(math.floor(random.random() * 10))
#     print num
#     text = replies[num]['text'].decode('utf-8')
#     media = replies[num]['media']
#     post.post(text=text, media=media)
#     return


def post_tweet_changed_by_hour(created_at):
    '''According to tweeted hour, post different tweet.

    Args:
        created_at:
            A RFC 822 based datetime format data.
            This is expected to set twitter streaming API data 'created_at'.
    '''
    dt = dateutil.parser.parse(created_at)
    dt_jp = dt + datetime.timedelta(hours=9)
    hour = dt_jp.hour
    print hour

    if (20 <= hour and hour < 24) or (0 <= hour and hour < 4):
        print 'night.'
    elif (4 <= hour and hour < 12):
        print 'morning'
    else:
        print 'evening'

    # Not imprement to post tweet.


def main():
    # エラーなどでプログラムが終了したら、再度実装する
    # atexit.register(main)

    # UNICODE変換する文字コードは対象のターミナルに合わせて
    hashtag = '#秋だわー'
    track = hashtag.decode('utf-8').split(',')

    # twitterにpostする
    def callback():
        post.tweet(api=api,
                   text=u'こんにちは',
                   hashtag=u'#testtest',
                   url=u'http://www.google.co.jp')
        # post.tweet(api=api,
        #            text=u'こんにちは ' + str(datetime.datetime.now()),
        #            hashtag=u'#testtest',
        #            url=u'http://www.google.co.jp')

    # ストリームを監視して、ハッシュタグを検知したらツイートを投稿する
    # stream.get(api, track, callback)

    created_at = "Mon Sep 21 17:12:52 +0000 2015"  # RFC 822 企画の日時
    post_tweet_changed_by_hour(created_at)


main()
