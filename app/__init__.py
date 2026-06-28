import os
from flask import Flask, render_template
from dotenv import load_dotenv

from app.data import work_experience, education, hobbies, pages, about_me, travel

load_dotenv()
app = Flask(__name__)


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
