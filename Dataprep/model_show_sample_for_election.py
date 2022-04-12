"""
Random sampling of tweet data.
Place_country limits in United States(US)

Limit tweets published in English
1. The 2016 U.S. presidential election(Trump)
From 2016-12-19 to 2016-12-25, filtered 500 tweets from every 3 hours respectively
2. The 2020 U.S. presidential election(Biden)
From 2020-12-14 to 2020-12-20, filtered 500 tweets from every 3 hours respectively
"""
import random
import time
from datetime import datetime, timedelta, date
from full_archive_search import *


def randomtimes(start, end, duration, frmt="%Y-%m-%dT%H:%M:%SZ"):
    stime = datetime.strptime(start, frmt)
    etime = datetime.strptime(end, frmt)
    start_time = random.random() * (etime - stime) + stime
    # time_str = [t.strftime(frmt) for t in time_datetime]
    end_time = start_time + timedelta(minutes=duration)
    return start_time.strftime(frmt), end_time.strftime(frmt)


def main():
    frmt = "%Y-%m-%dT%H:%M:%SZ"
    duration = 5
    params = {
        'query': '(trump OR biden OR election)  place_country:US lang:en',
        'expansions': 'author_id,geo.place_id',
        'place.fields': 'country,country_code,full_name,geo,id,name,place_type',
        'user.fields': 'created_at,description,id,location,name,username',
        'max_results': 500
    }
    begin = date(2016, 12, 19)
    end = date(2016, 12, 25)
    for i in range((end - begin).days + 1):
        day = begin + timedelta(days=i)
        filename = '../Dataset/model_show_sample_for_election/trump/' + str(day) + '.csv'
        s = str(day) + 'T00:00:00Z'
        for j in range(8):
            e = (datetime.strptime(s, frmt) + timedelta(hours=3)).strftime(frmt)
            start_time, end_time = randomtimes(s, e, duration)
            params['start_time'] = start_time
            params['end_time'] = end_time
            s = e
            query_to_csv(search_url, params, filename)
            time.sleep(5)

    begin = date(2020, 12, 14)
    end = date(2020, 12, 20)
    for i in range((end - begin).days + 1):
        day = begin + timedelta(days=i)
        filename = '../Dataset/model_show_sample_for_election/biden/' + str(day) + '.csv'
        s = str(day) + 'T00:00:00Z'
        for j in range(8):
            e = (datetime.strptime(s, frmt) + timedelta(hours=3)).strftime(frmt)
            start_time, end_time = randomtimes(s, e, duration)
            params['start_time'] = start_time
            params['end_time'] = end_time
            s = e
            query_to_csv(search_url, params, filename)
            time.sleep(5)


if __name__ == "__main__":
    main()