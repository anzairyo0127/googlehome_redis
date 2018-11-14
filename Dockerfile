# 元のイメージ
FROM python:3.6.6
# 環境変数HOMEに/rootを設定
ENV HOME /root
# pipのアップデート
RUN pip install --upgrade pip
# pip インストールリストのコピー
COPY ./tmp/requirements.txt /tmp/requirements.txt
# Ngrokをコンテナにインストール
COPY ./tmp/ngrok /usr/bin/ngrok
# インストールリストを用いたpipによるmoduleのダウンロード
RUN pip install -r /tmp/requirements.txt