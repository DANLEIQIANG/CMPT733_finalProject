import uuid
from flask import Flask, request, json, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()

#https://www.cnblogs.com/beifangls/p/9782172.html
# search
stus = Article.query.all()
print(stus)