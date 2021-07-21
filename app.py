from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect

from other_app import test_dict

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
def test():
    hello = 'Hello World!'
    return hello


def articles():
    return getAllArticles()


if __name__ == '__main__':
    app.run(debug=True)
