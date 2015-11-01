# coding: utf-8


def tweet(api, text, reply_to=None, hashtag=None, url=None, media=None):
    '''ツイートを投稿する'''

    if reply_to:
        content = u'@' + reply_to + u' ' + text
    else:
        content = text

    if hashtag:
        content += u' ' + hashtag
    if url:
        content += u' ' + url

    # ログに出力
    print '---------------------'
    print '[Posting tweet]'
    print '%-16s %s' % ('content', content)
    print '%-16s %s' % ('media', media)
    print 'tweeting...'

    # 画像がアップロードされる場合
    if media:
        api.PostMedia(status=content, media=media)
    else:
        api.PostUpdates(status=content)

    print 'done'
