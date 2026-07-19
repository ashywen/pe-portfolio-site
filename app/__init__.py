import os
import re
import datetime

import pymysql
pymysql.install_as_MySQLdb()

from playhouse.shortcuts import model_to_dict
from flask import Flask, render_template
from flask import request
from dotenv import load_dotenv
from peewee import *
from app.data import work_experience, education, hobbies, pages, about_me, travel

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )
print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


if os.getenv("TESTING") != "true":
    mydb.connect()
    mydb.create_tables([TimelinePost])


@app.route('/')
def home():
    return render_template(
        'home.html',
        title="About Me",
        url=os.getenv("URL"),
        about_me=about_me,
        work=work_experience,
        education=education,
        travel=travel,
        pages=pages
    )


@app.route('/hobbies')
def hobbies_page():
    return render_template(
        'hobbies.html',
        title="My Hobbies",
        url=os.getenv("URL"),
        hobbies=hobbies,
        pages=pages
    )


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    content = request.form.get('content', '').strip()

    if not name:
        return "Invalid name", 400
    if not content:
        return "Invalid content", 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email", 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route('/timeline')
def timeline():
    return render_template(
        'timeline.html',
        title="Timeline",
        url=os.getenv("URL"),
        pages=pages
    )