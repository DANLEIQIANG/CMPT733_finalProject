from flask import Flask
import random
app = Flask(__name__)

# 多类型 friendly和unfriendly
# eda: 1.词频图  前端展示图片（eda）
# 数据内容：数据随机采样
# 推文(数据初步清洗) 用户信息
# 3.9搞完 + vedio



#指标卡 & 饼图
@app.route('/overview/key_metrics/<startTime>_<endTime>')
def overview_key_metics(startTime,endTime):
    a = random.randint(0,9)*1000
    b = random.randint(0,9)*1000
    return {
        "msg": "success",
        "startTime": startTime,
        "endTime": endTime,
        "info":[
            {
                "type":"Friendly",
                "num": a
            },
            {
                "type": "Unfriendly",
                "num":  b
            },
            {
                "type": "Total",
                "num": random.randint(0, 9) * 1000
            }
        ]
    }
#状图，点击指标卡可以切换，一共三张图
@app.route('/overview/key_metrics_byday/<startTime>_<endTime>')
def overview_key_metics_byday(startTime,endTime):
    x = random.randint(1,9)*1000
    return {
        "msg": "success",
        "startTime": startTime,
        "endTime": endTime,
        "date": ["2020/09/01","2020/09/02","2020/09/03","2020/09/04","2020/09/05","2020/09/06","2020/09/07"],
        "friendly": [x, 520, 2000, x, 3900, 3300, 2200],
        "unfriendly": [300, x, x, 3340, x, 3300, 2020],
        "overall": [x+300, x+520, x+2000, x+3340, x+3900, 6600, 4200]
    }

#要不要加时间? 预期展示各种歧视的分类和比例，排序
@app.route('/overview/type/<startTime>_<endTime>')
def overview_type(startTime,endTime):
    print("overview_type")
    return {
        "msg": "success",
        "startTime": startTime,
        "endTime": endTime,
        "items":[
            {
                "name": "good",
                "percent": 98
            },
            {
                "name": "bad",
                "percent": 50
            },
            {
                "name": "undefined",
                "percent": 30
            }
        ]
    }


@app.route('/analysis/sex/<startTime>_<endTime>')
def analysis_sex(startTime,endTime):
    return {
        "msg": "success",
        "startTime": startTime,
        "endTime": endTime,
        "date": ["2020/09/01","2020/09/02","2020/09/03","2020/09/04","2020/09/05","2020/09/06","2020/09/07"],
        "total_male":10000,
        "total_female": 12000,
        "male": [79, 52, 200, 334, 390, 330, 220],
        "female": [30, 52, 200, 334, 390, 330, 220],
        "overall": [100, 102, 500, 634, 790, 660, 420]
    }

@app.route('/analysis/age/<startTime>_<endTime>')
def analysis_age(startTime,endTime):
    return {
        "msg": "success",
        "startTime": startTime,
        "endTime": endTime,
        "date": ["2020/09/01","2020/09/02","2020/09/03","2020/09/04","2020/09/05","2020/09/06","2020/09/07"],
        "7_17":10000,
        "18_40": 10000,
        "41_65": 10000,
        "_65": 10000,
        "7_17_split": [79, 52, 200, 334, 390, 330, 220],
        "18_40_split": [30, 52, 200, 334, 390, 330, 220],
        "41_65_split": [79, 52, 200, 334, 390, 330, 220],
        "_65_split": [30, 52, 200, 334, 390, 330, 220],
        "overall": [100, 102, 500, 634, 790, 660, 420]
    }



if __name__ == '__main__':
    app.run()