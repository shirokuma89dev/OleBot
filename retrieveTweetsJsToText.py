import json
import re
import os
from datetime import datetime

## CONFIG ##
TWEETS_SINCE = datetime(2022, 4, 1)
TWEETS_JS_PATH = "assets/tweets.js"
OUT_PATH = "out/tweets.txt"

with open(TWEETS_JS_PATH, "r") as file:
    data = file.read().replace("window.YTD.tweets.part0 = ", "")
    data = json.loads(data)

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

if os.path.exists(OUT_PATH):
    os.remove(OUT_PATH)

with open(OUT_PATH, "w") as outfile:
    for tweet_data in data:
        tweet = tweet_data["tweet"]
        created_at = tweet.get("created_at")

        tweet_date = datetime.strptime(created_at, "%a %b %d %H:%M:%S +0000 %Y").date()

        ## 指定日以降か
        if tweet_date < TWEETS_SINCE.date():
            continue

        ## リプライを除外
        if tweet.get("in_reply_to_status_id") is not None:
            continue

        text = tweet["full_text"]

        ## リツイートを除外
        if text.startswith("RT"):
            continue

        ## URLを除去
        text = re.sub(r"http\S+|www.\S+", "", text, flags=re.MULTILINE)

        text = re.sub(r"@\w+", "", text)  ## IDを除去
        text = text.replace("\n", " ")  ## 改行を除去

        outfile.write(text + "\n")
