from flask import Flask, render_template, request
from flask_paginate import Pagination
from indian import fetch_news
app = Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")

def paginate(news_list, current_page, per_page):
    i = (current_page - 1) * per_page
    seperated_list = news_list[i : i + 9]
    
    pagination = Pagination(
        page = current_page,
        per_page = per_page,
        total = len(news_list),
        record_name = "List",
        prev_label = "previous",
        next_label = "next",
        bs_version=3,
    )
    
    return seperated_list, pagination



@app.route("/<news_category>",methods=["GET", "POST"])
def general_news(news_category):
    
    uri = f"https://ndtvnews-api.herokuapp.com/general?category=values({news_category})"
    print(uri)
    news_list = fetch_news(uri)
    
    try:
        page = int(request.args.get("page", 1))
    except ValueError:
        page = 1
    
    separated_news_list, pagination = paginate(news_list = news_list, current_page = page, per_page = 9)
    print(separated_news_list)
    return render_template(
        "india.html", news_list = separated_news_list, pagination = pagination
    )





@app.route("/world")
def world():
    uri = "https://ndtvnews-api.herokuapp.com/general?category=values(world)"
    news_list = fetch_news(uri)
    
    page = request.args.get("page",1,type = int)
    
    print(page)
    PER_PAGE = 9 
    List=news_list
    i=(page-1)*PER_PAGE
    List1=List[i:i+9]
    print(len(List1))
    pagination = Pagination(page=page,per_page=PER_PAGE, total=len(List),record_name='List',prev_label="previous",
                            next_label = "next",search_msg="hui",bs_version=3)
    
    return render_template("india.html",news_list = List1, pagination = pagination)

@app.route("/sports")
def sports_news():
    return render_template("sports.html")

if __name__ == "__main__":
    app.run(debug=True)