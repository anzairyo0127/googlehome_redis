'''
uwsgiで起動するページです。
基本的にはここを弄ってください。
'''

# -*- coding: utf-8 -*-

import flask
from flask_assistant import Assistant, tell
import redis

app = flask.Flask(__name__)
assist = Assistant(app)


@app.route('/')
def index():
    '''
    http://127.0.0.1/ or http://192.168.99.100/ GETで繋がるページです。
    Hello, Worldと表示されます。
    '''
    return 'Hello, World'


@app.route('/redis/<num>')
def get_redis(num):
    '''
    http://127.0.0.1/redis/<int>/ or http://192.168.99.100/redis/<int> GETで繋がるページ
    <int>は好きな半角数字を入れてください。
    intをキーにredisを検索していきます。
    その結果をページに表示しています。
    redis内には{1:a}と{0001:aaa}が入っています。
    redis内に入っていないキーを取り出そうとするとNoneが返却されます。
    '''
    r = redis.StrictRedis(host='172.20.0.3', port=6379, db=0)
    if r.get(num):
        return r.get(num)
    else:
        return 'None'


@assist.action('Demo')
def hello_world():
    '''
    https://flask-assistant.readthedocs.io/en/latest/ 詳しくはこちらを参照してください。
    おそらくですが、このページにアクセスしたGoogleHomeが
    Microphone check 1, 2 what is this?と喋ってくれるんだと思う…
    '''
    speech = 'Microphone check 1, 2 what is this?'
    return tell(speech)


if __name__ == '__main__':
    app.run(debug=True)
