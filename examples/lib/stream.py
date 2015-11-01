# coding: utf-8

# modules
import dateutil.parser
from peewee import *
import re

# my library
import db


# easy_install の最新版でget_stream_filterがなければ下記のコード追加
# https://github.com/bear/python-twitter/blob/master/twitter/api.py
def get_stream_filter(api,
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
            yield data


def get(api, track, callback=None):
    '''Streamのツイートを検知してDBに保存する'''

    if track:
        print 'watching %s on twitter stream...' % track[0]
    else:
        print 'watching twitter stream...'

    for item in get_stream_filter(api, track=track):
        print '---------------------'
        print '[Getting tweet]'
        if 'text' in item:
            print '%-16s %s' % ('created_at', dateutil.parser.parse(item['created_at']))
            print '%-16s %s' % ('text', item['text'])
            print '%-16s %s' % ('place', item['place'])
            print '%-16s %s' % ('url', ('https://twitter.com/' + item['user']['screen_name'] + '/status/' + item['id_str']))

            # DBに保存する
            pattern = re.compile('"')
            repl = '\\"'
            db.save_tweet(tweet_id=item['id'],
                          user_id=item['user']['id'],
                          text=re.sub(pattern, repl, item['text']),
                          place=item['place'],
                          screen_name=item['user']['screen_name'],
                          raw=re.sub(pattern, repl, str(item)),
                          created_at=item['created_at'])

            if callback:
                callback()
