import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgres://teste:teste@localhost/test")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/database")
def database():
    users = db.execute("SELECT * FROM users").fetchall()
    return render_template("database.html", users=users)

@app.route("/info")
def about():
    return render_template("infos.html")
