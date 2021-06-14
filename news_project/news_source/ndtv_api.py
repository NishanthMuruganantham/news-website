import requests
import pandas as pd
from datetime import datetime


def fetch_general_news(uri):
    r = requests.get(uri)
    total_news_json = r.json()
    total_articles_collection = total_news_json["news"][0]["articles"]
    l = len(total_articles_collection)%9
    news_list = total_articles_collection[0:len(total_articles_collection)-l]
    
    for i in news_list:
        try:
            i["posted_date"] = (datetime.strptime(i["posted_date"], '%Y-%m-%d'))
        except ValueError:
            i["posted_date"] = None
    
    print("called and fetched")
    print(news_list)
    return news_list
# news_category = "science"
# uri = f"https://ndtvnews-api.herokuapp.com/general?category=values({news_category})"

# v = fetch_general_news(uri)

# print(v)