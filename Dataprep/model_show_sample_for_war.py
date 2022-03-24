"""
Random sampling of tweet data.
Place_country limits in United States(US), Australia(AU), Canada(CA), New Zealand(NZ), United Kingdom(GB)
Limit tweets published in English
1. Normal week
From 2021-09-24 to 2022-09-30, filtered 500 tweets from every 3 hours respectively
2. Holiday week
From 2021-12-24 to 2022-12-30, filtered 500 tweets from every 3 hours respectively
3. Week after war
From 2022-02-24 to 2022-03-02, filtered 500 tweets from every 3 hours respectively
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
        'query': '(place_country:US OR place_country:AU OR place_country:CA OR place_country:NZ  OR place_country:GB) lang:en',
        'expansions': 'author_id,geo.place_id',
        'place.fields': 'country,country_code,full_name,geo,id,name,place_type',
        'user.fields': 'created_at,description,id,location,name,username',
        'max_results': 500
    }
    # begin = date(2021, 9, 24)
    # end = date(2021, 9, 30)
    # for i in range((end - begin).days + 1):
    #     day = begin + timedelta(days=i)
    #     filename = '../Dataset/model_show_sample_for_war/normal_week/' + str(day) + '.csv'
    #     s = str(day) + 'T00:00:00Z'
    #     for j in range(24):
    #         e = (datetime.strptime(s, frmt) + timedelta(hours=3)).strftime(frmt)
    #         start_time, end_time = randomtimes(s, e, duration)
    #         params['start_time'] = start_time
    #         params['end_time'] = end_time
    #         s = e
    #         query_to_csv(search_url, params, filename)
    #         time.sleep(5)

    begin = date(2021, 12, 24)
    end = date(2021, 12, 30)
    for i in range((end - begin).days + 1):
        day = begin + timedelta(days=i)
        filename = '../Dataset/model_show_sample_for_war/holiday_week/' + str(day) + '.csv'
        s = str(day) + 'T00:00:00Z'
        for j in range(24):
            e = (datetime.strptime(s, frmt) + timedelta(hours=3)).strftime(frmt)
            start_time, end_time = randomtimes(s, e, duration)
            params['start_time'] = start_time
            params['end_time'] = end_time
            s = e
            query_to_csv(search_url, params, filename)
            time.sleep(5)

    begin = date(2022, 2, 24)
    end = date(2022, 3, 2)
    for i in range((end - begin).days + 1):
        day = begin + timedelta(days=i)
        filename = '../Dataset/model_show_sample_for_war/war_week/' + str(day) + '.csv'
        s = str(day) + 'T00:00:00Z'
        for j in range(24):
            e = (datetime.strptime(s, frmt) + timedelta(hours=3)).strftime(frmt)
            start_time, end_time = randomtimes(s, e, duration)
            params['start_time'] = start_time
            params['end_time'] = end_time
            s = e
            query_to_csv(search_url, params, filename)
            time.sleep(5)

        # df = pd.read_csv(filename)
        # print(tabulate(df, headers='keys', tablefmt='psql'))
        # break


if __name__ == "__main__":
    main()