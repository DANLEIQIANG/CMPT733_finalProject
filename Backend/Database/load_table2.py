import pandas as pd
import os
from flask import Flask
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

class Tbl_model_show(db.Model):
    __tablename__ = 'tbl_model_show'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    type = db.Column(db.String(64))
    labels = db.Column(db.Integer)
    counts = db.Column(db.Integer)
    period = db.Column(db.Integer)

db.create_all()

def load_db(df1, type, p_v):
    df1 = df1[['date','classification_labels']]
    df1 = df1.drop(df1[df1['date']=='date'].index)
    df1['type'] = type
    df1['period'] = p_v 
    a = df1.groupby(['date','classification_labels','type','period'])['classification_labels'].count()
    for i,v in a.items():
        table_1 = Tbl_model_show( type= i[2], period = i[3], date = i[0], labels = i[1], counts = v)
        db.session.add(table_1)

    db.session.commit()
    return

def read_csv(path, type, period):
    f = open(path, encoding='utf-8')
    df = pd.read_csv(f)
    load_db(df, type, period)

rootdir = r"model_show"   
for parent,dirnames,filenames in os.walk(rootdir):
    for f_name in filenames:
        path = os.path.join(parent, f_name)
        filter = path.split('/')
        if filter[1] == '.DS_Store':
            pass
        else:
            type = ''
            period = 0
            if filter[1] == 'biden':
                type = 'politic'
                period = 1
            elif filter[1] == 'trump':
                type = 'politic'
                period = 0
            elif filter[1] == 'before_covid':
                type = 'covid'
                period = 0
            elif filter[1] == 'after_covid':
                type = 'covid'
                period = 1
            elif filter[1] == 'holiday_week':
                type = 'war'
                period = 1
            elif filter[1] == 'normal_week':
                type = 'war'
                period = 0
            elif filter[1] == 'war_week':
                type = 'war'
                period = 2
            read_csv(path, type, period)