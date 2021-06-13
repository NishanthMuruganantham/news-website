from flask import render_template, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    return render_template("index.html")

@core.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html")