from flask import render_template, request, Blueprint, abort
from news_project.news_source.ndtv_api import fetch_general_news
from news_project import paginate


general = Blueprint('general', __name__)

@general.route("/<news_category>",methods=["GET", "POST"])
def general_news(news_category):
    
    uri = f"https://ndtvnews-api.herokuapp.com/general?category=values({news_category})"
    print(uri)
    news_list = fetch_general_news(uri)
    if len(news_list) != 0:
        try:
            page = int(request.args.get("page", 1))
        except ValueError:
            page = 1
        
        separated_news_list, pagination = paginate(news_list = news_list, current_page = page, per_page = 9)
        print(separated_news_list)
        return render_template(
            "india.html", news_list = separated_news_list, pagination = pagination
        )
    
    else:
        abort(404)


@general.route("/sports")
def select_sports():
    return render_template("sports_home.html")