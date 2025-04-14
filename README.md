# 🧠 X Scraper API

A simple FastAPI microservice that uses `snscrape` to fetch tweets from any public X (Twitter) user and return the **top 100 most-liked posts** including:

- ✅ Tweet content  
- ✅ Like count  
- ✅ Reply count  
- ✅ URL  
- ✅ Timestamp

## 🚀 How it works

You can send a GET request to `/scrape` with:

| Parameter | Type   | Required | Description                    |
|-----------|--------|----------|--------------------------------|
| handle    | string | ✅ yes    | X/Twitter username (without @) |
| limit     | int    | ❌ no     | Max number of tweets to scan (default: 500) |

### Example:


