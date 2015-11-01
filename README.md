Streaming API で特定の文字列を監視して、発見したら何かのアカウントで何かをつぶやく。

## 必要モジュール
- simplejson
- httplib2
- python-oauth2
- python-twitter
- peewee

## 使い方
- /examples/t_key.py に oauth認証情報を設定する
- /examples/stream.py に設定してある監視する文字列やツイート内容など適宜変える
- $ python examples/stream.py を実行する
