# Random sampling of tweet data in the second half of the year 2021.
# Place_country limits in United States(US), Australia(AU), Canada(CA), New Zealand(NZ), United Kingdom(GB)
# Limit tweets published in English
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
    begin = date(2021, 9, 1)
    end = date(2021, 12, 31)
    frmt = "%Y-%m-%dT%H:%M:%SZ"
    duration = 5
    params = {
        'query': '(place_country:US OR place_country:AU OR place_country:CA OR place_country:NZ  OR place_country:GB) lang:en',
        'expansions': 'author_id,geo.place_id',
        'place.fields': 'country,country_code,full_name,geo,id,name,place_type',
        'user.fields': 'created_at,description,id,location,name,username',
        'max_results': 500
    }
    for i in range((end - begin).days + 1):
        day = begin + timedelta(days=i)
        month = str(day.month)
        if day.month < 10:
            month = '0' + month
        filename = '../Dataset/' + str(day.year) + '_' + month + '.csv'
        morning_s = str(day) + 'T00:00:00Z'
        morning_e = str(day) + 'T12:00:00Z'
        morning_e = (datetime.strptime(morning_e, frmt) - timedelta(minutes=duration)).strftime(frmt)
        start_time, end_time = randomtimes(morning_s, morning_e, duration)
        params['start_time'] = start_time
        params['end_time'] = end_time
        query_to_csv(search_url, params, filename)

        time.sleep(5)

        afternoon_s = str(day) + 'T12:00:00Z'
        afternoon_e = str(day + timedelta(days=1)) + 'T00:00:00Z'
        afternoon_e = (datetime.strptime(afternoon_e, frmt) - timedelta(minutes=duration)).strftime(frmt)
        start_time, end_time = randomtimes(afternoon_s, afternoon_e, duration)
        params['start_time'] = start_time
        params['end_time'] = end_time
        query_to_csv(search_url, params, filename)

        time.sleep(5)

        # df = pd.read_csv(filename)
        # print(tabulate(df, headers='keys', tablefmt='psql'))
        # break


if __name__ == "__main__":
    main()