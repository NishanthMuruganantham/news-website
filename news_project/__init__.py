from flask import Flask
from flask_paginate import Pagination


#* initialising Flask app
app = Flask(__name__)


#* function to decide the pagination
def paginate(news_list, current_page, per_page):
    i = (current_page - 1) * per_page
    seperated_list = news_list[i : i + per_page]
    
    pagination = Pagination(
        page = current_page,
        per_page = per_page,
        total = len(news_list),
        record_name = "List",
        prev_label = "previous",
        next_label = "next",
        bs_version = 3,
    )
    
    return seperated_list, pagination


#* registering the declared blueprint
from news_project.news_apps.core import core
from news_project.news_apps.general_news import general
app.register_blueprint(core)
app.register_blueprint(general)