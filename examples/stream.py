# coding: utf-8
import twitter
import sys
import codecs
import dateutil.parser
import datetime
import time
from peewee import *
import t_key
import tweet


db = SqliteDatabase('db/twitter_stream.db')


class Twitte(Model):
    createAt = DateTimeField(index=True)
    idStr = CharField(index=True)
    contents = CharField()

    class Meta:
        database = db


# easy_install の最新版でGetStreamFilterがなければ下記のコード追加
# https://github.com/bear/python-twitter/blob/master/twitter/api.py
def GetStreamFilter(api,
                    follow=None,
                    track=None,
                    locations=None,
                    delimited=None,
                    stall_warnings=None):
    '''Returns a filtered view of public statuses.

    Args:
      follow:
        A list of user IDs to track. [Optional]
      track:
        A list of expressions to track. [Optional]
      locations:
        A list of Latitude,Longitude pairs (as strings) specifying
        bounding boxes for the tweets' origin. [Optional]
      delimited:
        Specifies a message length. [Optional]
      stall_warnings:
        Set to True to have Twitter deliver stall warnings. [Optional]

    Returns:
      A twitter stream
    '''
    if all((follow is None, track is None, locations is None)):
        raise ValueError({'message': "No filter parameters specified."})
    url = '%s/statuses/filter.json' % api.stream_url
    data = {}
    if follow is not None:
        data['follow'] = ','.join(follow)
    if track is not None:
        data['track'] = ','.join(track)
    if locations is not None:
        data['locations'] = ','.join(locations)
    if delimited is not None:
        data['delimited'] = str(delimited)
    if stall_warnings is not None:
        data['stall_warnings'] = str(stall_warnings)

    json = api._RequestStream(url, 'POST', data=data)
    for line in json.iter_lines():
        if line:
            data = api._ParseAndCheckTwitter(line)
            print data['user']['name']
            print data['user']['screen_name']
            yield data


def main(track):
    # UNICODE変換する文字コードは対象のターミナルに合わせて
    track = track.decode('utf-8').split(',')

    # db.create_tables([Twitte], True)

    print 'watching twitter stream'
    api = twitter.Api(consumer_key=t_key.dict['cons_key'],
                      consumer_secret=t_key.dict['cons_sec'],
                      access_token_key=t_key.dict['acc_token'],
                      access_token_secret=t_key.dict['acc_sec'])

    for item in GetStreamFilter(api, track=track):
        print '---------------------'
        if 'text' in item:
            print (item['id_str'])
            print (dateutil.parser.parse(item['created_at']))
            print (item['text'])
            print (item['place'])
            # # DBに保存する
            # row = Twitte(createAt=dateutil.parser.parse(item['created_at']),
            #              idStr=item['id_str'],
            #              contents=item['text'])
            # row.save()
            # row = None

            tweet.post(reply_to=item['user']['screen_name'].decode('utf-8'),
                       text=u'明日はピアノの発表会だけどBEAT IT!!',
                       # hashtag=u'#test',
                       url=u'http://j.mp/1gDlYWf')

            # print 'type: %s' % type(item['user']['screen_name'])
            # cont_txt = item['user']['screen_name'] + 'さんが何かをツイートしてます'
            # cont_txt = u'%sさんが何かをツイートしてます' % item['user']['screen_name']
            # cont_url = 'https://twitter.com/%s/status/%s' % (item['user']['screen_name'], item['id_str'])
            # tweet.post(text=cont_txt,
            #            url=cont_url)

# track = 'こんばんは'
track = '#わたなべくんとコンパしたい'
main(track)
