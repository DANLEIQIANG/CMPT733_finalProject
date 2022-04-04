import uuid
from flask import Flask, request, json, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

import config
'''
本地创建新数据库 twitter
修改config.py里的用户名和密码
运行这个文件
'''
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article2'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()

#https://www.cnblogs.com/beifangls/p/9782172.html
# search
stus = Article.query.all()
for item in stus:
    # print(item.title)
    # print(item.content)
    print(item.title)
