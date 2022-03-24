from flask import Flask
import random
app = Flask(__name__)

# 多类型 friendly和unfriendly
# eda: 1.词频图  前端展示图片（eda）
# 数据内容：数据随机采样
# 推文(数据初步清洗) 用户信息
# 3.9搞完 + vedio



#指标卡 & 饼图


@app.route('/api/timeselector/<startTime>_<endTime>')
def timeselector(startTime,endTime):
    a = random.randint(0,9)*1000
    b = random.randint(0,9)*1000
    return  {
        "error_code": 0,
        "date": ["2020/09/01","2020/09/02","2020/09/03","2020/09/04","2020/09/05","2020/09/06","2020/09/07"],
        "positive": [100, 520, 2000, 100, b, 3300, 2200],
        "negative": [300, 100, 100, a, 100, 3300, 2020],
        "neutral": [200, 520, a, 3340, 3900, 6600, 4200],
        "overall": [1, 1, 1, 1, 1, 1, 1],
        "total": [
            {
                "type": "Positive",
                "num": a
            },
            {
                "type": "Negative",
                "num": b
            },
            {
                "type": "Neutral",
                "num": random.randint(0, 9) * 1000
            }
        ]
    }


@app.route('/api/country/<startTime>_<endTime>')
def country(startTime,endTime):
    a = random.randint(0,9)*100
    b = random.randint(0,9)*100
    return  {
        "error_code": 0,
        "country":["USA","Canada","China","Australia","Japan"],
        "positive":[100,200,100,a,b],
        "negative":[200,100,100,b,a],
        "neutral":[100,200,100,a,a]
    }
@app.route('/api/compare/<type>')
def compare(type):
    print(type)
    a = random.randint(0, 9) * 1000
    b = random.randint(0, 9) * 1000
    c = random.randint(0, 9) * 1000
    return  {
    "error_code": 0,
     "info1":[
        {
            "type":"Positive",
            "num": a
        },
        {
            "type":"Negative",
            "num": b
        },
        {
            "type":"Neutral",
            "num": c
        },
    ],
    "info2":[
        {
            "type":"Positive",
            "num": c
        },
        {
            "type":"Negative",
            "num": a
        },
        {
            "type":"Neutral",
            "num":b
        },
    ],
    "info3":[
        {
            "type": "Positive",
            "num": c
        },
        {
            "type": "Negative",
            "num": a
        },
        {
            "type": "Neutral",
            "num": b
        },
    ]
  }

@app.route('/api/covid_byday')
def covid_byday():

    a = random.randint(0, 9) * 100
    b = random.randint(0, 9) * 100
    c = random.randint(0, 9) * 100
    return   {
    "error_code": 0,
    "date":["2020/01/01","2021/01/02","2021/01/03","2020/01/01","2021/01/02","2021/01/03"],
    "positive":[a,200,100,200,150,100],
    "negative":[200,b,100,200,150,100],
    "neutral":[100,200,c,200,150,100]
  }

if __name__ == '__main__':
    app.run()