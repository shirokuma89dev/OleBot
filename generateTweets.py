import MeCab
import markovify
import os

## CONFIG
TWEETS_TXT_PATH = "out/tweets.txt"
OUT_PATH = "out/bot_tweets.txt"

NUM_TWEETS = 10

## ツイートデータを読み込む
with open(TWEETS_TXT_PATH, "r") as file:
    text = file.read()

## ツイートデータを形態素解析して、マルコフ連鎖モデルを学習する
m = MeCab.Tagger("-r /etc/mecabrc -Owakati")
parsed_text = "\n".join(m.parse(line).strip() for line in text.split("\n"))

model = markovify.NewlineText(parsed_text)

## 再生成するために前回の出力を削除
if os.path.exists(OUT_PATH):
    os.remove(OUT_PATH)

with open(OUT_PATH, "w") as outfile:
    for i in range(NUM_TWEETS):
        ## 新しいツイートを生成する
        new_tweet = model.make_short_sentence(140, tries=200)
        new_tweet = new_tweet.replace(" ", "")
        outfile.write(new_tweet + "\n")