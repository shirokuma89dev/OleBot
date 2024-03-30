# OleBot

![OleBot_Logo](https://github.com/shirokuma89dev/OleBot/assets/47915291/19db04b6-5854-4ccb-af3c-f2adc0762d18)

マルコフ連鎖を使って俺っぽい文章を生成するPythonプログラムです！！

## How To Use

### 1. Twitterデータの準備

<img width="1073" alt="スクリーンショット 2024-03-30 18 01 02" src="https://github.com/shirokuma89dev/OleBot/assets/47915291/632932a1-776b-4d39-99f2-1a64c58e8462"><br>

Twitterの設定から過去のツイートを取得してください。必要なのは.zipファイルに含まれるtweets.jsのみです。クローンしたリポジトリの中のassets内に配置してください。

### 2. Docker環境の整備

環境を汚したくないので、今回はDockerを用いて環境構築をしました。あらかじめDockerシステムをご自身のパソコンにインストールしてください。

まずDockerイメージをビルドして、コンテナを作成します。これは初回のみで構いません。

``` bash
docker build -t olebot ./
docker create --name olebot -v `pwd`:/olebot -it olebot /bin/bash
```

次に、Dockerコンテナを起動します。

``` bash
docker start olebot && docker attach olebot  
```

### 3. ツイートをテキストに展開

作業ディレクトリは`/olebot`にあります。

``` bash
cd /olebot
```

.jsファイルをそのまま学習させることはできないので、ツイートの内容だけを抽出します。実行後に/olebot/out内にtweets.txtが生成されているはずです。

``` bash
python retrieveTweetsJsToText.py
```

retrieveTweetsJsToText.pyのCONFIG欄を編集することで、いつからのツイートを列挙するか等を変更できます。

``` python
## CONFIG ##
TWEETS_SINCE = datetime(2022, 4, 1)
TWEETS_JS_PATH = "assets/tweets.js"
OUT_PATH = "out/tweets.txt"
```

### 4. 生成

``` bash
python generateTweets.py
```

/olebot/out内にbot_tweets.txtが生成されます。あとは、予約投稿するなり、1人で見て眺めるなりとご自由にお楽しみください。Twitterに自動で呟く機能はありません。
