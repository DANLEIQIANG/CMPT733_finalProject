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

class Tbl_country_label(db.Model):
    __tablename__ = 'tbl_country_label'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    country = db.Column(db.String(64))
    labels = db.Column(db.Integer)
    counts = db.Column(db.Integer)

db.create_all()

def load_db(csv_df):
    df1 = csv_df[['geo_country_code','date','classification_labels']]
    df1 = df1.drop(df1[df1['geo_country_code']=='geo_country_code'].index)

    a = df1.groupby(['geo_country_code','date','classification_labels'])['classification_labels'].count()
    for i,v in a.items():
        table_1 = Tbl_country_label(date = i[1], country = i[0], labels = i[2], counts = v)
        db.session.add(table_1)

    db.session.commit()
    return

rootdir = r"tw_2021_csv"   
for parent,dirnames,filenames in os.walk(rootdir):
    for f_name in filenames:
        f = open(os.path.join(rootdir, f_name), encoding='utf-8')
        df = pd.read_csv(f)
        load_db(df)

#update contry
Tbl_country_label.query.filter_by(country='AU').update({'country':'Australia'})
Tbl_country_label.query.filter_by(country='US').update({'country':'United States'})
Tbl_country_label.query.filter_by(country='CA').update({'country':'Canada'})
Tbl_country_label.query.filter_by(country='NZ').update({'country':'New Zealand'})
Tbl_country_label.query.filter_by(country='GB').update({'country':'United Kingdom'})
db.session.commit()