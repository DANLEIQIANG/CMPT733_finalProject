import pymysql
from flask import Flask, request
from pymysql.cursors import DictCursor
 
app = Flask(__name__)

def get_time_data(start_date, end_date):
    conn = pymysql.connect(host='127.0.0.1', database='twitter', user='root', password='12345678')
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT date, labels, sum(counts) FROM tbl_country_label GROUP BY date, labels HAVING date >='%s' AND date <= '%s'; " % (str(start_date),str(end_date)))
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/api/timeselector/<startTime>_<endTime>')
def timeselector(startTime,endTime):
    li = get_time_data(startTime,endTime)
    neg_value = 0
    po_value = 0
    nu_value = 0
    date_lst = []
    lab_lst = []
    neg_lst = []
    po_lst = []
    nu_lst = []
    for dir in li:
        if dir['labels'] == 0:
            neg_lst.append(int(dir['sum(counts)']))
            neg_value += int(dir['sum(counts)'])
        elif dir['labels'] == 1:
            po_lst.append(int(dir['sum(counts)']))
            po_value += int(dir['sum(counts)'])
        else:
            nu_lst.append(int(dir['sum(counts)']))
            nu_value += int(dir['sum(counts)'])
        for k, v in dir.items():
            if k == 'date' and str(v) not in date_lst:
                v = str(v)
                date_lst.append(v)
            if k == 'labels' and v not in lab_lst:
                lab_lst.append(v)

    over_list = [1 for _ in range(len(po_lst))]

    return  {
        "error_code": 0,
        "date": date_lst,
        "positive": po_lst,
        "negative": neg_lst,
        "neutral": nu_lst,
        "overall": over_list,
        "total": [
            {
                "type": "Positive",
                "num": po_value
            },
            {
                "type": "Negative",
                "num": neg_value
            },
            {
                "type": "Neutral",
                "num": nu_value
            }
        ]
    }

def get_contry_data(start_date, end_date):
    conn = pymysql.connect(host='127.0.0.1', database='twitter', user='root', password='12345678')
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT country, date, labels, sum(counts) FROM tbl_country_label GROUP BY country, date, labels HAVING date >='%s' AND date <= '%s'; " % (str(start_date),str(end_date)))
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/api/country/<startTime>_<endTime>')
def country(startTime,endTime):
    li = get_contry_data(startTime, endTime)
    cou_lst = []
    for dir in li:
        for k, v in dir.items():
            if k == 'country' and v not in cou_lst:
                cou_lst.append(v)

    sum_lst = []
    for i in cou_lst:
        sum_lst.append({'country':i,'count_0':0, 'count_1':0, 'count_2':0})

    for i in li:
        for o in sum_lst:
            if i['country'] == o['country']:
                if i['labels'] == 0:
                    o['count_0']=o['count_0']+i['sum(counts)']
                elif i['labels'] == 1:
                    o['count_1']=o['count_1']+i['sum(counts)']
                else:
                    o['count_2']=o['count_2']+i['sum(counts)']

    neg_lst = []
    po_lst = []
    nu_lst = []
    for dir in sum_lst:
        neg_lst.append(int(dir['count_0']))
        po_lst.append(int(dir['count_1']))
        nu_lst.append(int(dir['count_2']))
        for k, v in dir.items():
            if k == 'country' and v not in cou_lst:
                cou_lst.append(v)
    
    return {
        "error_code": 0,
        "country": cou_lst,
        "positive": po_lst,
        "negative": neg_lst,
        "neutral": nu_lst
  }

def get_compare_data(compare_type):
    conn = pymysql.connect(host='127.0.0.1', database='twitter', user='root', password='12345678')
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT type, labels, period, sum(counts) FROM tbl_model_show GROUP BY type, labels, period HAVING type ='%s'; " % str(compare_type))
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/api/compare/<compare_type>')
def compare(compare_type):
    li = get_compare_data(compare_type)
    print(compare_type)
    for dir in li:
        neg_value_0 = 0
        neg_value_1 = 0
        neg_value_2 = 0
        po_value_0 = 0
        po_value_1 = 0
        po_value_2 = 0
        nu_value_0 = 0
        nu_value_1 = 0
        nu_value_2 = 0

        for dir in li:
            if dir['labels'] == 0:
                if dir['period'] == 0:
                    neg_value_0 = int(dir['sum(counts)'])
                elif dir['period'] == 1:
                    neg_value_1 = int(dir['sum(counts)'])
                else:
                    neg_value_2 = int(dir['sum(counts)'])
            elif dir['labels'] == 1:
                if dir['period'] == 0:
                    po_value_0 = int(dir['sum(counts)'])
                elif dir['period'] == 1:
                    po_value_1 = int(dir['sum(counts)'])
                else:
                    po_value_2 = int(dir['sum(counts)'])
            else:
                if dir['period'] == 0:
                    nu_value_0 = int(dir['sum(counts)'])
                elif dir['period'] == 1:
                    nu_value_1 = int(dir['sum(counts)'])
                else:
                    nu_value_2 = int(dir['sum(counts)'])

    return  {
    "error_code": 0,
     "info1":[
        {
            "type":"Positive",
            "num": po_value_0
        },
        {
            "type":"Negative",
            "num": neg_value_0
        },
        {
            "type":"Neutral",
            "num": nu_value_0
        },
    ],
    "info2":[
        {
            "type":"Positive",
            "num": po_value_1
        },
        {
            "type":"Negative",
            "num": neg_value_1
        },
        {
            "type":"Neutral",
            "num": nu_value_1
        },
    ],
    "info3":[
        {
            "type": "Positive",
            "num": po_value_2
        },
        {
            "type": "Negative",
            "num": neg_value_2
        },
        {
            "type": "Neutral",
            "num": nu_value_2
        },
    ]
  }

def get_covidby_data():
    conn = pymysql.connect(host='127.0.0.1', database='twitter', user='root', password='12345678')
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT date, type, labels, period, sum(counts) FROM tbl_model_show GROUP BY type, labels, date, period HAVING type ='covid' and period = 1; ")
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/api/covid_byday')
def covid_byday():
    li = get_contry_data()
    date_lst = []
    neg_lst = []
    po_lst = []
    nu_lst = []
    for dir in li:
        if dir['labels'] == 0:
            neg_lst.append(int(dir['sum(counts)']))
        elif dir['labels'] == 1:
            po_lst.append(int(dir['sum(counts)']))
        else:
            nu_lst.append(int(dir['sum(counts)']))
        for k, v in dir.items():
            if k == 'date' and str(v) not in date_lst:
                v = str(v)
                date_lst.append(v)
    return   {
    "error_code": 0,
    "date": date_lst,
    "positive": po_lst,
    "negative": neg_lst,
    "neutral": nu_lst
  }

if __name__ == '__main__':
    app.run()