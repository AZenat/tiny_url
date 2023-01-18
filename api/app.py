import datetime
import os
import secrets
import string
import sys

import validators
from flask import Flask
from flask import render_template, request, redirect, abort
from flask_cors import CORS
from flask_jwt_extended import JWTManager

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from database import db
from database.operation import *
from database.url import URL
from config import config

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = False
app.config.setdefault('JWT_ACCESS_TOKEN_EXPIRES', datetime.timedelta(minutes=1))
app.config.setdefault('JWT_REFRESH_TOKEN_EXPIRES', datetime.timedelta(days=7))
app.config.setdefault('JWT_HEADER_NAME', 'JWT_Authorization')
app.secret_key = config.api_secret_key
jwt = JWTManager(app)


@app.get("/")
def index():
    return render_template("index.html")


def create_random_key():
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(7))


def create_url(long_url):
    short_url = create_random_key()
    while get_db_url(db.session, short_url):
        short_url = create_random_key()
    return URL(long_url=long_url, short_url=short_url)


@app.post("/url")
def post_url():
    long_url = request.form["url"]
    if not validators.url(long_url):
        return abort(400)
    url = create_url(long_url)
    create_db_url(db.session, url)
    return render_template("success.html", url=url, base_url=config.api_base_url)


@app.get("/<short_url>")
def resolve(short_url):
    url = db.session.query(URL).filter(URL.short_url == short_url).first()
    if url:
        increment_db_click(db.session, url)
        return redirect(url.long_url, 301)
    else:
        abort(404)


@app.route("/stats")
@app.route("/stats/<int:page>")
def stats(page=1):
    stats = db.session.query(URL).order_by(URL.id.desc())
    return render_template("stats.html", stats=stats)


@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html'), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host=config.api_host, port=config.api_port)
