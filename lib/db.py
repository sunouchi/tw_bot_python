# coding: utf-8

# modules
# import MySQLdb

# # my library
# import '../config'

# # DBにログイン
# connection = MySQLdb.connect(db=config.DB_NAME,
#                              user=config.DB_USER,
#                              passwd=config.DB_PASSWD)


# def test():
#     cursor = connection.cursor()

#     #SQL
#     cursor.execute('select * from puzzle')
#     result = cursor.fetchall()
#     # sql = u'insert into puzzle (id, img_path) values(3, \'http://example.com/img3.png\')'
#     # cursor.execute(sql)
#     # connection.commit()

#     for i in range(4, 10):
#         sql = u'insert into puzzle (id, img_path) values(%d, \'http://example.com/img%d.png\')' % (i, i)
#         print sql
#         cursor.execute(sql)

#     connection.commit()

#     # for row in result:
#     #     print row[0]

#     cursor.close()
#     connection.close()


def save_tweet(tweet_id,
               user_id,
               screen_name,
               raw,
               created_at,
               text=None,
               place=None):
    '''ツイートをDBに保存する'''

    table = 'tweets'
    if text is None:
        text = 'NULL'
    if place is None:
        place = 'NULL'

    cursor = connection.cursor()
    print '---------------------'
    print '[Save to DB]'
    print 'sql...'
    sql = u'insert into %s (tweet_id, user_id, text, place, screen_name, raw, created_at) values(%d, %d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")' % (table, tweet_id, user_id, text, place, screen_name, raw, created_at)
    cursor.execute(sql)
    print 'done.'

    connection.commit()
    return
