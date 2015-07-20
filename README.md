pythonのtwitter bot
Streaming API で特定の文字列を監視して、発見したら何かのアカウントで何かをつぶやく。

## 必要モジュール
- simplejson
- httplib2
- python-oauth2
- python-twitter
- peewee

## oauth認証情報の設定
/examples/t_key.py にある cons_key, cons_sec, acc_token, acc_sec にそれぞれ設定する。

## 監視する文字列とツイート内容の設定
/examples/stream.py にそれぞれ設定してあるので、適宜変える。
