# はじめに
## クイックスタート

docker-compose.ymlのあるディレクトリをカレントディレクトリにした状態で、以下のコマンドを打ちます。

```
docker-compose up -d --build
```

なお、Dockerfileの更新がなければ、二回目以降は以下のコマンドを使います。

```
docker-compose up -d
```

以下のようなログが出ていれば成功しています。

```
Creating network "ghome_default" with the default driver
Creating google_home_ctr ... done
Creating redius_ctr      ... done
```

この時点でuwsgiが起動しております。以下のURLを開いてみてください。

DockerとDockerToolboxでIPアドレスが異なりますが、これはDockerToolboxが`Defalut`という名前のDockerMachineというものを用いて使用しているからになります。詳細は`DockerToolbox DockerMachine`で調べてみてください。

```
[Docker]
http://127.0.0.1:3031
[Docker Toolbox]
http://192.168.99.100:3031
```

そうしましたら、以下のコマンドを打ち、Ngrokを起動します。なお、コマンドを打っても黒い画面のままになる事が結構な頻度で出ます。その場合は`Ctrlキー`と`cキー`を同時押ししてNgrokを中止し、もう一度`docker-compose exec home ngrok http 3031`コマンドを実行してください。

```
docker-compose exec home ngrok http 3031
```

成功していれば以下のような文字が表示されているはずです。

```
Session Status                online
Session Expires               7 hours, 59 minutes
Version                       2.2.8
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://08f4fea3.ngrok.io -> localhost:3031
Forwarding                    https://08f4fea3.ngrok.io -> localhost:3031
```

`Forwarding`が二つあり、その右側にURLが書かれています。そのURLが外部に公開されているものになります。今回の場合、`https://08f4fea3.ngrok.io`がURLとなります。なお、この値はNgrokを起動するたびに変更されます。これはNgrokがURLを都度変更するような仕様にしていることが要因です。また、`Session Expires`と書いてある通り、制限時間もあることも留意してください。

Ngrokやめる場合は`Ctrlキー`と`cキー`を同時押ししてください。使っているパソコンのターミナルに戻ってこれるはずです。

パソコンを閉じる、作業を中断する、という場合はコンテナを閉じたほうがよいでしょう。以下のコマンドを打ってください。

```
docker-compose down
```

以下のようなログが出力され、閉じられました。

```
Stopping redius_ctr      ... done
Stopping google_home_ctr ... done
Removing redius_ctr      ... done
Removing google_home_ctr ... done
Removing network ghome_default
```

## pythonイメージのモジュールを追加、変更する場合

`tmp/requirements.txt`を編集し、イメージの`buid`を行ってください。

`module名==ver数字`になっています。

なおモジュールの追加はpipにて行っています。

元のModule一覧
```
Flask==1.0.2
uwsgi==2.0.17
redis==2.10.6
flask-assistant==0.2.99
aniso8601==4.0.1
```

イメージの`build`は以下のコマンドを打ってください。

```
[新たにイメージのbuildだけを行う場合]
docker-compose build
[新たにbuildを行い、かつ、コンテナを立ち上げる場合]
docker-compose up -d --build
```

## コンテナへの侵入…docker-compose exec …について

コンテナに侵入したい場合は以下のコマンドを打つと良いでしょう

```
docker-compose exec home /bin/bash
```

`docker-compose exec サービス名 shコマンド`となっており、`サービス名`とは`docker-compose.yml`の`service`の階層に書いている名前になります。

DockerComposeとしてイメージにあれこれ設定を付け加えたものを`サービス`という単位で呼んでいます。

今回はpythonが入ったサービスの名称を`home`にしました。`home`がダサくてムカつくって人は`docker-compose.yml`のservice階層の`home`って書かれているところを変えてください。

`docker-compose exec home /bin/bash`はBashを呼び出しています。

Ngrokを使うときのコマンドは`docker-compose exec home ngrok http 3031`と書いたと思います。

`ngrok http 3031`は`Ngrok`というソフトを用いてhttpのport番号`3031`を開放して外部公開してください、というコマンドになります。

## uwsgiについて
flaskのwebページ出力は`uwsgi`を使っており、uwsgiの設定ファイルで`page.py`という名称のpythonプログラムをport:3031で出力しています。

もし、`page.py`という名称を変更したい場合は`uwsgi.ini`ファイルの以下の部分を更新しコンテナを再起動してください。

```
wsgi-file = page.py ←ここを更新
```

## Redisの連携について