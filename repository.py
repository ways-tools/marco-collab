# function 1 - getAllArticles()
# function 2 - createArticle(article)

# class Article { name: string, id: int }

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Article('{self.id}', '{self.name}')"
