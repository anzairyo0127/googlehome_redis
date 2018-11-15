'''
uwsgiで起動するページです。
基本的にはここを弄ってください。
'''

# -*- coding: utf-8 -*-

import flask
from flask_assistant import Assistant, tell

app = flask.Flask(__name__)
assist = Assistant(app)


@app.route('/')
def index():
    '''
    http://127.0.0.1/ or http://192.168.99.100/ GETで繋がるページです。
    Hello, Worldと表示されます。
    '''
    return 'Hello, World'


@assist.action('Demo')
def hello_world():
    '''
    https://flask-assistant.readthedocs.io/en/latest/ 
    詳しくは上を参照してください。
    （なお、モジュールとか、やりかたとか、変更してもいいと思います。）
    おそらくですが、このページにアクセスしたGoogleHomeが
    Microphone check 1, 2 what is this?と喋ってくれるんだと思う…
    '''
    speech = 'Microphone check 1, 2 what is this?'
    return tell(speech)


if __name__ == '__main__':
    app.run(debug=True)
