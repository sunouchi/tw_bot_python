#coding: utf-8
import key

# Twitter Keys
CONSUMER_KEY = key.CONSUMER_KEY
CONSUMER_SECRET = key.CONSUMER_SECRET
ACCESS_TOKEN = key.ACCESS_TOKEN
ACCESS_SECRET = key.ACCESS_SECRET

# Database
DB_USE_PRODUCTION = False
# dev
DB_DEVELOP_NAME = 'tweet_puzzle_development'
DB_DEVELOP_USER = 'sunouchi'
DB_DEVELOP_PASSWD = 'hoge'
# prod
DB_PRODUCTION_NAME = ''
DB_PRODUCTION_USER = ''
DB_PRODUCTION_PASSWD = ''
if DB_USE_PRODUCTION:
    DB_NAME = DB_PRODUCTION_NAME
    DB_USER = DB_PRODUCTION_USER
    DB_PASSWD = DB_PRODUCTION_PASSWD
else:
    DB_NAME = DB_DEVELOP_NAME
    DB_USER = DB_DEVELOP_USER
    DB_PASSWD = DB_DEVELOP_PASSWD
