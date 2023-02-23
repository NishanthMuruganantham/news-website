from flask import render_template, Blueprint
from news_project.news_source.ndtv_api import fetch_general_news


core = Blueprint("core", __name__)


#* Home Page View
@core.route("/")
def index():
    
    uri = "https://ndtvapi.vercel.app/{}?{}=values({})"
    
    home_latest_news = fetch_general_news(uri = uri.format("general", "category", "latest"))
    home_india_news = fetch_general_news(uri = uri.format("general", "category", "india"))
    home_world_news = fetch_general_news(uri = uri.format("general", "category", "world"))
    home_business_news = fetch_general_news(uri = uri.format("general", "category", "business"))
    home_football_news = fetch_general_news(uri = uri.format("sports", "sport", "football"))
    home_cricket_news = fetch_general_news(uri = uri.format("sports", "sport", "cricket"))
    home_tennis_news = fetch_general_news(uri = uri.format("sports", "sport", "tennis"))
    
    return render_template(
        "index.html",
        home_latest_news = home_latest_news,
        home_india_news = home_india_news,
        home_world_news = home_world_news,
        home_business_news = home_business_news,
        home_football_news = home_football_news,
        home_cricket_news = home_cricket_news,
        home_tennis_news = home_tennis_news,
    )


#* 404 Error View
@core.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html")