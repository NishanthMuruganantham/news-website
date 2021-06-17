import requests
from datetime import datetime


def fetch_general_news(uri):
    r = requests.get(uri)
    total_news_json = r.json()
    total_articles_collection = total_news_json["news"][0]["articles"]
    
    #* fetching news count which are only divisible by 9 to feed proper tile views in news page
    l = len(total_articles_collection) % 9
    news_list = total_articles_collection[0 : len(total_articles_collection) - l]
    
    for i in news_list:
        try:
            i["posted_date"] = datetime.strptime(i["posted_date"], "%Y-%m-%d")
        except ValueError:
            i["posted_date"] = None
    
    print("called and fetched")
    return news_list