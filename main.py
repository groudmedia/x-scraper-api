from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import snscrape.modules as sn
import pandas as pd

app = FastAPI()

@app.get("/scrape")
def scrape(handle: str = Query(...), limit: int = 500):
    tweets = []
    for i, tweet in enumerate(sn.TwitterUserScraper(handle).get_items()):
        if i >= limit:
            break
        tweets.append({
            "date": tweet.date.strftime("%Y-%m-%d %H:%M:%S"),
            "text": tweet.content,
            "likes": tweet.likeCount,
            "replies": tweet.replyCount,
            "url": tweet.url,
        })

    df = pd.DataFrame(tweets)
    df = df.sort_values(by="likes", ascending=False).head(100)
    return JSONResponse(content=df.to_dict(orient="records"))
