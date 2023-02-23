from flask import render_template, request, Blueprint, abort
from news_project.news_source.ndtv_api import fetch_general_news
from news_project import paginate


general = Blueprint("general", __name__)


#* General News view
@general.route("/<news_category>", methods=["GET", "POST"])
def general_news(news_category):
    
    uri = f"https://ndtvapi.vercel.app/general?category=values({news_category})"
    print(uri)
    news_list = fetch_general_news(uri)
    
    if len(news_list) != 0:
        print("Fetched Data COunt : {}".format(len(news_list)))
        try:
            page = int(request.args.get("page", 1))
        except ValueError:
            page = 1
        separated_news_list, pagination = paginate(
            news_list=news_list, current_page=page, per_page=9
        )
        return render_template(
            "general.html",
            news_list = separated_news_list,
            pagination = pagination,
            options = [
                "latest",
                "india",
                "world",
                "entertainment",
                "science",
                "business",
                "offbeat",
            ],
            page_title = news_category,
        )
    
    else:
        print("incorrect request")
        abort(404)


#* Sports Home tiles view
@general.route("/sports")
def select_sports():
    return render_template("sports_home.html")


#* Sports News View
@general.route("/sports/<sport_name>", methods=["GET", "POST"])
def sports_news(sport_name):
    
    uri = f"https://ndtvapi.vercel.app/sports?sport=values({sport_name})"
    print(uri)
    news_list = fetch_general_news(uri)
    
    if len(news_list) != 0:
        print("Fetched Data COunt : {}".format(len(news_list)))
        try:
            page = int(request.args.get("page", 1))
        except ValueError:
            page = 1
        separated_news_list, pagination = paginate(
            news_list=news_list, current_page=page, per_page=9
        )
        return render_template(
            "sports.html",
            news_list = separated_news_list,
            pagination = pagination,
            options = [
                "cricket",
                "football",
                "tennis",
                "formula-1",
                "hockey",
                "golf",
                "badminton",
                "chess",
                "kabaddi",
                "wrestling",
                "nba",
                "boxing",
            ],
            page_title = sport_name,
        )
    
    else:
        print("incorrect request")
        abort(404)


#* City News view
@general.route("/cities", defaults={"city_name": None})
@general.route("/cities/<city_name>", methods=["GET", "POST"])
def city_news(city_name):
    
    if city_name is not None:
        uri = f"https://ndtvapi.vercel.app/cities?city=values({city_name})"
    else:
        uri = "https://ndtvapi.vercel.app/cities"
        city_name = "city"
    print(uri)
    news_list = fetch_general_news(uri)
    
    if len(news_list) != 0:
        print("Fetched Data COunt : {}".format(len(news_list)))
        try:
            page = int(request.args.get("page", 1))
        except ValueError:
            page = 1
        
        separated_news_list, pagination = paginate(
            news_list=news_list, current_page=page, per_page=9
        )
        return render_template(
            "cities.html",
            news_list = separated_news_list,
            pagination = pagination,
            options = [
                "agra",
                "ahmedabad",
                "allahabad",
                "amritsar",
                "aurangabad",
                "bangalore",
                "bhopal",
                "bhubaneshwar",
                "chandigarh",
                "chennai",
                "delhi",
                "ghaziabad",
                "goa",
                "gurgaon",
                "guwahati",
                "hyderabad",
                "jaipur",
                "jammu",
                "kanpur",
                "kolkata",
                "lucknow",
                "ludhiana",
                "meerut",
                "mumbai",
                "muzaffarnagar",
                "muzaffarpur",
                "nagpur",
                "noida",
                "others",
                "patna",
                "pune",
                "srinagar",
                "surat",
                "thiruvananthapuram",
            ],
            page_title = city_name,
        )
    
    else:
        print("incorrect request")
        abort(404)